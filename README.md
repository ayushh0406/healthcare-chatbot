Healthcare Chatbot Mini Project
-------------------------------

Project Overview:
This is a simple, rule-based healthcare chatbot developed as a mini NLP project using only core Python functionality (no advanced NLP/ML libraries).  
It answers common healthcare-related questions about symptoms, emergencies, diet, hygiene, vaccinations, and advice for special groups like children, elderly, and pregnant women.

Objective:
- Implement core NLP logic using Python without external NLP or ML libraries.
- Use pattern matching, regular expressions, and keyword-based rules to process user queries.
- Provide relevant healthcare information through an interactive chatbot interface.
- Demonstrate fundamental understanding of rule-based NLP techniques.

Files in Project:
---------------
1. healthcare_chatbot.py  
   - Contains all chatbot logic: preprocessing input, defining rules, and generating responses.
   - No external libraries other than Python built-ins and `re` module.

2. healthcare_chatbot_app.py  
   - Streamlit web app frontend for interactive use.
   - Displays an engaging UI with chat bubbles, emojis, and clean layout.
   - Connects user input to chatbot logic and renders conversation dynamically.

3. requirements.txt  
   - Lists required Python package: `streamlit`  
   (Use: `pip install -r requirements.txt` to set up environment)

How the Code Works:
-------------------
- User input is preprocessed (lowercased, punctuation removed).
- The chatbot checks input against a comprehensive set of keyword-based rules implemented with conditional checks and regular expressions.
- Rules cover a wide range of health-related queries: emergencies, symptoms, diet, hygiene, vaccinations, and special groups.
- For recognized patterns, the bot returns predefined helpful responses.
- If no rule matches, a fallback response politely asks the user to rephrase.
- The web app uses Streamlit for a user-friendly frontend with message bubbles and scroll functionality.

How to Run the Program:
-----------------------
1. Set up Python environment (Python 3.7+ recommended).
2. Install dependencies:

 `pip install -r requirements.txt`


3. Run the Streamlit app:
'streamlit run healthcare_chatbot_app.py'


4. The app will open in your browser at `http://localhost:8501`.
5. Type your healthcare-related questions in the input box.
6. Chat freely until you type 'exit', 'quit', or 'bye' to close.

Example Queries to Try:
----------------------
- "Hi"
- "I have a headache"
- "What should I eat for good nutrition?"
- "Is vaccination important?"
- "My child has a rash"
- "Pregnancy care tips?"
- "I am unconscious"  (triggers emergency response)
- "Thank you"

Rules and Logic Summary:
------------------------
- Uses manual keyword matching (if-else checks) with regular expressions.
- Covers emergency alerts for critical symptoms.
- Identifies a wide range of common and less common symptoms.
- Provides diet and nutrition advice.
- Includes hygiene and vaccination guidance.
- Special advice for children, elderly, and pregnant women.
- Polite greetings and fallback responses.
- No external NLP or AI model usage, purely rule-based.

Project Highlights:
-------------------
- Demonstrates core NLP principles by building token-based, pattern-matching chatbot logic from scratch.
- Clear, well-commented code explains each step and decision.
- Easy to maintain and extend by adding new keywords and responses.
- Professional yet friendly UI using Streamlit with chat bubbles and emojis.
- Fully compliant with academic mini-project guidelines restricting use of advanced NLP frameworks.

Author: [Your Name]  
Date: [Project Completion Date]

---

If you want me to help you generate a `requirements.txt` or instructions for deployment, just ask!
   
