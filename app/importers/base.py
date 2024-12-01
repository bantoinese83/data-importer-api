import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class DataImporter(ABC):
    """
    Abstract base class for data importers.

    Methods:
        import_data(): Abstract method to import data based on the client's method.
        can_handle(config: dict) -> bool: Determine if this importer can handle the provided configuration.
        validate_config(config: dict) -> bool: Validate the configuration for the importer.
        required_config_keys() -> list: Return a list of required configuration keys.
        handle_error(error: Exception) -> dict: Handle errors that occur during data import.
    """

    @abstractmethod
    async def import_data(self):
        """
        Import data based on the client's method.

        This method must be implemented by subclasses.

        Returns:
            dict: A dictionary containing the status and imported data.
        """
        pass

    @classmethod
    def can_handle(cls, config: dict) -> bool:
        """
        Determine if this importer can handle the provided configuration.

        Args:
            config (dict): The configuration dictionary.

        Returns:
            bool: True if the importer can handle the configuration, False otherwise.
        """
        return False

    @classmethod
    def validate_config(cls, config: dict) -> bool:
        """
        Validate the configuration for the importer.

        Args:
            config (dict): The configuration dictionary.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        required_keys = cls.required_config_keys()
        for key in required_keys:
            if key not in config:
                logger.error(f"Missing required config key: {key}")
                return False
        return True

    @classmethod
    def required_config_keys(cls) -> list:
        """
        Return a list of required configuration keys.

        Returns:
            list: A list of required configuration keys.
        """
        return []

    @staticmethod
    async def handle_error(error: Exception) -> dict:
        """
        Handle errors that occur during data import.

        Args:
            error (Exception): The exception that occurred.

        Returns:
            dict: A dictionary containing the error status and message.
        """
        logger.error(f"An error occurred: {error}")
        return {"status": "error", "message": str(error)}