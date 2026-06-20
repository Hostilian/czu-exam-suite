# 🚀 GitHub Pages Deployment Guide
## OS & Networks Exam Blitz — Access on Your Phone

---

## Step 1: Create a GitHub Account
Go to https://github.com and sign up (free).

---

## Step 2: Create a New Repository

1. Click the **+** icon → **New repository**
2. Name it: `os-exam-blitz`
3. Set to **Public** ✓
4. Check **"Add a README file"** ✓
5. Click **Create repository**

---

## Step 3: Upload Your Files

In your new repository, click **"Add file"** → **"Upload files"**

Upload these files from `D:\CZUU\OS_EXAM_SUITE\`:
- `EXAM_BLITZ_2HR.html` ← **rename this to `index.html` before uploading!**

That's all you need — the file is completely self-contained!

---

## Step 4: Enable GitHub Pages

1. Go to repository **Settings** (top tabs)
2. Click **Pages** in the left sidebar
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 2-3 minutes

---

## Step 5: Access on Your Phone

Your site will be live at:
```
https://YOUR_USERNAME.github.io/os-exam-blitz/
```

Bookmark this on your phone! Works offline after first load.

---

## 🎧 Audio TTS on Phone

The audio memorization section uses your phone's built-in Text-to-Speech:
- **iOS (Safari):** Works natively ✓
- **Android (Chrome):** Works natively ✓
- **Tap "🎧 Audio Memo"** → press **▶ Play All**
- Choose a speed (0.9× recommended for studying)
- Lock your screen — audio continues playing!

---

## Alternative: Quick Share Without GitHub

If you don't want to use GitHub, use these free options:

### Option A: Netlify Drop (Fastest!)
1. Go to https://app.netlify.com/drop
2. Drag & drop `EXAM_BLITZ_2HR.html` renamed to `index.html`
3. Get instant URL — share via QR code with your phone

### Option B: Share via QR Code
1. Open `EXAM_BLITZ_2HR.html` in Chrome on your PC
2. Right-click address bar → "Send to your devices" (if signed into Google)

### Option C: Local Network Access
1. Open PowerShell in the OS_EXAM_SUITE folder
2. Run: `python -m http.server 8080`
3. On your phone (same WiFi): go to `http://YOUR_PC_IP:8080/EXAM_BLITZ_2HR.html`

---

## 📱 Mobile Tips

- **Tap sections** using the big colored buttons on the home screen
- **Audio section** has a full playlist — tap any track to jump to it
- **Flashcards** — tap the card to flip, use the buttons below to rate
- **Simulators** work fully on mobile (scrollable)
- **Checklist** saves your progress locally in the browser

---

*Built for CZU Prague OS & Networks ETE2AE — Good luck! 🍀*
