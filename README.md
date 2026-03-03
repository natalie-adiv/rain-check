# 🌦️ RainCheck

RainCheck is a Python-based automation tool designed to monitor real-time weather data and provide proactive notifications for rain alerts. By integrating with external Weather APIs, the system helps users stay prepared for changing weather conditions.

---

## 🚀 Key Features

* **Real-time Monitoring**: Fetches live weather updates from external providers.
* **Automated Logic**: Evaluates weather conditions and triggers notifications based on predefined rain thresholds.
* **API Integration**: Robust handling of JSON data from RESTful Weather APIs.
* **Secure Configuration**: Supports environment variables for sensitive API credentials.

## 🛠 Tech Stack

* **Language**: Python 3.x
* **Libraries**: `requests` (for API calls), `json` (for data parsing), `python-dotenv` (for security).
* **Concepts**: API Integration, Data Processing, Automation.



## 📋 Prerequisites

* Python 3.8+
* A valid API Key from a weather provider (e.g., OpenWeatherMap or WeatherAPI).

## ⚙️ Configuration

To keep your API keys secure and follow industry best practices for a **Senior Software Engineer**:

1. **Create a `.env` file** in the project root:
   ```bash
   touch .env

2. **Add your API credentials** to the `.env` file:
   ```env
   WEATHER_API_KEY=your_api_key_here
   CITY_NAME=your_city_Name

3. **Note**: Ensure your `.gitignore` includes `.env` to avoid leaking credentials to GitHub.



## 💻 Setup & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/natalie-adiv/rain-check.git](https://github.com/natalie-adiv/rain-check.git)
   cd rain-check   

2. **Install dependencies**:
   ```bash
   pip install requests python-dotenv

3. **Run the application**:
   ```bash
   python main.py

## 🧠 Notification Logic

The core logic of RainCheck follows a simple yet effective flow:

1. **Fetch**: Request current and forecast data for the specified location.
2. **Parse**: Extract precipitation probability and weather condition codes.
3. **Analyze**: If rain is detected within the next 12 hours (probability > 50%), a notification is prepared.
4. **Trigger**: Send the alert via the configured notification channel (e.g., Terminal, Email, or Desktop Notification).

## 🎓 Academic Connection & Future Work

As part of my **Master of Science in Machine Learning & Big Data**, I plan to expand RainCheck with:

* **Predictive Models**: Using historical weather patterns to forecast localized rain events with higher accuracy.
* **Data Pipelines**: Implementing advanced data collection for long-term weather trend analysis.


