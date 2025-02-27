import React, { useState } from "react";
import axios from "axios";
import "./chatbot.css"; // Ensure this matches the actual file name

const Chatbot = () => {
  const [query, setQuery] = useState("");
  const [conversation, setConversation] = useState([]);

  const sendQuery = async () => {
    if (!query) return;
    // Add user's message to conversation
    setConversation((prev) => [...prev, { sender: "user", text: query }]);
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/search/", { query });
      console.log("Response data:", response.data);
      if (response.data.comparison) {
        // Handle cross-CDP comparison response
        const comparisons = response.data.comparison;
        let compText = "";
        Object.keys(comparisons).forEach((cdp) => {
          compText += `${cdp}: ${comparisons[cdp]}\n\n`;
        });
        setConversation((prev) => [
          ...prev,
          { sender: "bot", text: compText }
        ]);
      } else {
        // Normal response
        const answer = response.data.answer;
        const cdp = response.data.cdp || "";
        setConversation((prev) => [
          ...prev,
          { sender: "bot", text: cdp ? `${cdp}: ${answer}` : answer }
        ]);
      }
    } catch (error) {
      console.error("Error:", error);
      setConversation((prev) => [
        ...prev,
        { sender: "bot", text: "Error fetching answer." }
      ]);
    }
    setQuery("");
  };

  return (
    <div className="chatbot-container">
      <h2>CDP Support Chatbot</h2>
      <div className="chat-window">
        {conversation.map((msg, idx) => (
          <div key={idx} className={`chat-message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask your question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={(e) => { if (e.key === "Enter") sendQuery(); }}
        />
        <button onClick={sendQuery}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
