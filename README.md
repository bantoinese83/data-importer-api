# Data Importer API 🚀

## 🚀 Technologies

<img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
<img src="https://img.shields.io/badge/FastAPI-0.115.5-green.svg" alt="FastAPI">
<img src="https://img.shields.io/badge/httpx-0.27.2-blue.svg" alt="httpx">
<img src="https://img.shields.io/badge/pandas-2.2.3-green.svg" alt="pandas">
<img src="https://img.shields.io/badge/boto3-1.35.68-blue.svg" alt="boto3">

## ✨ Key Features

- Import data from Excel files
- Import data from APIs
- Import data from FTP servers
- Import data from S3 blob storage
- Robust error handling and logging

## 📝 Description

The Data Importer API is a FastAPI-based application that allows importing data from various sources such as Excel
files, APIs, FTP servers, and S3 blob storage. This API provides a unified interface to handle different data import
mechanisms.

## 🚀 Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bantoinese83/data-importer-api.git
    cd data-importer-api
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

The configuration for different clients is stored in `app/config.json`. Here is an example configuration:

```json
{
  "ClientA": {
    "type": "excel",
    "file_path": "path/to/excel/file.xlsx"
  },
  "ClientB": {
    "type": "api",
    "api_url": "https://api.example.com/data"
  },
  "ClientC": {
    "type": "ftp",
    "ftp_url": "ftp://example.com/data"
  }
}
```

## Usage

1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Access the API documentation at [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. To import data for a specific client, send a POST request to `/import/{client_name}`. For example:
    ```sh
    curl -X POST "http://127.0.0.1:8000/import/ClientA"
    ```

## Importers

### Excel Importer

Handles importing data from Excel files.

### API Importer

Handles importing data from APIs.

### FTP Importer

Handles importing data from FTP servers.

### Blob Storage Importer

Handles importing data from S3 blob storage.

## Error Handling

The API provides detailed error messages and logs errors for troubleshooting. Common errors include:

- `FileNotFoundError`: Raised when the specified file is not found.
- `httpx.HTTPStatusError`: Raised for HTTP errors during API data import.
- `ClientError`: Raised for client errors during S3 data import.
- `BotoCoreError`: Raised for BotoCore errors during S3 data import.

## Endpoints

| Method | Endpoint                | Description                        |
|--------|-------------------------|------------------------------------|
| POST   | `/import/{client_name}` | Import data from a specific client |

## 📊 GitHub Profile Insights

### 🚀 My GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=bantoinese83&show_icons=true&theme=radical)

---

### 💻 Top Languages

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=bantoinese83&layout=compact&theme=radical)

---

### 🌟 Contribution Graph

![Contribution Graph](https://github-readme-activity-graph.vercel.app/graph?username=bantoinese83&theme=radical)

---

### 🏆 GitHub Achievements

![GitHub Achievements](https://github-profile-trophy.vercel.app/?username=bantoinese83&theme=radical)

---

### 🐙 Streak Stats

![GitHub Streak Stats](https://streak-stats.demolab.com?user=bantoinese83&theme=radical&date_format=M%20j%5B%2C%20Y%5D)

---

Feel free to explore my repositories and projects to see what I've been working on. 🚀