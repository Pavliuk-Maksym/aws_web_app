import os
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
)
from app.services import s3_service

s3_bp = Blueprint(
    name="s3",
    import_name=__name__,
    url_prefix="/s3",
    template_folder="../templates",
    static_folder="../static",
)


# S3 main page
@s3_bp.route("/", methods=["GET"])
def s3_index():
    return render_template("s3.html")


# Create folder
@s3_bp.route("/create-folder", methods=["POST"])
def create_folder():
    bucket = request.form.get("bucket_name")
    folder = request.form.get("folder_name")
    success, msg = s3_service.create_folder(bucket, folder)
    flash(msg, "success" if success else "error")
    return redirect(url_for("s3.s3_index"))


# Delete object (folder or file)
@s3_bp.route("/delete-object", methods=["POST"])
def delete_object():
    bucket = request.form.get("bucket_name")
    key = request.form.get("object_key")
    success, msg = s3_service.delete_object(bucket, key)
    flash(msg, "success" if success else "error")
    return redirect(url_for("s3.s3_index"))


# List files
@s3_bp.route("/list-objects", methods=["GET"])
def list_objects():
    bucket = request.args.get("bucket_name")
    success, result = s3_service.list_objects(bucket)
    if not success:
        flash(result, "error")
        return redirect(url_for("s3.s3_index"))
    return render_template("s3.html", objects=result)


# Upload file
@s3_bp.route("/upload-file", methods=["POST"])
def upload_file():
    bucket = request.form.get("bucket_name")
    folder = request.form.get("folder_path") or ""
    file = request.files["file"]
    success, msg = s3_service.upload_file(bucket, folder, file)
    flash(msg, "success" if success else "error")
    return redirect(url_for("s3.s3_index"))


# Download file
@s3_bp.route("/download-file", methods=["POST"])
def download_file():
    bucket = request.form.get("bucket_name")
    key = request.form.get("object_key")
    filename = os.path.basename(key)
    path = f"D:/Загрузки/{filename}"

    success, msg = s3_service.download_file(bucket, key, path)
    flash(msg, "success" if success else "error")
    return redirect(url_for("s3.s3_index"))
