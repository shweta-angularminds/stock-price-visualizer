📈 Stock Analysis & AI News Summarizer App

A Streamlit web application that allows users to:

📊 Fetch stock data

📈 Visualize stock trends

📰 Summarize financial/news text using AI

Built using Python, Streamlit, and Transformers.

🚀 Tech Stack

Streamlit – Web App UI

yfinance – Fetch stock market data

pandas – Data handling

matplotlib – Data visualization

transformers – AI text summarization


📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/shweta-angularminds/stock-price-visualizer.git
cd stock-price-visualizer

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

If you don't have requirements.txt, create one with:

streamlit
yfinance
pandas
matplotlib
transformers


▶️ Run the App
streamlit run app.py

Then open the local URL shown in the terminal (usually):

http://localhost:8501

📊 Features

🔎 Search stock by ticker (e.g., AAPL, TSLA)

📅 Select date range

📈 Interactive stock price chart

🤖 AI-powered text summarization

📥 Real-time data using yfinance

🧠 How It Works

User enters stock ticker.

yfinance fetches stock data.

pandas processes the data.

matplotlib generates charts.

transformers model summarizes financial text.

streamlit displays everything in a clean UI.

📌 Example Tickers

AAPL

TSLA

MSFT

GOOGL

AMZN

🛠 Future Improvements

Add technical indicators (RSI, MACD)

Deploy on Streamlit Cloud

Add news API integration

Improve UI design

👨‍💻 Author

Your Name
GitHub: https://github.com/shweta-angularminds
