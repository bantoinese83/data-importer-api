import logging
from app.importers.base import DataImporter
import pandas as pd

logger = logging.getLogger(__name__)

class ExcelImporter(DataImporter):
    """
    ExcelImporter is a concrete implementation of DataImporter for handling Excel data sources.

    Attributes:
        file_path (str): The path to the Excel file.
    """

    def __init__(self, file_path: str):
        """
        Initialize the ExcelImporter with the given file path.

        Args:
            file_path (str): The path to the Excel file.
        """
        self.file_path = file_path

    @classmethod
    def can_handle(cls, config: dict) -> bool:
        """
        Determine if this importer can handle the provided configuration.

        Args:
            config (dict): The configuration dictionary.

        Returns:
            bool: True if the configuration is for an Excel source, False otherwise.
        """
        return config.get("type") == "excel" and "file_path" in config

    async def import_data(self):
        """
        Import data from the Excel file.

        Returns:
            dict: A dictionary containing the status, source, and imported data.

        Raises:
            FileNotFoundError: If the Excel file is not found.
            Exception: If an unexpected error occurs during data import.
        """
        logger.info(f"Importing data from Excel file: {self.file_path}")
        try:
            data = pd.read_excel(self.file_path)
            logger.info("Data imported successfully from Excel")
            return {"status": "success", "source": "Excel", "data": data.to_dict()}
        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            return {"status": "error", "message": "File not found"}
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return {"status": "error", "message": "An unexpected error occurred"}