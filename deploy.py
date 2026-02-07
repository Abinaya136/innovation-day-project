import os
import sys
from pyngrok import ngrok, conf
from app import app

# Disable pyngrok's default logger to keep output clean
conf.get_default().monitor_thread = False

def start_public_server():
    print("\n" + "="*60)
    print("🚀 STARTING PUBLIC DEPLOYMENT SERVER (NGROK)")
    print("="*60)

    # Set Auth Token provided by user
    ngrok.set_auth_token("39LrhQdhYJkM8qLJz34jy9LSmbJ_21ZLCYsVSsuWJB817NXJ8")

    # Ask for Auth Token (Optional but good for stability)
    token = os.environ.get("NGROK_AUTHTOKEN")
    if False: # Token is hardcoded above for demo
        pass
    if not token:
        print("\n⚠️  NOTE: You are running without an Ngrok Auth Token.")
        print("   The session will expire after 2 hours.")
        print("   For a permanent link, sign up at ngrok.com and set NGROK_AUTHTOKEN.\n")
    
    try:
        # Open a HTTP tunnel on the default port 5000
        public_url = ngrok.connect(5000).public_url
        print("✅ PUBLIC HTTPS URL GENERATED:\n")
        print(f"   👉  {public_url}  👈\n")
        with open("deployed_url.txt", "w") as f:
            f.write(public_url)
        print(f"   (Share this link. Microphone permissions will work here.)")
        print("="*60 + "\n")
    except Exception as e:
        print(f"\n❌ Error starting ngrok: {e}")
        if "ERR_NGROK_4018" in str(e) or "authentication failed" in str(e).lower():
            print("\n🚨 AUTHENTICATION REQUIRED:")
            print("   Ngrok now requires a free account for tunnels.")
            print("   1. Sign up at: https://dashboard.ngrok.com/signup")
            print("   2. Get your Authtoken from: https://dashboard.ngrok.com/get-started/your-authtoken")
            print("   3. Run: ngrok config add-authtoken <TOKEN>")
            print("   OR set NGROK_AUTHTOKEN environment variable.")
        else:
            print("   Ensure you don't have other ngrok instances running.")
        sys.exit(1)

    # Run the Flask app
    # Use threaded=True to handle multiple requests (like simultaneous camera/upload)
    app.run(port=5000, threaded=True)

if __name__ == '__main__':
    start_public_server()
