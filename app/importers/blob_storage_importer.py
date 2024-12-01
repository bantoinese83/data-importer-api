import logging
import boto3
from botocore.exceptions import BotoCoreError, ClientError

from app.importers.base import DataImporter

logger = logging.getLogger(__name__)

class BlobStorageImporter(DataImporter):
    """
    BlobStorageImporter is a concrete implementation of DataImporter for handling S3 blob storage data sources.

    Attributes:
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key of the object in the S3 bucket.
        s3_client (boto3.client): The boto3 S3 client.
    """

    def __init__(self, bucket_name: str, object_key: str):
        """
        Initialize the BlobStorageImporter with the given S3 bucket name and object key.

        Args:
            bucket_name (str): The name of the S3 bucket.
            object_key (str): The key of the object in the S3 bucket.
        """
        self.bucket_name = bucket_name
        self.object_key = object_key
        self.s3_client = boto3.client("s3")

    @classmethod
    def can_handle(cls, config: dict) -> bool:
        """
        Determine if this importer can handle the provided configuration.

        Args:
            config (dict): The configuration dictionary.

        Returns:
            bool: True if the configuration is for an S3 blob storage source, False otherwise.
        """
        return config.get("type") == "blob_storage" and "bucket_name" in config and "object_key" in config

    async def import_data(self):
        """
        Import data from the S3 bucket.

        Returns:
            dict: A dictionary containing the status, source, and imported data.

        Raises:
            ClientError: If a client error occurs during data import.
            BotoCoreError: If a BotoCore error occurs during data import.
            Exception: If an unexpected error occurs during data import.
        """
        logger.info(f"Fetching data from S3 bucket: {self.bucket_name}, key: {self.object_key}")
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=self.object_key)
            data = response["Body"].read().decode("utf-8")
            logger.info("Data fetched successfully from S3")
            return {"status": "success", "source": "S3", "data": data}
        except ClientError as e:
            logger.error(f"Client error occurred: {e.response['Error']['Message']}")
            return {"status": "error", "message": f"Client error: {e.response['Error']['Message']}"}
        except BotoCoreError as e:
            logger.error(f"BotoCore error occurred: {e}")
            return {"status": "error", "message": "BotoCore error"}
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return {"status": "error", "message": "An unexpected error occurred"}