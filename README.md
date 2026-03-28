# Intership-Cyber

🔐 ML-Based URL Phishing Detector

A machine learning-based web application that detects phishing URLs in real time by analyzing their structural patterns and characteristics. This project uses dynamic model training with Scikit-learn and provides an interactive web interface using Flask.

🚀 Features:

🔍 Real-time URL phishing detection
🤖 Machine Learning models trained dynamically (no pre-saved .pkl files)
🌐 Flask-based user-friendly web interface
📊 URL feature extraction and pattern analysis
⚡ Fast and lightweight prediction system

🧠 How It Works

1.Input URL
User enters a URL through the web interface
2.Feature Extraction
The system analyzes the URL and extracts features such as:
URL length
Presence of special characters (@, -, //)
Number of subdomains
Use of HTTPS
Suspicious keywords
3.Model Training
Machine Learning models are trained dynamically using Scikit-learn
No pre-trained or serialized model files are used
4.Prediction
The model classifies the URL as:
✅ Legitimate
❌ Phishing
5.Output Display.
Result is shown instantly on the web interface.

🛠️ Tech Stack

Programming Language: Python
Machine Learning: Scikit-learn
Web Framework: Flask
Frontend: HTML, CSS
Libraries Used:
pandas
numpy
sklearn
flask

📊 Dataset:

The dataset contains labeled URLs categorized as phishing or legitimate
Features are extracted from URL structures rather than webpage content
📈 Future Improvements
🔗 Integration with real-time threat intelligence APIs
🧠 Use of advanced models (Random Forest, XGBoost, Deep Learning)
🌍 Deployment on cloud platforms (AWS / Heroku)
📱 Mobile-friendly UI enhancements
🔒 Browser extension for live phishing detection

🎯 Learning Outcomes
Understanding of phishing detection techniques
Hands-on experience with machine learning workflows
Practical implementation of Flask web applications.
Feature engineering for cybersecurity problems.
