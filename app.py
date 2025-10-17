import os
from flask import Flask, request, render_template, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = os.path.join("/tmp", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if "file" not in request.files:
                print("❌ No file part in request")
                return "No file part", 400

            file = request.files["file"]

            if file.filename == "":
                print("❌ Empty filename")
                return "No selected file", 400

            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)

            file_url = url_for("uploaded_file", filename=filename, _external=True)
            print(f"✅ File uploaded successfully: {file_url}")
            return {"success": True, "file_url": file_url}, 200

        except Exception as e:
            print(f"❌ Error while uploading: {e}")
            return f"Internal Server Error: {e}", 500

    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    except Exception as e:
        print(f"❌ Error sending file: {e}")
        return f"Error retrieving file: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
