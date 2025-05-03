
import streamlit as st
import openai

st.set_page_config(page_title="AI Email Generator", page_icon="✉️")

st.title("📧 AI Email Generator")
st.write("Generate professional emails using AI. Just enter your details below.")

openai_api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

recipient = st.text_input("👤 Recipient Type (e.g. Manager, Friend)")
purpose = st.text_input("🎯 Purpose of the Email")
tone = st.selectbox("🎨 Tone", ["Formal", "Friendly", "Persuasive", "Apologetic", "Thankful"])
message = st.text_area("📝 Key Message (what should the email say?)")

if st.button("Generate Email") and openai_api_key:
    prompt = f"""
    You are an expert email writer.
    Write a {tone.lower()} email to a {recipient}.
    Purpose: {purpose}
    Main Message: {message}
    Make it clear, polite, and structured. Add a suitable subject line.
    """
    try:
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        email_text = response["choices"][0]["message"]["content"]
        st.subheader("✉️ Generated Email")
        st.code(email_text)
    except Exception as e:
        st.error(f"Error: {e}")
elif st.button("Generate Email"):
    st.warning("Please enter your OpenAI API key to generate the email.")
