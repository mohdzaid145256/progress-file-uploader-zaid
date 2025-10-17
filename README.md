# ☁️ Progress File Uploader – Multi-Cloud Deployment (Render + AWS)

**🌐 Live Demo (Render):**
👉 [https://progress-file-uploader-zaid.onrender.com](https://progress-file-uploader-zaid.onrender.com)

**☁️ Live Demo (AWS S3 Hosting):**
👉 [https://progress-file-uploader-zaid.s3.us-east-2.amazonaws.com](https://progress-file-uploader-zaid.s3.us-east-2.amazonaws.com)

**💻 GitHub Repository:**
🔗 [https://github.com/mohdzaid145256/progress-file-uploader-zaid](https://github.com/mohdzaid145256/progress-file-uploader-zaid)

---

## 🚀 Objective

Built a **secure, full-stack file upload web application** integrated with **AWS S3 Cloud Storage** and deployed publicly on **Render**.
This project demonstrates hands-on skills in **Flask backend development**, **AWS integration**, **secure file handling**, and **responsive UI design**.

---

## 🧩 Key Features

* ✅ **AWS S3 integration** for secure and scalable file storage
* ✅ **Multiple format support** – `.pdf`, `.png`, `.jpg`, `.txt`, `.csv`
* ✅ **File-size limit (10 MB)** for efficient resource use
* ✅ **File type validation** for security
* ✅ **Metadata logging** (filename, size, type, timestamp, URL)
* ✅ **Modern UI** with animated progress bar
* ✅ **Public file link** generation after upload
* ✅ **Error handling with JSON responses**
* ✅ **Deployed on both AWS & Render**

---

## 🧱 Tech Stack

**Frontend:** HTML, CSS, Bootstrap, JavaScript
**Backend:** Flask (Python)
**Cloud:** AWS S3 (Region: `us-east-2`, Ohio)
**Deployment:** Render (App Hosting) + AWS (File Storage)

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mohdzaid145256/progress-file-uploader-zaid.git
cd progress-file-uploader-zaid
```

### 2️⃣ Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure AWS Credentials

Set your credentials as environment variables:

```bash
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_REGION="us-east-2"
export AWS_BUCKET_NAME="progress-file-uploader-zaid"
```

### 5️⃣ Run Application

```bash
python -m flask --app app run --debug
```

Then visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Project Structure

```
progress-file-uploader-zaid/
│
├── app.py              # Flask backend with AWS S3 logic
├── templates/
│   └── index.html      # Frontend upload UI with progress animation
├── upload_log.txt      # Metadata log (auto-generated)
├── requirements.txt    # Dependencies list
└── README.md           # Documentation
```

---

## 🏆 Highlights & Learnings

* 🌍 Deployed the same backend across **Render and AWS**
* 🔒 Applied **IAM-based access control** and S3 permissions
* 🧾 Added **metadata tracking** for every uploaded file
* 🧠 Strengthened understanding of **Flask–AWS integration**
* 🧰 Followed **best practices** for secure cloud development

---

## 👨‍💻 Developer

**Mohd Zaid**
📍 Sikar, Rajasthan, India
📧 [mohdzaid4919@gmail.com](mailto:mohdzaid4919@gmail.com)
🔗 [GitHub](https://github.com/mohdzaid145256) | [LinkedIn](https://www.linkedin.com/in/mohdzaid123)

---

> *Part of the Progress Software Internship Challenge – Task 1 (Cloud Integration with AWS & Render)*

