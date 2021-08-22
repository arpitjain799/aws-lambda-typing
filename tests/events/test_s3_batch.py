from aws_lambda_typing.events import S3BatchEvent


def test_s3_batch_event() -> None:
    event: S3BatchEvent = {
        "invocationSchemaVersion": "1.0",
        "invocationId": "YXNkbGZqYWRmaiBhc2RmdW9hZHNmZGpmaGFzbGtkaGZza2RmaAo",
        "job": {
            "id": "f3cc4f60-61f6-4a2b-8a21-d07600c373ce"
        },
        "tasks": [
            {
                "taskId": "dGFza2lkZ29lc2hlcmUK",
                "s3Key": "customerImage1.jpg",
                "s3VersionId": "1",
                "s3BucketArn": "arn:aws:s3:us-east-1:0123456788:examplebucket"
            }
        ]
    }
