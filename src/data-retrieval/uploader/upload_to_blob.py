import os
from azure.storage.blob import BlobServiceClient

def upload_to_azure(file_path, container_name, blob_name, connection_string):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"Successfully uploaded {file_path} to Azure Blob Storage as {blob_name}")
    except Exception as ex:
        print(f"Error uploading file to Azure Blob Storage: {ex}")

def delete_local_file(file_path):
    try:
        os.remove(file_path)
        print(f"Successfully deleted {file_path}")
    except Exception as ex:
        print(f"Error deleting file {file_path}: {ex}")

if __name__ == "__main__":
    print("Uploader script started")
    azure_connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    container_name = 'newsfiles'
    shared_dir = '/shared'
    
    if not azure_connection_string:
        print("Azure storage connection string not found")
        exit(1)
    
    print(f"Contents of {shared_dir}:")
    for root, dirs, files in os.walk(shared_dir):
        for name in files:
            print(os.path.join(root, name))
    
    for file_name in os.listdir(shared_dir):
        file_path = os.path.join(shared_dir, file_name)
        print(f"Processing file: {file_path}")
        if (file_name != "scraper_done.txt"):
            upload_to_azure(file_path, container_name, file_name, azure_connection_string)
        delete_local_file(file_path)
    print("Uploader script finished")
