<p align="center">
  <img src="assets/RainCheck_Logo.png" width="200" alt="RainCheck Logo">
</p>

# 🌦️ RainCheck

RainCheck is a Python-based automation tool designed to monitor real-time weather data and provide proactive notifications for rain alerts. By integrating with external Weather APIs, the system helps users stay prepared for changing weather conditions.

---

## 🚀 Key Features

* **Real-time Monitoring**: Fetches live weather updates from external providers.
* **Automated Logic**: Evaluates weather conditions and triggers notifications based on predefined rain thresholds.
* **API Integration**: Robust handling of JSON data from RESTful Weather APIs.
* **Secure Configuration**: Supports environment variables for sensitive API credentials.
* **Resilient Data Fetching**: Implemented robust error handling for API rate limits and network connectivity issues.

## 🛠 Tech Stack

* **Language**: Python 3.x
* **Libraries**: `requests` (for API calls), `json` (for data parsing), `python-dotenv` (for security).
* **Concepts**: API Integration, Data Processing, Automation.


## 🏗️ Architecture

The project follows a **modular Object-Oriented Design**, emphasizing clean separation of concerns:
* **API Layer**: Handles data fetching and interaction with external weather providers.
* **Analysis Layer**: Encapsulates the business logic for precipitation evaluation and threshold monitoring.
* **Notification Dispatchers**: Manages the delivery of alerts across different channels.

This architecture ensures the system is easily extensible—for example, adding new weather providers or notification channels (like Slack or SMS) without modifying the core logic.

## 📋 Prerequisites

* Python 3.8+
* A valid API Key from a weather provider (e.g., OpenWeatherMap or WeatherAPI).

## ⚙️ Configuration

To keep your API keys secure and follow industry best practices for a **Senior Software Engineer**:

1. **Create a `.env` file** in the project root:
   ```bash
   touch .env
   ```

2. **Add your API credentials** to the `.env` file:
   ```env
   WEATHER_API_KEY=your_api_key_here
   CITY_NAME=your_city_Name
   ```

3. **Note**: Ensure your `.gitignore` includes `.env` to avoid leaking credentials to GitHub.



## 💻 Setup & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/natalie-adiv/rain-check.git](https://github.com/natalie-adiv/rain-check.git)
   cd rain-check   
   ```

2. **Install dependencies**:
   ```bash
   pip install requests python-dotenv
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 🧠 Notification Logic

The core logic of RainCheck follows a simple yet effective flow:

1. **Fetch**: Request current and forecast data for the specified location.
2. **Parse**: Extract precipitation probability and weather condition codes.
3. **Analyze**: If rain is detected within the next 12 hours (probability > 50%), a notification is prepared.
4. **Trigger**: Send the alert via the configured notification channel (e.g., Terminal, Email, or Desktop Notification).

## 🎓 Academic Connection & Future Work

As I progress through my MSc in Machine Learning & Big Data (currently in my second semester), I am specifically looking to implement Time-Series Analysis to identify micro-climatic patterns based on the historical data collected by this tool.

Future enhancements include:

* **Predictive Analytics**: Using historical weather patterns and ML models to forecast local rainfall.
* **Multi-channel Alerts**: Integration with WhatsApp, Slack, or SMS.
* **Data Visualization**: Developing dashboards to visualize historical trends and model predictions.

