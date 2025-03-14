📢 GigaChat Streamlit Bot

A simple chatbot application powered by GigaChat and built using Streamlit. This bot interacts with users, processes their prompts, and returns text or image responses from the GigaChat API.

🚀 Features

🔑 Secure authentication with API token retrieval

📝 Text-based AI responses

🖼️ Image response handling

🎨 Streamlit-based user interface

🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/gigachat-bot.git
cd gigachat-bot

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Environment Variables

Create a .streamlit/secrets.toml file and add your GigaChat API credentials:

[secrets]
CLIENT_ID = "your_client_id"
SECRET = "your_secret_key"

▶️ Run the Application

streamlit run main.py

📂 Project Structure

📦 gigachat-bot
├── 📜 main.py        # Streamlit UI and chatbot logic
├── 📜 gigachat_api.py # API request functions
├── 📜 utils.py        # Helper functions
├── 📜 requirements.txt # Dependencies
├── 📜 README.md       # Project documentation

🛠️ Usage

Run the bot using Streamlit.

Enter a message in the chat input.

Wait for the AI response (text or image).

Enjoy the interactive experience!

📌 Future Improvements



💡 Contributing

Pull requests are welcome! Feel free to contribute to improve this chatbot.

📜 License

This project is licensed under the MIT License.
