import os
from flask import Flask, request, render_template
import boto3
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Environment variables for AWS
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Initialize the S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    key = f"uploads/{filename}"  # path inside S3 bucket

    try:
        # Upload the file to S3 (make it public)
        s3.upload_fileobj(file, BUCKET_NAME, key, ExtraArgs={"ACL": "public-read"})
        file_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{key}"
        return render_template("index.html", url=file_url)
    except ClientError as e:
        return f"Upload failed: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
