# 💬 Flask AI Chatbot (Hugging Face + Kimi Model)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black.svg)
![HuggingFace](https://img.shields.io/badge/HuggingFace-API-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A modern **AI-powered chat application** built with **Flask** and integrated with **Hugging Face OpenAI-compatible API Router**, using the powerful model:

> 🤖 `moonshotai/Kimi-K2-Instruct-0905`


---

## 🚀 Features

- ⚡ Real-time AI chat responses
- 🌐 Clean web-based UI (HTML + CSS + JS)
- 🤖 Powered by Hugging Face LLM API
- 🔥 Flask REST API backend
- 💬 Simple and fast messaging system
- 📡 JSON-based communication
- 🧠 Uses `Kimi-K2-Instruct` model

---

## 🛠️ Tech Stack

| Layer     | Technology                              |
|-----------|------------------------------------------|
| Backend   | Flask (Python)                          |
| Frontend  | HTML, CSS, JavaScript                   |
| AI Model  | MoonshotAI Kimi-K2                      |
| API Layer | Hugging Face Router (OpenAI compatible) |

---

## 📁 Project Structure

```bash
project/
│── app.py
│── templates/
│   └── index.html
│── static/
│   └── style.css
│── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/flask-ai-chatbot.git
cd flask-ai-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask openai python-dotenv
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
HF_API_KEY=your_huggingface_api_key
```

⚠️ Never expose API keys in public repositories.

---

## ▶️ Run the Project

```bash
python app.py
```

Then open:

```bash
http://127.0.0.1:5000/
```

---

## 🔁 API Workflow

1. User sends message from UI
2. Flask receives request at `/chat`
3. Message is sent to Hugging Face API
4. AI model generates response
5. Response is returned as JSON
6. Frontend displays reply in chat UI

---

## 📡 API Endpoint

### POST `/chat`

### Request

```json
{
  "message": "Hello AI"
}
```

### Response

```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

## 🧠 Code Overview

### 🔹 Flask Backend

- Handles routing (`/` and `/chat`)
- Sends requests to Hugging Face API
- Returns AI response as JSON

### 🔹 Frontend

- Chat UI built with HTML/CSS
- Uses JavaScript `fetch()` for API calls
- Displays real-time responses

---

## 📌 Future Improvements

- 💬 Chat history storage (database integration)
- 🎨 Modern UI (React / Tailwind CSS)
- 🔐 User login system
- ☁️ Deployment (Render / AWS / Hugging Face Spaces)
- 🧠 Multi-model selection feature

---

## ⚠️ Security Warning

- Do NOT commit API keys to GitHub
- Use `.env` or secret managers
- Rotate keys if exposed

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

### Hamayun Malik

💡 AI & Software Developer  
🚀 Building intelligent systems & AI applications

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub and share it with others.

---
