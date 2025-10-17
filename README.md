# ☁️ Progress File Uploader – AWS Cloud Integration

**Live Demo:**
👉 [https://progress-file-uploader-zaid.onrender.com](https://progress-file-uploader-zaid.onrender.com)

**GitHub Repository:**
🔗 [https://github.com/mohdzaid145256/progress-file-uploader-zaid](https://github.com/mohdzaid145256/progress-file-uploader-zaid)

---

## 🚀 Objective

Developed a **secure, full-stack web application** that enables users to upload files to **AWS S3 Cloud Storage**.
This task demonstrates cloud integration, metadata handling, and security validation while maintaining a professional, production-ready UI.

---

## 🧩 Features

* ✅ Direct upload to AWS S3 (secure, server-side handling)
* ✅ Supports common formats: `.pdf`, `.jpg`, `.png`, `.txt`, `.csv`
* ✅ 10 MB file-size limit with validation
* ✅ Auto-timestamped filenames for version control
* ✅ Real-time metadata logging (filename, size, type, timestamp)
* ✅ Clean Flask backend + responsive frontend
* ✅ Error-handled responses for a smooth user experience
* ✅ Deployed demo via **Render**

---

## 🧱 Tech Stack

**Frontend:** HTML + CSS + JS
**Backend:** Python (Flask)
**Cloud:** AWS S3 (Region – `us-east-2`, Ohio)
**Deployment:** Render (Free Cloud Hosting)
**AI Assistance:** ChatGPT (GPT-5) for code optimization and UI improvement

---

## ⚙️ Setup Steps

### 1. Clone the Repo

```bash
git clone https://github.com/mohdzaid145256/progress-file-uploader-zaid.git
cd progress-file-uploader-zaid
```

### 2. Create Virtual Environment & Activate

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS Credentials

Either export them as environment variables:

```bash
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
```

Or add them directly in `app.py` (for testing only).

### 5. Run the Application

```bash
python -m flask --app app run --debug
```

Visit 👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 File Structure

```
progress-file-uploader-zaid/
│
├── app.py               # Flask backend with S3 upload logic
├── templates/
│   └── index.html       # Frontend UI for upload
├── upload_log.txt       # Metadata logs (auto-created)
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

---

## 🧠 AI Usage & Automation

AI tools were leveraged responsibly to:

* Refactor and comment Python code for readability
* Generate user-friendly UI and polished layout
* Add metadata logging, file validation, and secure upload flow
* Optimize error messages and HTTP response formatting

---

## 📊 Reflection

This project deepened my understanding of **AWS S3 integration**, secure file handling, and deploying Flask apps on cloud platforms.
I learned how to manage **access policies**, environment variables, and cross-origin communication between client and server.
Configuring S3 permissions and debugging upload errors were valuable real-world challenges that enhanced my practical skills.

---

## 🏆 Bonus Highlights

* 🔒 Secure uploads with AWS IAM policies
* 🧾 Metadata logging for audit & analytics
* 📈 Validations for file type and size
* 🌍 Public link generation for each uploaded file
* 🧠 AI-powered refactoring and README drafting

---

## 👨‍💻 Developed By

**Mohd Zaid**
📧 [mohdzaid4919@gmail.com](mailto:mohdzaid4919@gmail.com)
🔗 [GitHub](https://github.com/mohdzaid145256) | [LinkedIn](https://www.linkedin.com/in/mohdzaid123)

---

> *Part of the Progress Software Internship Challenge – Task 1 (AWS Cloud Integration)*


