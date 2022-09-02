import os

#AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_ACCESS_KEY_ID = "DO00XFTANNYJTZY4HRJH"
#AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = "a4vDI4+3Im3PMjS1yWNTBbb7f6szQQ0wYHTD0uiQWoU"
AWS_STORAGE_BUCKET_NAME = "staticf"
AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
     "ACL": "public-read"
}
AWS_LOCATION = "https://staticf.fra1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "staticf.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = 'staticf.cdn.backends.StaticRootS3BotoStorage'
