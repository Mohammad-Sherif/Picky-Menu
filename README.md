# Picky Menu App & CMS

Welcome to the **Picky Menu App**, a fully bilingual (English/Arabic), mobile-optimized, serverless static website with a built-in Content Management System (CMS).

## Features
- 🚀 **Lightning Fast**: Built with pure HTML/CSS/JS, no databases or slow server calls required for the frontend.
- 📱 **Mobile First**: Designed to look like a premium native mobile application.
- 🌍 **Bilingual**: Instantly switch between English and Arabic with full RTL layout support.
- 🛠 **Built-in CMS**: A completely secure, serverless Admin Dashboard (`admin.html`) that allows IT admins to manage categories and products via the GitHub API.

---

## 1. How to Host on GitHub Pages (Free)
Since this app doesn't require a backend server, you can host it 100% for free using GitHub Pages.

1. Create a new repository on GitHub (e.g., `picky-menu`).
2. Upload all the files from this folder to the repository.
3. On your GitHub repository page, go to **Settings** > **Pages**.
4. Under "Build and deployment", select **Deploy from a branch**.
5. Select the `master` (or `main`) branch and click **Save**.
6. Within a minute or two, your site will be live at `https://[your-username].github.io/picky-menu`.

---

## 2. How to Use the Admin Dashboard (CMS)

To securely manage the menu without a database, the Admin Dashboard uses the GitHub API to update your `data.js` file directly.

### Step 1: Generate a GitHub Token (Secret Key)
Only someone with a secret token can edit your menu.
1. Log into your GitHub account.
2. Go to **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**.
3. Click **Generate new token (classic)**.
4. Give it a name (e.g., "Picky CMS").
5. Under **Select scopes**, check the box for **`repo`** (Full control of private repositories).
6. Click **Generate token**.
7. **Copy the token and save it somewhere safe!** (It starts with `ghp_...`). You won't be able to see it again.

### Step 2: Login to the Dashboard
1. Go to your live website and add `/admin.html` to the URL (e.g., `https://[your-username].github.io/picky-menu/admin.html`).
2. Enter your GitHub Token.
3. Enter your GitHub Username (Repository Owner).
4. Enter your Repository Name (e.g., `picky-menu`).
5. Click **Login & Load Menu**.

### Step 3: Manage Categories and Products
Once logged in, you can:
- **Add Categories**: Click "+ Add Category". You must have at least one category before adding products.
- **Add Products**: Click "+ Add Product". You can specify names and descriptions in both English and Arabic.
- **Images**: Since this is a static site without a database, you must provide a direct URL to an image. You can upload your image to an image host (like Imgur) or directly to your GitHub repository and paste the link here.
- **Edit/Delete**: Use the buttons next to any category or item.

### Step 4: Save & Publish
When you are done making changes, scroll to the bottom and click **Save & Publish All Changes**.
This securely pushes the changes directly to your GitHub repository. Your live website will automatically update within a minute!
