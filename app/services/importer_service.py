import json
import logging
from app.importers.base import DataImporter

logger = logging.getLogger(__name__)

class ImporterService:
    """
    Service to manage data importers and configurations.

    Attributes:
        importer_registry (list): List of registered importer classes.
        config (dict): Loaded configuration from the config file.
    """
    def __init__(self, config_file: str = "app/config.json"):
        """
        Initialize the ImporterService with the given configuration file.

        Args:
            config_file (str): Path to the configuration file.
        """
        self.importer_registry = []
        try:
            with open(config_file, "r") as f:
                self.config = json.load(f)
            logger.info(f"Configuration loaded successfully from {config_file}")
        except FileNotFoundError as e:
            logger.error(f"Configuration file not found: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from configuration file: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading configuration: {e}")
            raise

    def register_importer(self, importer_class):
        """
        Register a new importer class.

        Args:
            importer_class (type): The importer class to register.

        Raises:
            ValueError: If the importer_class does not implement DataImporter.
        """
        if issubclass(importer_class, DataImporter):
            self.importer_registry.append(importer_class)
            logger.info(f"Registered importer: {importer_class.__name__}")
        else:
            logger.error(f"{importer_class} does not implement DataImporter")
            raise ValueError(f"{importer_class} does not implement DataImporter")

    def get_importer(self, client_name: str):
        """
        Get an importer instance for the specified client.

        Args:
            client_name (str): The name of the client.

        Returns:
            DataImporter: An instance of the appropriate importer class.

        Raises:
            ValueError: If no configuration is found for the client or no suitable importer is found.
        """
        client_config = self.config.get(client_name)
        if not client_config:
            logger.error(f"No configuration found for client: {client_name}")
            raise ValueError(f"No configuration found for client: {client_name}")

        # Find an importer that can handle this configuration
        for importer_class in self.importer_registry:
            if importer_class.can_handle(client_config):
                logger.info(f"Found importer {importer_class.__name__} for client: {client_name}")
                # Remove the 'type' key before passing the config to the importer's __init__ method
                config_without_type = {k: v for k, v in client_config.items() if k != "type"}
                return importer_class(**config_without_type)

        logger.error(f"No importer found to handle configuration: {client_config}")
        raise ValueError(f"No importer found to handle configuration: {client_config}")