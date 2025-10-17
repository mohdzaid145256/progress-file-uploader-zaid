
Task 1 - Cloud File Uploader for Progress Software Internship
# Progress File Uploader - Mohd Zaid

A simple Flask-based Cloud File Uploader built for the Progress Software Internship Assignment.

## 🌐 Live Demo
[Click here to view the hosted app on Render](https://progress-file-uploader-zaid.onrender.com)

## 🧠 Tech Stack
- Python (Flask)
- HTML, CSS (Frontend)
- Render Cloud (Deployment)
- AWS S3 Compatible Backend Logic (boto3-ready)

## ⚙️ Description
This application allows users to upload files and receive a publicly accessible URL.  
For demonstration purposes, the app stores files locally on Render Cloud’s temporary storage due to AWS verification delay.  
The backend logic remains fully compatible with AWS S3 using the `boto3` library.

## 🧩 How to Run Locally
```bash
git clone https://github.com/mohdzaid145256/progress-file-uploader-zaid.git
cd progress-file-uploader-zaid
pip install -r requirements.txt
python app.py
