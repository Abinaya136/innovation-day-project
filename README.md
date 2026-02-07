# 🌿 LeafCare - AI-Powered Leaf Disease Detection System

A farmer-focused web application for detecting and diagnosing leaf diseases using AI, with multi-language support (English, Tamil, Hindi) and SMS reminder capabilities.

## ✨ Features

- 🔍 **AI Disease Detection** - Identifies 8 types of leaf diseases with high accuracy
- 🗣️ **Voice Input/Output** - Supports voice commands and text-to-speech in multiple languages
- 🌐 **Multi-Language Support** - English, Tamil, and Hindi
- 📱 **SMS Reminders** - Sends treatment reminders to farmers
- 🎯 **Grad-CAM Visualization** - Shows which part of the leaf triggered the diagnosis
- 💊 **Organic Treatment Advice** - Provides eco-friendly treatment recommendations

## 🚀 Live Demo

**Deployed URL**: [Coming soon after deployment]

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **ML Framework**: PyTorch, timm
- **AI Model**: ConvNeXt-Tiny
- **LLM**: Groq API for advice generation
- **Deployment**: Render (cloud hosting)

## 📋 Diseases Detected

1. Anthracnose
2. Bacterial Spot
3. Curl
4. Healthy
5. Mealybug
6. Mite Disease
7. Ringspot
8. Mosaic

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Access at: `http://localhost:5000`

## 🌐 Cloud Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

**Quick start:**
```bash
# For Windows
.\deploy_to_cloud.ps1

# For Linux/Mac
bash deploy_to_cloud.sh
```

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── llm_advisor.py         # AI advisor for treatment recommendations
├── sms_service.py         # SMS functionality
├── model_engine.py        # Disease detection model wrapper
├── models/                # AI model files
│   └── best_convnext_tiny.zip
├── static/                # CSS, JS, images
├── templates/             # HTML templates
│   └── index.html
├── requirements.txt       # Python dependencies
├── Procfile              # For deployment
└── render.yaml           # Render configuration

```

## 🎯 Usage

1. **Upload Image**: Click or drag-and-drop a leaf image
2. **Get Diagnosis**: AI analyzes and shows the disease
3. **View Results**: See confidence score, heatmap, and detailed advice
4. **Multi-Language**: Switch between English, Tamil, Hindi
5. **Voice Support**: Use microphone for voice input
6. **SMS Reminder**: Set treatment reminders via SMS

## 🔐 Environment Variables

For deployment, set these in your hosting platform:

- `GROQ_API_KEY` - Your Groq API key (for LLM)
- Other API keys as needed

## 📄 License

This project is for educational and innovation purposes.

## 👥 Contributors

- Abinaya - Lead Developer

## 🙏 Acknowledgments

- Built for Innovation Day Project
- Uses state-of-the-art AI models for disease detection
- Designed with farmers in mind for ease of use

---

**Status**: ✅ Ready for Deployment
