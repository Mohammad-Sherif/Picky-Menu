# Picky Menu App & CMS

Welcome to the **Picky Menu App**, a fully bilingual (English/Arabic), mobile-optimized, serverless static website with a built-in Content Management System (CMS).

---

### Part 1: How to Host the Website and Get Your Link
The website is currently a collection of files. To host it online for free, follow these steps:
1. Go to your repository link on GitHub.
2. In the top right corner, click on **Settings**.
3. From the left sidebar, scroll down and select **Pages**.
4. In the middle of the page under `Build and deployment`, you will find a section called `Branch`. 
5. Open the dropdown menu that says `None` and select `main`, then click **Save**.
6. Wait exactly two or three minutes and refresh the page. You will see a message at the top saying your site is live, along with the link! 

*(The link will look like this: `https://[your-username].github.io/[your-repo-name]/`)*

---

### Part 2: How the IT Admin Can Access the Admin Panel
The admin panel is hidden and not meant for customers, so accessing it requires a specific method that does not depend on a specific account:
1. After getting the website link from the previous step, add `admin.html` to the end of it. 
*(The link will look like this: `https://[your-username].github.io/[your-repo-name]/admin.html`)*

2. When the admin panel opens, it will ask for 3 details to verify ownership:
   - **Repository Owner (Username):** Enter the GitHub account name where the project is hosted.
   - **Repository Name:** Enter the name of the repository.
   - **GitHub Token (Secret Key):** This is a secret password generated from your GitHub account. The steps to generate it are explained below.

---

### Part 3: How to Get the Secret Key (GitHub Token)
This step is done by the IT admin only once to get the password that will control the menu (whether on this account or any other account):

1. While logged into your GitHub account, click on your profile picture in the top right and select **Settings**.
2. Scroll all the way down the left sidebar and select **Developer settings**.
3. From the left sidebar, select **Personal access tokens** and then choose **Tokens (classic)**.
4. Click on the **Generate new token (classic)** button on the top right.
5. In the *Note* field, write any name like `Picky Admin`.
6. In the *Expiration* field, choose `No expiration` so the password never expires and works indefinitely.
7. Scroll down to the checkboxes and **check only the first box labeled `repo`** (this gives file modification permissions).
8. Scroll to the very bottom and click **Generate token**.
9. A long code starting with `ghp_...` will appear. **You must copy this code and save it in a very secure place** because it will never be shown again! This is the Secret Key you will use to log into the admin panel.

---

### Part 4: How to Use the Admin Panel
After opening the link and logging in with the details above:

- You will see the entire menu. You can click **Add Category** to add a new section.
- You can click **Add Product** to add a new item.
- **Editing Prices and Ingredients:** Next to any product, click the **Edit** button to open a screen where you can modify it (Name in EN/AR, Description, Price).
- **Images:** To add an image for a new product, simply upload the image to GitHub or any other hosting site, and paste its link (URL) into the "Image URL" field.
- **Saving Changes:** Once you are done with all modifications (adding or deleting), scroll to the bottom and click **Save & Publish All Changes**. Within a minute, these changes will reflect on the live customer menu.
