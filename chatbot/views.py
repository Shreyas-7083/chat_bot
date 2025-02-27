import json
import os
import difflib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Directory where documentation text files are stored
DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")

# Load documentation texts into a dictionary
documentation = {}

def load_documentation():
    docs = {
        "Segment": "segment.txt",
        "mParticle": "mparticle.txt",
        "Lytics": "lytics.txt",
        "Zeotap": "zeotap.txt"
    }
    for cdp, filename in docs.items():
        file_path = os.path.join(DOCS_DIR, filename)
        try:
            with open(file_path, "r", encoding="utf8") as f:
                documentation[cdp] = f.read()
        except Exception as e:
            documentation[cdp] = ""
            print(f"Error loading {filename}: {e}")

# Load documentation when the module is imported
load_documentation()

@csrf_exempt
def search_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get("query", "").strip()
            if not query:
                return JsonResponse({"error": "Query is required."}, status=400)

            # Check if the query is a comparison query
            if "compare" in query.lower() or "difference" in query.lower():
                # List of supported CDPs
                cdps = ["Segment", "mParticle", "Lytics", "Zeotap"]
                found_cdps = [cdp for cdp in cdps if cdp.lower() in query.lower()]
                if len(found_cdps) >= 2:
                    comparison_result = {}
                    # Fetch a snippet from each identified CDP
                    for cdp in found_cdps[:2]:
                        text = documentation.get(cdp, "")
                        snippet = text[:300] + "..." if text else "No content available."
                        comparison_result[cdp] = snippet
                    return JsonResponse({"comparison": comparison_result})
                else:
                    return JsonResponse({"answer": "Could not identify two CDPs to compare."})
            else:
                # Normal search: find the best matching CDP documentation
                best_match = None
                best_score = 0.0
                best_cdp = None
                for cdp, text in documentation.items():
                    ratio = difflib.SequenceMatcher(None, query.lower(), text.lower()).ratio()
                    if ratio > best_score:
                        best_score = ratio
                        best_match = text
                        best_cdp = cdp
                if best_score < 0.1:
                    return JsonResponse({"answer": "Sorry, I couldn't find any relevant information."})
                snippet = best_match[:500] + "..."
                return JsonResponse({"cdp": best_cdp, "answer": snippet})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
