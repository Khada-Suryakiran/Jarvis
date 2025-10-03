# Cogniflow 🧑‍💻🤖

Jarvis is a lightweight Python-based personal assistant web application.  
It provides a simple interface (web UI) to interact with assistant features such as task automation, AI responses, and external API integration.

---

## 🚀 Features
- Web-based interface (HTML/CSS/JS frontend + Python backend).
- Template-driven UI (`templates/` for HTML, `static/` for styles & scripts).
- Environment-based configuration (`.env` file for secrets/API keys).
- Extensible design — add custom commands, AI logic, or API calls.

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask or similar framework)  
- **Frontend:** HTML, CSS, JavaScript  
- **Config:** `.env` for environment variables  
- **Dependencies:** Listed in `requirements.txt`

---

## 📂 Project Structure
```
Jarvis/
│── app.py             # Main application entry point
│── requirements.txt   # Python dependencies
│── .env               # Environment variables (do not commit sensitive keys!)
│── static/            # CSS, JS, and static assets
│── templates/         # HTML templates for UI
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/Khada-Suryakiran/Jarvis.git
cd Jarvis
```

### 2. Create & activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Create a `.env` file in the root directory (if not already present):
```env
GOOGLE_GENAI_API_KEY=your_google_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the application
```bash
python app.py
```

By default, the app will be available at:  
👉 http://127.0.0.1:5000/

---

## 🔑 API Keys Setup

Jarvis can integrate with **Google Gemini** and **OpenAI GPT** models.  
To enable these features, you need to set up API keys in your `.env` file.

### 1. Google Gemini API Key
- Sign in to [Google AI Studio](https://aistudio.google.com/).
- Create a new project (if you don’t have one).
- Generate an API key under **API Keys**.
- Copy the key and paste it into your `.env` file:

```env
GOOGLE_GENAI_API_KEY=your_google_gemini_api_key
```

---

### 2. OpenAI API Key
- Sign up or log in at [OpenAI](https://platform.openai.com/).
- Go to **API Keys** in your account dashboard.
- Click **Create new secret key** and copy it.
- Paste it into your `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

### Example `.env` file
```env
GOOGLE_GENAI_API_KEY=your_google_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

⚠️ **Important:**  
- Never share your API keys publicly or commit them to GitHub.  
- Keep `.env` file in your local system only.  
- Add `.env` to `.gitignore` to avoid accidental uploads.  

---

## 🧩 Future Improvements
- Add voice command support (SpeechRecognition / gTTS).
- Integrate AI APIs (OpenAI, Gemini, HuggingFace, etc.).
- Build task automation (calendar, reminders, system commands).
- Add authentication system for multiple users.

---

## 📜 License
This project currently has no license.  
You can choose one (MIT recommended if you want it open-source).

---

## 👨‍💻 Author
Developed by **Khada Suryakiran**  
🔗 [GitHub Profile](https://github.com/Khada-Suryakiran)
