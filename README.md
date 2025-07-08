# Emotion Detection Web Application

A Flask-based web application that analyzes emotions in text using Watson NLP API with fallback simulation capabilities.

## 🎯 Features

- **Real-time Emotion Analysis**: Detect 5 core emotions (anger, disgust, fear, joy, sadness)
- **Watson NLP Integration**: Leverages IBM Watson's advanced NLP capabilities
- **Responsive Web Interface**: Clean, modern UI with real-time feedback
- **Robust Error Handling**: Comprehensive error management and fallback mechanisms
- **Unit Testing**: Full test coverage with automated testing suite
- **Code Quality**: Pylint compliant code with 10/10 rating

## 🛠️ Technology Stack

- **Backend**: Python 3.7+, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: IBM Watson NLP
- **Testing**: unittest
- **Code Quality**: Pylint

## 🏗️ Project Structure

```
emotion-detection-webapp/
├── EmotionDetection/           # Core emotion detection package
│   ├── __init__.py            # Package initialization
│   └── emotion_detection.py   # Main emotion detection logic
├── templates/                  # HTML templates
│   └── index.html             # Main web interface
├── static/                     # Static assets
│   └── style.css              # Application styles
├── server.py                   # Flask web server
├── test_emotion_detection.py   # Unit tests
├── requirements.txt            # Python dependencies
├── setup.py                   # Package setup configuration
└── README.md                  # Project documentation
```


## 🐛 Known Issues

- Watson NLP API may have rate limiting
- Fallback simulation provides basic keyword-based detection

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- IBM Watson for providing the NLP API
- Flask community for the excellent documentation
- All contributors who helped improve this project

⭐ **Star this repository if you found it helpful!**
