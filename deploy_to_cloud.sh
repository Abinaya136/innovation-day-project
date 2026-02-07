#!/bin/bash
# 🚀 Quick Deployment Script for Render

echo "=================================="
echo "🌿 LeafCare Deployment Helper"
echo "=================================="
echo ""

# Check if GitHub repository URL is set
echo "📋 Step 1: Create GitHub Repository"
echo "-----------------------------------"
echo "1. Go to: https://github.com/new"
echo "2. Repository name: leafcare-disease-detector"
echo "3. Make it PUBLIC (required for free Render)"
echo "4. Don't initialize with README"
echo "5. Click 'Create repository'"
echo ""
read -p "Have you created the GitHub repository? (y/n): " created_repo

if [ "$created_repo" != "y" ]; then
    echo "❌ Please create the repository first, then run this script again."
    exit 1
fi

# Get GitHub username
echo ""
read -p "Enter your GitHub username: " github_username

if [ -z "$github_username" ]; then
    echo "❌ GitHub username is required!"
    exit 1
fi

# Add remote and push
echo ""
echo "📤 Step 2: Pushing to GitHub..."
echo "-----------------------------------"

REPO_URL="https://github.com/$github_username/leafcare-disease-detector.git"

# Remove existing remote if any
git remote remove origin 2>/dev/null

# Add new remote
git remote add origin $REPO_URL

# Push to GitHub
echo "Pushing to: $REPO_URL"
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ Successfully pushed to GitHub!"
else
    echo "❌ Failed to push. Please check your credentials and try again."
    echo "   You may need to authenticate via GitHub CLI or Personal Access Token"
    exit 1
fi

echo ""
echo "=================================="
echo "✅ GitHub Setup Complete!"
echo "=================================="
echo ""
echo "🎯 Next Steps:"
echo "1. Go to: https://render.com"
echo "2. Sign up/Login (it's free!)"
echo "3. Click 'New +' → 'Web Service'"
echo "4. Connect your GitHub account"
echo "5. Select: $github_username/leafcare-disease-detector"
echo "6. Use these settings:"
echo "   - Name: leafcare-app"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn app:app"
echo "   - Instance Type: Free"
echo "7. Click 'Create Web Service'"
echo ""
echo "⏱️  Deployment takes 5-10 minutes"
echo "📱 You'll get a URL like: https://leafcare-app.onrender.com"
echo ""
echo "🎉 Your app will work from anywhere, even when your laptop is off!"
echo "=================================="
