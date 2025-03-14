# 🤖 GigaChat Streamlit Bot

A powerful AI chatbot built using **Streamlit** and **GigaChat API**. This bot enables real-time conversations with AI, supporting both text and image responses.

---

## 🚀 Features
- 🔐 **Secure Authentication** – Retrieves and manages API access tokens.
- 💬 **Interactive Chat** – AI-powered text responses.
- 🖼️ **Image Handling** – AI-generated image support.
- 🎨 **User-Friendly UI** – Built with Streamlit for a smooth experience.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/gigachat-bot.git
cd gigachat-bot
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure API Credentials
Create a `.streamlit/secrets.toml` file and add:
```toml
[secrets]
CLIENT_ID = "your_client_id"
SECRET = "your_secret_key"
```

---

## ▶️ Running the Application
```sh
streamlit run main.py
```

---

## 📂 Project Structure
```
📦 gigachat-bot
├── 📜 main.py        # Streamlit UI and chatbot logic
├── 📜 gigachat_api.py # API interaction functions
├── 📜 utils.py        # Helper functions
├── 📜 requirements.txt # Dependencies
├── 📜 README.md       # Documentation
```

---

## 🎯 Usage
1. Start the chatbot.
2. Enter your message in the chat input.
3. Receive AI responses (text or images).
4. Enjoy the conversation!

---

## 🔧 Future Enhancements
- [ ] Improve UI with more customization.
- [ ] Add support for voice input.
- [ ] Implement session-based history management.

---

## 🤝 Contributing
We welcome contributions! Feel free to submit pull requests to improve the project.

---

## 📜 License
This project is licensed under the **MIT License**.
