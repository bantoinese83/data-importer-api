import json
import logging

from fastapi import FastAPI, HTTPException, Depends

from app.importers.api_importer import APIImporter
from app.importers.excel_importer import ExcelImporter
from app.importers.ftp_importer import FTPImporter
from app.importers.blob_storage_importer import BlobStorageImporter
from app.services.importer_service import ImporterService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Data Importer 🚀",
    description="An API to import data from various sources. 📊",
    version="0.1",
    docs_url="/"
)


def get_importer_service():
    """
    Create and configure an ImporterService instance.

    Returns:
        ImporterService: An instance of ImporterService with registered importers.
    """
    importer_service = ImporterService()
    importer_service.register_importer(ExcelImporter)
    importer_service.register_importer(APIImporter)
    importer_service.register_importer(FTPImporter)
    importer_service.register_importer(BlobStorageImporter)
    return importer_service


@app.post("/import/{client_name}", response_model=dict, tags=["import 📥"], summary="Import data from a client",
          description="Import data from a client.")
async def import_data(client_name: str, importer_service: ImporterService = Depends(get_importer_service)):
    """
    Import data for a specified client.

    Args:
        client_name (str): The name of the client to import data for.
        importer_service (ImporterService): The service to manage data importers and configurations.

    Returns:
        dict: A dictionary containing the client name and the result of the import operation.

    Raises:
        HTTPException: If an error occurs during the import process.
    """
    try:
        logger.info(f"🚀 Starting data import for client: {client_name}")
        importer = importer_service.get_importer(client_name)
        result = await importer.import_data()
        logger.info(f"✅ Data import successful for client: {client_name}")
        return {"client": client_name, "result": result}
    except json.JSONDecodeError as e:
        logger.error(f"❌ JSONDecodeError: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid JSON format.")
    except ValueError as e:
        logger.error(f"❌ ValueError: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except FileNotFoundError as e:
        logger.error(f"❌ FileNotFoundError: {str(e)}")
        raise HTTPException(status_code=404, detail="File not found.")
    except Exception as e:
        logger.error(f"❌ Exception: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")