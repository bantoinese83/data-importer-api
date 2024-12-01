import logging
from app.importers.base import DataImporter
import httpx

logger = logging.getLogger(__name__)

class APIImporter(DataImporter):
    """
    APIImporter is a concrete implementation of DataImporter for handling API data sources.

    Attributes:
        api_url (str): The URL of the API endpoint.
    """

    def __init__(self, api_url: str):
        """
        Initialize the APIImporter with the given API URL.

        Args:
            api_url (str): The URL of the API endpoint.
        """
        self.api_url = api_url

    @classmethod
    def can_handle(cls, config: dict) -> bool:
        """
        Determine if this importer can handle the provided configuration.

        Args:
            config (dict): The configuration dictionary.

        Returns:
            bool: True if the configuration is for an API source, False otherwise.
        """
        return config.get("type") == "api" and "api_url" in config

    async def import_data(self):
        """
        Import data from the API endpoint.

        Returns:
            dict: A dictionary containing the status, source, and imported data.

        Raises:
            httpx.HTTPStatusError: If an HTTP error occurs during data import.
            httpx.RequestError: If a request error occurs during data import.
            Exception: If an unexpected error occurs during data import.
        """
        logger.info(f"Fetching data from API: {self.api_url}")
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.api_url)
                response.raise_for_status()
            logger.info("Data fetched successfully from API")
            return {"status": "success", "source": "API", "data": response.json()}
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            return {"status": "error", "message": f"HTTP error: {e.response.status_code}"}
        except httpx.RequestError as e:
            logger.error(f"Request error occurred: {e}")
            return {"status": "error", "message": "Request error"}
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return {"status": "error", "message": "An unexpected error occurred"}