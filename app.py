import os
import time
from flask import Flask, request, render_template, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# === CONFIGURATION ===
UPLOAD_FOLDER = os.path.join("/tmp", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Max file size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB limit

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt'}


# === HELPER FUNCTIONS ===
def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# === ROUTES ===
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Validate file in request
            if "file" not in request.files:
                return "No file part in request", 400

            file = request.files["file"]

            # Validate file name
            if file.filename == "":
                return "No selected file", 400

            # Validate file type
            if not allowed_file(file.filename):
                return "File type not allowed. Please upload PDF, PNG, JPG, or TXT files.", 400

            # Save securely
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)

            # === Metadata Logging ===
            metadata = {
                "filename": filename,
                "content_type": file.content_type,
                "size_bytes": os.path.getsize(save_path),
                "uploaded_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }

            # Print metadata in logs (for debugging + internal assessment)
            print(f"📊 File Metadata: {metadata}")

            # === Return file URL ===
            file_url = url_for("uploaded_file", filename=filename, _external=True)
            print(f"✅ File uploaded successfully: {file_url}")

            return {"success": True, "file_url": file_url}, 200

        except Exception as e:
            print(f"❌ Error while uploading: {e}")
            return f"Internal Server Error: {e}", 500

    # Default GET request (renders upload UI)
    return render_template("index.html")


@app.errorhandler(413)
def file_too_large(e):
    """Custom error for oversized files."""
    return "File too large. Maximum upload size is 10 MB.", 413


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    """Serve uploaded file."""
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    except Exception as e:
        print(f"❌ Error sending file: {e}")
        return f"Error retrieving file: {e}", 500


# === MAIN ENTRY ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
