# 📦 Model File Upload Instructions

## Problem
Your AI model file (`best_convnext_tiny.zip`) is **98.75 MB**, which exceeds GitHub's recommended 50MB limit.

## Solution
Upload the model to Google Drive and download it during deployment.

---

## 🔧 Step-by-Step Instructions:

### **Option 1: Using Google Drive (Recommended)**

#### 1. Upload Model to Google Drive
1. Go to https://drive.google.com
2. Click **"New"** → **"File upload"**
3. Upload: `models/best_convnext_tiny.zip`

#### 2. Get Shareable Link
1. Right-click the uploaded file
2. Click **"Share"**
3. Change to **"Anyone with the link"** can view
4. Click **"Copy link"**

You'll get something like:
```
https://drive.google.com/file/d/1ABCDEFGHIJKLMNOPqrstuvwxyz/view?usp=sharing
```

#### 3. Convert to Direct Download Link
Change the link format from:
```
https://drive.google.com/file/d/FILE_ID/view?usp=sharing
```
To:
```
https://drive.google.com/uc?export=download&id=FILE_ID
```

**Example:**
- Original: `https://drive.google.com/file/d/1ABCDEFGHIJKLMNOPqrstuvwxyz/view?usp=sharing`
- Direct: `https://drive.google.com/uc?export=download&id=1ABCDEFGHIJKLMNOPqrstuvwxyz`

#### 4. Set in Render Environment
1. Go to Render dashboard
2. Select your service
3. Go to **"Environment"** tab
4. Add new environment variable:
   - **Key**: `MODEL_DOWNLOAD_URL`
   - **Value**: Your direct download link

---

### **Option 2: Using Dropbox**

#### 1. Upload to Dropbox
1. Go to https://www.dropbox.com
2. Upload `models/best_convnext_tiny.zip`

#### 2. Get Shareable Link
1. Click **"Share"**
2. Click **"Create link"**
3. Copy the link

#### 3. Convert to Direct Download
Change the end of the URL from `?dl=0` to `?dl=1`

**Example:**
- Shared: `https://www.dropbox.com/s/abc123/model.zip?dl=0`
- Direct: `https://www.dropbox.com/s/abc123/model.zip?dl=1`

#### 4. Set in Render Environment
Same as Google Drive option above.

---

### **Option 3: GitHub LFS (Requires Git LFS)**

If you prefer to keep the model in GitHub:

```bash
# Install Git LFS
git lfs install

# Track the model file
git lfs track "models/*.zip"

# Add and commit
git add .gitattributes models/best_convnext_tiny.zip
git commit -m "Add model with LFS"
git push
```

**Note**: GitHub LFS has a 1GB free storage limit.

---

## 🎯 For Local Development (Your Laptop)

Since the model file already exists locally at:
```
c:\Users\abina\Downloads\innovation day projectttt - Copy\models\best_convnext_tiny.zip
```

The app will work fine on your laptop without downloading!

---

## ✅ Quick Summary

1. **Upload** model to Google Drive
2. **Get** direct download link
3. **Add** `MODEL_DOWNLOAD_URL` to Render environment variables
4. **Deploy** - Render will download the model automatically!

---

## 🆘 Need Help?

If you're having trouble, you can also:
- Use a smaller model (if available)
- Host the model on AWS S3 (free tier available)
- Use Hugging Face model hub

---

**Next**: Once you upload the model and get the link, we can proceed with deployment! 🚀
