# 📤 Progress File Uploader – Mohd Zaid

A **Flask-based File Upload Web App** that enables users to upload files securely with **progress tracking**, **file validation**, and **AWS S3 integration**.
Developed as part of the **Progress Software Internship Task (Task 1)**, this project demonstrates a complete full-stack cloud deployment workflow.

---

## 🚀 Live Deployments

* **Render Deployment:**
  🔗 https://progress-file-uploader-zaid-1.onrender.com

* **AWS Elastic Beanstalk Deployment:**
  🔗 [http://progress-file-uploader-env.eba-t3pvp3pa.us-east-2.elasticbeanstalk.com](http://progress-file-uploader-env.eba-t3pvp3pa.us-east-2.elasticbeanstalk.com)

---

## 🧠 Project Overview

This project demonstrates:

* Flask-based **secure file uploads**
* Real-time **upload progress visualization**
* **AWS S3 integration** for scalable cloud storage
* **File type and size validation**
* **Metadata logging** (filename, size, type, URL)
* Deployment on both **Render** and **AWS Elastic Beanstalk**

---

## 🛠️ Tech Stack

| Category              | Technologies Used                     |
| --------------------- | ------------------------------------- |
| **Backend Framework** | Flask (Python)                        |
| **Cloud Storage**     | AWS S3                                |
| **Deployment**        | Render, AWS Elastic Beanstalk         |
| **Frontend**          | HTML, CSS (Bootstrap 5), JavaScript   |
| **Dependencies**      | Flask, boto3, gunicorn, python-dotenv |

---

## 📁 Folder Structure

```
progress-file-uploader-zaid/
│
├── app.py                 # Flask application
├── templates/
│   └── index.html         # Frontend HTML template
├── static/                # (optional) CSS/JS assets
├── requirements.txt       # Project dependencies
├── Procfile               # Process file for Render & AWS
├── .ebextensions/
│   └── python.config      # Elastic Beanstalk configuration
├── .env                   # AWS credentials and config
└── README.md              # Documentation
```

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mohdzaid145256/progress-file-uploader-zaid.git
cd progress-file-uploader-zaid
```

### 2️⃣ Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app locally

```bash
python app.py
```

Then visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## 🌩️ Deployment on Render

1. Push your project to **GitHub**.
2. Visit **[Render.com](https://render.com)** → Click **New Web Service**.
3. Connect your GitHub repo and select branch `main`.
4. Use the following settings:

   ```
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```
5. Click **Deploy** 🎉
   Render will automatically generate a live production link.

---

## ☁️ Deployment on AWS Elastic Beanstalk

1. **Create an S3 Bucket**

   * Go to **AWS Console → S3 → Create Bucket**
   * Enable **public access** (for testing purposes)
   * Note down the bucket name and region

2. **Create `.env` file**

   ```
   AWS_ACCESS_KEY=your-access-key
   AWS_SECRET_KEY=your-secret-key
   AWS_BUCKET_NAME=progress-file-uploader-zaid
   AWS_REGION=us-east-2
   ```

3. **Initialize Elastic Beanstalk**

   ```bash
   eb init -p python-3.12 progress-file-uploader-zaid --region us-east-2
   ```

4. **Create the environment**

   ```bash
   eb create progress-file-uploader-env
   ```

5. **Deploy**

   ```bash
   eb deploy
   ```

6. Once the environment status shows:

   ```
   Status: Ready
   Health: Green
   ```

   Visit the live link:
   🔗 [http://progress-file-uploader-env.eba-t3pvp3pa.us-east-2.elasticbeanstalk.com](http://progress-file-uploader-env.eba-t3pvp3pa.us-east-2.elasticbeanstalk.com)

---

## ✅ Bonus Features Implemented

| Feature               | Description                                      |
| --------------------- | ------------------------------------------------ |
| **File Size Limit**   | Restricts uploads larger than 5MB                |
| **Type Validation**   | Supports only PNG, JPG, PDF, DOCX, and TXT       |
| **Metadata Logging**  | Records filename, size, type, and cloud URL      |
| **S3 Integration**    | Files stored securely in AWS S3                  |
| **Responsive UI**     | Modern and clean Bootstrap-based design          |
| **Success Animation** | Displays animated checkmark on successful upload |

---

## 📊 Example Metadata Log Output

```json
{
  "filename": "resume.pdf",
  "size_bytes": 358400,
  "type": "application/pdf",
  "url": "https://progress-file-uploader-zaid.s3.us-east-2.amazonaws.com/resume.pdf"
}
```

---

## 🧩 Future Improvements

* Add **user authentication (login before upload)**
* Integrate **database logging** for upload history
* Add **file preview** and **delete** features
* Enable **AWS CloudWatch monitoring** for analytics

---

## 👨‍💻 Developer

**Mohd Zaid**
📍 Sikar, Rajasthan, India
📧 [mohdzaid4919@gmail.com](mailto:mohdzaid4919@gmail.com)
🔗 [GitHub Profile](https://github.com/mohdzaid145256)

---

### 🌟 *A production-ready, full-stack Flask project showcasing secure file handling, progress tracking, and multi-cloud deployment.*
