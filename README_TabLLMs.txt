TabLLMs - Talk to Your Data
============================

TabLLMs is a simple and powerful Streamlit app that allows users to upload a CSV file and ask natural language questions about their dataset. These queries are translated into Python pandas code using a language model and executed to return the result.

Features:
---------
- Upload any CSV file.
- Preview the top 20 rows.
- Ask natural language questions like "What is the average salary by department?"
- View the LLM-generated pandas code.
- See the result of the query execution.

Files:
------
1. app.py
   - The main Streamlit app.
   - Handles file upload, user queries, code generation, and result display.

2. utils/llm_utils.py
   - Contains the function `query_to_code` that calls the OpenAI API.
   - Converts user natural language input into pandas code.

Setup Instructions:
-------------------
1. Clone the repository.
2. Install dependencies:
   pip install -r requirements.txt
3. Add your OpenAI API key in `llm_utils.py` or use an environment variable.
4. Run the app:
   streamlit run app.py

Security Note:
--------------
Avoid hardcoding sensitive API keys. Use environment variables instead.

Disclaimer:
-----------
This app executes dynamically generated code. Use it with caution, especially on untrusted datasets or inputs.