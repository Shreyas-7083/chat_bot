
---

Final README for Assignment 2:
## Building a Support Agent Chatbot for CDP CDP Support Agent Chatbot

```markdown
# CDP Support Agent Chatbot

This project is developed as part of the Zeotap Software Engineer Intern Assignment (Jan 2025). It is a Django-based backend that powers a support agent chatbot capable of answering "how-to" questions related to four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant information from the official documentation to guide users in performing specific tasks.

---

## Table of Contents

- [Objective](#objective)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Structures & Design](#data-structures--design)
- [Installation & Setup](#installation--setup)
- [Usage Instructions](#usage-instructions)
- [Non-Functional Improvements](#non-functional-improvements)
- [Project Structure](#project-structure)
- [Additional Notes](#additional-notes)

---

## Objective

Develop a chatbot that understands and responds to "how-to" questions for the following CDPs: Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant sections from each CDP's documentation and returns answer snippets, with support for handling question variations and bonus features like cross-CDP comparisons.

---

## Features

### Core Functionalities
- **Answer "How-to" Questions:**  
  Processes queries and returns relevant instructional snippets from documentation.
- **Documentation Extraction:**  
  Loads documentation from text files (`segment.txt`, `mparticle.txt`, `lytics.txt`, `zeotap.txt`) and uses fuzzy matching (difflib) to find the best match.
- **Variation Handling:**  
  Supports differences in phrasing and question length using difflib’s similarity ratio.
- **API Endpoint:**  
  A POST endpoint `/api/search/` accepts a JSON payload with the query and returns a JSON response.

### Bonus Features
- **Cross-CDP Comparisons:**  
  If the query indicates a comparison (e.g., "compare Segment and Lytics"), the chatbot returns snippets from both CDPs.
- **Advanced Query Handling:**  
  Can be extended to use more advanced NLP techniques for complex, platform-specific queries.

---

## Technologies Used

- **Backend:**  
  - Django with Django REST Framework  
  - Python’s difflib for fuzzy matching
- **Documentation Handling:**  
  - Text files (`segment.txt`, `mparticle.txt`, `lytics.txt`, `zeotap.txt`) are loaded and indexed for search.

---

## Data Structures & Design

- **Documentation Data:**  
  Documentation for each CDP is stored in a separate text file within the `chatbot/docs/` directory.
- **Search Logic:**  
  The backend loads the text files into memory and uses `difflib.SequenceMatcher` to calculate similarity ratios between the user query and the content of each file.
- **Response Format:**  
  - Standard queries return a JSON object with `cdp` and `answer` keys.
  - Comparison queries return a JSON object with a `comparison` key containing snippets from multiple CDPs.

---

## Installation & Setup

### Prerequisites
- Python and pip
- Django

### Backend Setup
1. **Clone the Repository:**
   ```bash
   git clone  https://github.com/Shreyas-7083/chat_bot.git
