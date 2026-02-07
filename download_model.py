#!/usr/bin/env python3
"""
Download the AI model from cloud storage before starting the app.
This script runs during Render deployment to fetch the large model file.
"""
import os
import urllib.request
from pathlib import Path

MODEL_DIR = Path("models")
MODEL_ZIP = MODEL_DIR / "best_convnext_tiny.zip"
MODEL_PATH = MODEL_DIR / "best_convnext_tiny.pth"

# IMPORTANT: Upload your model ZIP to Google Drive or Dropbox and get a direct download link
# Replace this URL with your actual model download URL
MODEL_URL = os.environ.get(
    "MODEL_DOWNLOAD_URL",
    ""  # Leave empty for now - will be set in Render environment
)

def download_model():
    """Download model from cloud storage if not present"""
    
    # Create models directory if it doesn't exist
    MODEL_DIR.mkdir(exist_ok=True)
    
    # Check if model already exists
    if MODEL_PATH.exists():
        print(f"✅ Model already exists at {MODEL_PATH}")
        return True
    
    if MODEL_ZIP.exists():
        print(f"✅ Model ZIP already exists at {MODEL_ZIP}")
        return True
    
    # If no URL provided, skip download (for local development)
    if not MODEL_URL:
        print("⚠️  WARNING: MODEL_DOWNLOAD_URL not set!")
        print("   Skipping model download. Make sure model exists locally.")
        return False
    
    # Download the model
    print(f"📥 Downloading model from cloud storage...")
    print(f"   URL: {MODEL_URL}")
    
    try:
        urllib.request.urlretrieve(MODEL_URL, MODEL_ZIP)
        file_size = MODEL_ZIP.stat().st_size / (1024 * 1024)  # MB
        print(f"✅ Model downloaded successfully ({file_size:.1f} MB)")
        return True
    except Exception as e:
        print(f"❌ Failed to download model: {e}")
        return False

if __name__ == "__main__":
    download_model()
