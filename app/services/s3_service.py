import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource("s3")


def create_folder(bucket_name: str, folder_name: str) -> tuple[bool, str]:
    try:
        if not folder_name.endswith("/"):
            folder_name += "/"
        bucket = s3.Bucket(bucket_name)
        bucket.put_object(Key=folder_name)
        return True, f"Folder '{folder_name}' created in bucket '{bucket_name}'."
    except ClientError as e:
        return False, f"Failed to create folder: {e}"


def delete_object(bucket_name: str, object_key: str) -> tuple[bool, str]:
    try:
        obj = s3.Object(bucket_name, object_key)
        obj.delete()
        return True, f"Object '{object_key}' deleted from bucket '{bucket_name}'."
    except ClientError as e:
        return False, f"Failed to delete object: {e}"


def list_objects(bucket_name: str) -> tuple[bool, list | str]:
    try:
        bucket = s3.Bucket(bucket_name)
        objects = [obj.key for obj in bucket.objects.all()]
        return True, objects
    except ClientError as e:
        return False, f"Failed to list objects: {e}"


def upload_file(bucket_name: str, folder_path: str, file_obj) -> tuple[bool, str]:
    try:
        key = (
            f"{folder_path.strip('/')}/{file_obj.filename}"
            if folder_path
            else file_obj.filename
        )
        bucket = s3.Bucket(bucket_name)
        bucket.upload_fileobj(file_obj, key)
        return (
            True,
            f"File '{file_obj.filename}' uploaded to '{key}' in bucket '{bucket_name}'.",
        )
    except ClientError as e:
        return False, f"Failed to upload file: {e}"


def download_file(
    bucket_name: str, object_key: str, download_path: str
) -> tuple[bool, str]:
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.download_file(object_key, download_path)
        return True, f"File '{object_key}' downloaded to {download_path}."
    except ClientError as e:
        return False, f"Failed to download file: {e}"


def generate_image_url(bucket_name: str, object_key: str) -> tuple[bool, str]:
    try:
        s3_client = boto3.client("s3")
        url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_key},
            ExpiresIn=300,
        )
        return True, url
    except ClientError as e:
        return False, f"Failed to generate image URL: {e}"
