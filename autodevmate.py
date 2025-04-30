import streamlit as st
from agno.agent import Agent
from agno.models.ibm import WatsonX

# Init Granite Agent
agent = Agent(model=WatsonX(id="ibm/granite-3-2-8b-instruct"), markdown=True)

st.set_page_config(page_title="AutoDevMate - IBM Granite Assistant", layout="wide")
st.title("🤖 AutoDevMate – IBM Granite-Powered Dev Tools")

tabs = st.tabs(["🔍 PR Review Engine", "🧱 Boilerplate Generator", "💬 Dev Chat Assistant"])

# --- Helper: Run with token and cost tracking ---
def run_with_metrics(prompt: str):
    result = agent.run(prompt)
    input_tokens = sum(result.metrics.get("input_tokens", []))
    output_tokens = sum(result.metrics.get("output_tokens", []))
    input_cost = input_tokens / 1000 * 0.001
    output_cost = output_tokens / 1000 * 0.002
    total_cost = input_cost + output_cost
    return result.content, input_tokens, output_tokens, input_cost, output_cost, total_cost

# --- 1. PR Review Engine ---
with tabs[0]:
    st.header("🔍 Pull Request Review Engine")
    pr_input = st.text_area("Paste Git Diff or Pull Request Patch:", height=300)
    if st.button("🧠 Analyze Pull Request"):
        with st.spinner("Reviewing..."):
            prompt = f"""
You are a senior software engineer. Analyze the following Git diff and provide:
1. A summary of the change
2. Code quality or security concerns
3. Missing tests or logical issues

Diff:
{pr_input}
"""
            content, in_tok, out_tok, in_cost, out_cost, total = run_with_metrics(prompt)
            st.markdown("### 📝 Review Summary")
            st.write(content)

            st.markdown("### 💰 Token Usage")
            st.text_area("Cost & Token Breakdown", value=f"""
Input Tokens:  {in_tok}   (${in_cost:.4f})
Output Tokens: {out_tok}   (${out_cost:.4f})
------------------------------
Total Estimated Cost: ${total:.4f}
""", height=120)

# --- 2. Boilerplate Generator ---
with tabs[1]:
    st.header("🧱 Boilerplate Code Generator")
    user_prompt = st.text_input("Enter prompt (e.g., 'Create a Flask API with login')")

    if st.button("🚀 Generate Code"):
        with st.spinner("Generating boilerplate code..."):
            prompt = f"""Generate a production-ready code scaffold for the following request:\n\n{user_prompt}\n\nInclude necessary structure and inline comments."""
            content, in_tok, out_tok, in_cost, out_cost, total = run_with_metrics(prompt)
            st.markdown("### 🧾 Generated Code")
            st.code(content, language="python")
            st.download_button("📄 Download Code", content, file_name="boilerplate.py")

            st.markdown("### 💰 Token Usage")
            st.text_area("Cost & Token Breakdown", value=f"""
Input Tokens:  {in_tok}   (${in_cost:.4f})
Output Tokens: {out_tok}   (${out_cost:.4f})
------------------------------
Total Estimated Cost: ${total:.4f}
""", height=120)

# --- 3. Developer Chat Assistant ---
with tabs[2]:
    st.header("💬 Developer Chat Assistant")
    chat_input = st.text_area("Ask something about your code or dev setup", height=150)
    uploaded_code = st.file_uploader("Optional: Upload code file (e.g., .py, .js, .yaml)", type=["py", "js", "json", "yaml", "txt"])

    code_content = ""
    if uploaded_code:
        code_content = uploaded_code.read().decode("utf-8", errors="ignore")
        st.markdown("### 📄 Uploaded Code")
        st.code(code_content)

    if st.button("💡 Ask Granite"):
        with st.spinner("Thinking..."):
            prompt = f"""
You are a helpful software assistant.

User question: {chat_input}

Uploaded code (if any):
{code_content}
"""
            content, in_tok, out_tok, in_cost, out_cost, total = run_with_metrics(prompt)
            st.markdown("### 🤖 Response")
            st.write(content)

            st.markdown("### 💰 Token Usage")
            st.text_area("Cost & Token Breakdown", value=f"""
Input Tokens:  {in_tok}   (${in_cost:.4f})
Output Tokens: {out_tok}   (${out_cost:.4f})
------------------------------
Total Estimated Cost: ${total:.4f}
""", height=120)
