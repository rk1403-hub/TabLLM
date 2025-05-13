import streamlit as st
import pandas as pd
from utils.llm_utils import query_to_code

st.set_page_config(page_title="TabLLMs - Talk to Your Data", layout="wide")
st.title("📊 TabLLMs - Talk to Your Data")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Show preview of data
    st.subheader("Top 20 Rows of CSV")
    st.dataframe(df.head(20), use_container_width=True)

    # Ask user for a natural language query
    st.subheader("Ask a question about your data:")
    query = st.text_input("E.g., What is the average age per city?")

    if query:
        st.info("Sending query to LLM...")
        code = query_to_code(query, df.head(5).to_string())

        st.subheader("LLM-Generated Code:")
        st.code(code, language='python')

        try:
            local_vars = {"df": df.copy()}
            exec(code, {}, local_vars)

            result = local_vars.get("result", None)
            if result is not None:
                st.success("✅ Result:")
                st.dataframe(result, use_container_width=True)
            else:
                st.warning("⚠️ No `result` variable found in the code.")
        except Exception as e:
            st.error(f"❌ Error executing code: {e}")
