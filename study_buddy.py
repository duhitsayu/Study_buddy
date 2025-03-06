import streamlit as st
import google.generativeai as genai


genai.configure(api_key="[your_api_key]")
model = genai.GenerativeModel("gemini-1.5-flash") 

st.title("📚 Personalized Study Buddy")
st.markdown("Enter a topic, choose a mode, and let AI help you learn!")

topic = st.text_input("Enter a topic (e.g., Python loops, Photosynthesis):", "")
mode = st.selectbox("Choose a mode:", ["Explain", "Quiz"])

if st.button("Go"):
    if topic.strip() == "":
        st.error("Please enter a topic!")
    else:
        if mode == "Explain":
            prompt = f"Explain {topic} in 100 words or less, in simple terms for beginners."
        else:
            prompt = f"Generate 3 multiple-choice questions about {topic} with 4 options each and the correct answers."
        try:
            response = model.generate_content(prompt)
            output = response.text
            st.markdown("### Your Study Buddy Result")
            if mode == "Explain":
                st.write(output)
            else:
                st.markdown(output)
        except Exception as e:
            st.error(f"Oops! Something went wrong: {str(e)}")
            st.write("Backup response: 'AI is thinking—try again!'")

st.markdown("---")
st.write("Built with ❤️ by [Akki].")