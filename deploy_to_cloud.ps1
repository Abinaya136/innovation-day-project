# 🚀 Quick Deployment Script for Windows

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "🌿 LeafCare Deployment Helper" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: GitHub Repository
Write-Host "📋 Step 1: Create GitHub Repository" -ForegroundColor Yellow
Write-Host "-----------------------------------"
Write-Host "1. Go to: https://github.com/new"
Write-Host "2. Repository name: leafcare-disease-detector"
Write-Host "3. Make it PUBLIC (required for free Render)"
Write-Host "4. Don't initialize with README"
Write-Host "5. Click 'Create repository'"
Write-Host ""

$created_repo = Read-Host "Have you created the GitHub repository? (y/n)"

if ($created_repo -ne "y") {
    Write-Host "❌ Please create the repository first, then run this script again." -ForegroundColor Red
    exit 1
}

# Get GitHub username
Write-Host ""
$github_username = Read-Host "Enter your GitHub username"

if ([string]::IsNullOrWhiteSpace($github_username)) {
    Write-Host "❌ GitHub username is required!" -ForegroundColor Red
    exit 1
}

# Step 2: Push to GitHub
Write-Host ""
Write-Host "📤 Step 2: Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "-----------------------------------"

$repo_url = "https://github.com/$github_username/leafcare-disease-detector.git"

# Remove existing remote if any
git remote remove origin 2>$null

# Add new remote
git remote add origin $repo_url

# Push to GitHub
Write-Host "Pushing to: $repo_url" -ForegroundColor Cyan
git branch -M main
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to push. Please check your credentials and try again." -ForegroundColor Red
    Write-Host "   You may need to authenticate via GitHub CLI or Personal Access Token" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host "✅ GitHub Setup Complete!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🎯 Next Steps:" -ForegroundColor Yellow
Write-Host "1. Go to: https://render.com"
Write-Host "2. Sign up/Login (it's free!)"
Write-Host "3. Click 'New +' → 'Web Service'"
Write-Host "4. Connect your GitHub account"
Write-Host "5. Select: $github_username/leafcare-disease-detector"
Write-Host "6. Use these settings:"
Write-Host "   - Name: leafcare-app"
Write-Host "   - Build Command: pip install -r requirements.txt"
Write-Host "   - Start Command: gunicorn app:app"
Write-Host "   - Instance Type: Free"
Write-Host "7. Click 'Create Web Service'"
Write-Host ""
Write-Host "⏱️  Deployment takes 5-10 minutes" -ForegroundColor Cyan
Write-Host "📱 You'll get a URL like: https://leafcare-app.onrender.com" -ForegroundColor Green
Write-Host ""
Write-Host "🎉 Your app will work from anywhere, even when your laptop is off!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Cyan
