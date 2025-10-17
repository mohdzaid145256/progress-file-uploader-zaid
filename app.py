import os
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Use Render's temporary directory for uploads
UPLOAD_FOLDER = os.path.join("/tmp", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if "file" not in request.files:
                return "No file part", 400

            file = request.files["file"]
            if file.filename == "":
                return "No selected file", 400

            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)

            file_url = url_for("uploaded_file", filename=filename, _external=True)
            return render_template("index.html", file_url=file_url)

        except Exception as e:
            return f"Error: {str(e)}", 500

    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return app.send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
