# Touno Portfolio - Render Deployment Guide

## ✅ What's Ready for Deployment

Your portfolio has been converted from Flet (desktop app) to Flask (web app) with the following:

- **Flask Web App** (`app.py`) - Routes for all portfolio sections
- **HTML Templates** - Responsive design with sky-blue theme
- **Static Assets** - All images, certificates, videos served from `/assets`
- **Procfile** - Configuration for Render deployment
- **requirements.txt** - All Python dependencies listed

## 🚀 Deploy to Render (Free)

### Step 1: Push to GitHub

```bash
cd "C:\Users\Tauno\OneDrive\Desktop\Touno potfolio"
git add -A
git commit -m "Add Flask web app for deployment"
git push
```

### Step 2: Create Render Account

1. Go to https://render.com
2. Sign up with GitHub account
3. Connect your GitHub repository

### Step 3: Deploy Web Service

1. Click **New +** → **Web Service**
2. Select your GitHub repository
3. Fill in these settings:
   - **Name**: `touno-portfolio` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plans**: Select **Free** tier

4. Click **Create Web Service**

### Step 4: Monitor Deployment

Render will automatically:
- Install dependencies from `requirements.txt`
- Build and start your app
- Assign a public URL (e.g., `https://touno-portfolio.onrender.com`)

## ✅ What Works After Deployment

- ✅ All navigation links (HOME, ABOUT, TIMELINE, MATLAB, BLOG, GITHUB, CONTACT)
- ✅ Images load correctly from `/assets`
- ✅ Certificate PDFs are downloadable
- ✅ Video file playable from `/assets`
- ✅ GitHub commit screenshots display
- ✅ Sky-blue color scheme applied
- ✅ Responsive design (mobile, tablet, desktop)

## 📝 Keeping Local Copy

Your original code remains intact:
- **`main.py`** - Original Flet app (for local desktop use)
- **`app.py`** - New Flask app (for web deployment)
- **`assets/`** - Shared asset folder for both apps

## 🔄 Updates

To update your live portfolio:
1. Edit files locally (app.py, templates, etc.)
2. Push to GitHub: `git add -A && git commit -m "Update..." && git push`
3. Render automatically redeploys within 1-2 minutes

## 📊 Project Structure

```
Touno potfolio/
├── main.py                 # Original Flet app
├── app.py                  # Flask web app
├── requirements.txt        # Python dependencies
├── Procfile               # Render configuration
├── render.yaml            # Alternative Render config
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── timeline.html
│   ├── matlab.html
│   ├── blog.html
│   ├── github.html
│   └── contact.html
└── assets/               # Images, certificates, videos
    ├── background.jpg
    ├── profile.jpg
    ├── about.jpg
    ├── *.pdf
    ├── *.png
    └── portfolio video.mp4
```

## ❓ Troubleshooting

**App not loading?**
- Check Render deployment logs
- Ensure all templates are in `templates/` folder
- Verify assets folder has all files

**Images not showing?**
- Check URL format: `/assets/filename`
- Render preserves folder structure

**Port issues?**
- Render automatically assigns PORT via environment variable
- App configured to use `os.environ.get('PORT', 5000)`

## 🎯 Your Live Portfolio URL

After deployment, you'll get a URL like:
```
https://touno-portfolio.onrender.com
```

Share this link to showcase your portfolio online!
