
# Personalized Study Buddy App

-> [try it here](https://huggingface.co/spaces/duhitsayu/studybuddy)

A smart, AI-powered learning tool. Enter any topic, choose a mode (Explain or Quiz), and get instant, personalized study content—perfect for students and learners! This app leverages cutting-edge AI to generate beginner-friendly explanations or multiple-choice quizzes on demand.
## Screenshots
![image](https://github.com/user-attachments/assets/78f0d5c9-bb1c-49d7-8a20-3e61652e3167)
**output**-
![image](https://github.com/user-attachments/assets/901cac08-fdbe-47d6-b736-428a073c53fe)


## Features
- **Dual Modes:**  
  - **Explain:** Get a concise, 100-word explanation of any topic.  
  - **Quiz:** Receive 3 multiple-choice questions with answers to test your knowledge.  
- **Instant AI Responses:** Powered by Google Gemini (free tier) or adaptable to other LLMs.  
- **User-Friendly Interface:** Built with Streamlit for a clean, interactive experience.  
- **Error Handling:** Graceful fallbacks for empty inputs or API hiccups.  

## Demo
- **Explain Mode:** Input "Python loops" → "Loops in Python repeat code. A `for` loop iterates over a sequence..."
- **Quiz Mode:** Input "Photosynthesis" → "1. What gas do plants use? a) Oxygen b) CO2 **Answer:** b)..."

## Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io) - Python-based web app framework.  
- **Backend:** Python - Logic and API integration.  
- **AI:** [Google Gemini API](https://makersuite.google.com) - Free tier for text generation.  
- **Environment:** Local or virtual env (e.g., `venv`).  

## Prerequisites
- Python 3.8+  
- A free [Google Gemini API key](https://makersuite.google.com) (or another LLM API key).  
- Git (to clone this repo).

## Installation
1. **Clone the Repo:**  
   ```bash
   git clone https://github.com/yourusername/personalized-study-buddy.git
   cd personalized-study-buddy
   ```
2. **Set Up Virtual Environment (Optional but Recommended):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Install Dependencies:**  
   ```bash
   pip install streamlit google-generativeai
   ```
4. **Add Your API Key:**  
   - Sign up at [makersuite.google.com](https://makersuite.google.com), get a Gemini API key.  
   - Replace `"your-gemini-api-key-here"` in `study_buddy.py` with your key:
     ```python
     genai.configure(api_key="your-gemini-api-key-here")
     ```

## Running the App
1. **Start the App:**  
   ```bash
   streamlit run study_buddy.py
   ```
2. **Open Your Browser:**  
   - Go to `http://localhost:8501`.  
   - Enter a topic, pick a mode, hit "Go"—watch AI do its magic!

## Usage
- **Explain Mode:** Type "Blockchain" → Get a simple explanation.  
- **Quiz Mode:** Type "Cell division" → Answer 3 MCQs.  
- **Error Handling:** No topic? See "Please enter a topic!" API down? Fallback text appears.

## Alternative APIs
Ran out of OpenAI credits? Try these:  
- **Hugging Face:** Use `mistralai/Mixtral-8x7B-Instruct-v0.1` (free tier, `pip install huggingface_hub`).  
- **OpenAI:** Add billing at [platform.openai.com](https://platform.openai.com) if you prefer GPT.

## Contributing
- Fork this repo, tweak the code, submit a pull request—let’s make learning smarter together!  
- Issues? Open a ticket [here](https://github.com/yourusername/Study_buddy/issues).

## License
MIT License—free to use, modify, and share. See [LICENSE](LICENSE) for details.

## Acknowledgments
- Built with ❤️ by akki.  


---

Happy coding, and good luck! 🚀


