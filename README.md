
# 📤 Progress File Uploader  
**Developed by Mohd Zaid | Progress Software Internship Task (Cloud Platform Usage)**  

---

## 🚀 Objective  
To build and deploy a **simple file uploader web application** that allows users to upload any file (e.g., image, PDF, or text) and returns a **publicly accessible URL**.  
The application demonstrates the use of **Python (Flask)**, **Bootstrap**, and **cloud deployment** using **Render (serverless hosting)**.  

---
🌐 Hosted App: https://progress-file-uploader-zaid.onrender.com
   💻 GitHub Repo: https://github.com/mohdzaid145256/progress-file-uploader-zaid


---

## ⚙️ Tech Stack  
- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Backend:** Python Flask  
- **Hosting Platform:** Render (Serverless Cloud Deployment)  
- **Storage:** Temporary storage in `/tmp/uploads` directory (cloud-hosted container storage)  

---

## 🧩 Features  
✅ Clean and responsive UI (Bootstrap)  
✅ Real-time progress bar during upload  
✅ Validations for file type and size  
✅ Generates public file URL after successful upload  
✅ Logs file metadata (filename, size, MIME type) to console  
✅ Deployed on a live cloud endpoint (Render)  

---

## 🏗️ Setup Steps (Local Development)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mohdzaid145256/progress-file-uploader-zaid.git
cd progress-file-uploader-zaid


🧠 Reflection
While building this project, I learned how to:
Integrate Flask with HTML for a full-stack app.
Implement AJAX file uploads with live progress tracking.
Add validation and metadata logging in backend workflows.
Deploy Flask apps on a cloud serverless platform (Render).
Challenges included managing temporary file storage in a stateless environment, which was solved using Flask’s dynamic directory creation (os.makedirs()).


🧰 Bonus Enhancements
File Size Limit: 10 MB max upload limit.
File Type Validation: Only PDF, JPG, PNG, and TXT allowed.
Metadata Logging: Logs file name, MIME type, size, and timestamp.
AI-Enhanced Design: Used AI for code optimization and UI polishing.
Clean UX: Success feedback and animated progress bar.


