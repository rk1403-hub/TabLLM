# utils/llm_utils.py

from openai import OpenAI

# Initialize OpenAI client (set your key here or via environment variable)
client = OpenAI(api_key="insert key")

def query_to_code(user_query, df_head):
    """
    Converts a user's natural language question into pandas code using an LLM.
    Assumes a pandas DataFrame called `df` exists.
    """
    prompt = f"""
You are a Python data analyst using pandas. The user uploaded a dataset that looks like this:

{df_head}

Convert the following user request into valid pandas code using a DataFrame called `df`.
Store the final result in a variable called `result`.

User request: {user_query}

Python code:
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or "gpt-4"
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=300
        )
        code = response.choices[0].message.content.strip()
        return code
    except Exception as e:
        return f"# Error occurred: {e}"
