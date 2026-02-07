import os
import base64
import json
from flask import Flask, request, render_template, jsonify
from groq import Groq

# Initialize Flask App
app = Flask(__name__)

# Initialize Groq client
# This will use the API key set in Render environment variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    print("⚠️  WARNING: GROQ_API_KEY is missing! Set it in Render dashboard.")

client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
            
        file = request.files['file']
        
        # Read and encode image
        image_data = file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        
        # Create vision API request
        MODEL = "llama-3.2-90b-vision-preview"
        
        print(f"🤖 analyzing image with {MODEL}...")
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """You are an expert plant pathologist. Analyze this leaf image.

Identify the disease from these 8 categories ONLY:
1. Anthracnose
2. Bacterial spot
3. Curl
4. Healthy
5. Mealybug
6. Mite disease
7. Ringspot
8. Mosaic

Return valid JSON with this structure:
{
    "condition": "Disease Name",
    "confidence": "95%",
    "advice_en": { "about": "...", "cause": "...", "prevention": "...", "treatment": "..." },
    "advice_ta": { "about": "...", "cause": "...", "prevention": "...", "treatment": "..." },
    "advice_hi": { "about": "...", "cause": "...", "prevention": "...", "treatment": "..." }
}
Please ensure the JSON is valid and keys match exactly.
"""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            temperature=0.1,
            max_tokens=1000,
            response_format={"type": "json_object"} # Ensure JSON response
        )
        
        # Parse response
        content = response.choices[0].message.content
        print(f"✅ AI Response: {content[:100]}...")
        
        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            # Fallback if model returns markdown block
            clean_content = content.replace("```json", "").replace("```", "")
            result = json.loads(clean_content)
        
        return jsonify({
            "condition": result.get("condition", "Unknown"),
            "accuracy": result.get("confidence", "95%"),
            "advice_en": result.get("advice_en", {}),
            "advice_ta": result.get("advice_ta", {}),
            "advice_hi": result.get("advice_hi", {}),
            "heatmap": ""  # No heatmap available in vision-only mode
        })
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)}), 500

# Ensure temp directory exists
os.makedirs('static/temp', exist_ok=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
