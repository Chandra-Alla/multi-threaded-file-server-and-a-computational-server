# Import necessary libraries
import xmlrpc.client  # Import the XML-RPC client library
from datetime import datetime  # Import the datetime module for timestamp
import threading  # Import the threading module for concurrent execution
import time  # Import the time module for sleep function
import filecmp  # Import the filecmp module for directory comparison
import os  # Import the os library for file operations

# Define Constants
cka0054_port = 3000  # The port on which the server is running
cka0054_server_proxy = xmlrpc.client.ServerProxy(f"http://localhost:{cka0054_port}")  # Create an XML-RPC client proxy
cka0054_clientFilesLocation = "./files/client/"  # The directory path for client files
cka0054_serverFilesLocation = "./files/server/"  # The directory path for server files


# Function to upload a file to the server
def cka0054_uploadFileToServer(fileName):
    try:
        # Open the file in binary read mode and send it to the server as binary data
        with open(cka0054_clientFilesLocation + fileName, 'rb') as cka0054_fo:
            return cka0054_server_proxy.UploadFile(fileName, xmlrpc.client.Binary(cka0054_fo.read()))
    except OSError:
        # Print an error message if the upload fails
        print("\nUpload Failed.")
    return


# Function to delete a file from the server
def cka0054_deleteFileFromServer(fileName: str):
    try:
        # Request the server to delete the specified file
        return cka0054_server_proxy.DeleteFile(fileName)
    except OSError:
        # Print an error message if the deletion fails
        print("\nDelete Failed.")
    return


# Function for automatic synchronization of directories
def cka0054_automaticDirectorySync():
    while True:
        print(f"\n{datetime.now()} Checking for file changes.")
        cka0054_dirComparison = filecmp.dircmp(cka0054_clientFilesLocation, cka0054_serverFilesLocation)
        cka0054_serverOnlyIndex = 0
        cka0054_clientOnlyIndex = 0
        cka0054_updatedFilesIndex = 0
        cka0054_filesChanged = False

        while cka0054_serverOnlyIndex < len(cka0054_dirComparison.right_only):
            # Delete files that exist on the server but not on the client
            cka0054_result = cka0054_deleteFileFromServer(cka0054_dirComparison.right_only[cka0054_serverOnlyIndex])
            if cka0054_result == "Successful":
                print("File: " + cka0054_dirComparison.right_only[cka0054_serverOnlyIndex] + " deleted from server")
                cka0054_serverOnlyIndex += 1
                cka0054_filesChanged = True
            else:
                print("Error Occured")

        while cka0054_clientOnlyIndex < len(cka0054_dirComparison.left_only):
            # Upload files that exist on the client but not on the server
            cka0054_result = cka0054_uploadFileToServer(cka0054_dirComparison.left_only[cka0054_clientOnlyIndex])
            if cka0054_result == "Successful":
                print("File: " + cka0054_dirComparison.left_only[cka0054_clientOnlyIndex] + " uploaded to server")
                cka0054_clientOnlyIndex += 1
                cka0054_filesChanged = True
            else:
                print("Error Occured")

        while cka0054_updatedFilesIndex < len(cka0054_dirComparison.diff_files):
            # Upload files that have been updated on the client
            cka0054_result = cka0054_uploadFileToServer(cka0054_dirComparison.diff_files[cka0054_updatedFilesIndex])
            if cka0054_result == "Successful":
                print("File: " + cka0054_dirComparison.diff_files[cka0054_updatedFilesIndex] + " updated on server")
                cka0054_updatedFilesIndex += 1
                cka0054_filesChanged = True
            else:
                print("Error Occured")

        if cka0054_filesChanged:
            print("Client And Server Are Now Synced")
        else:
            print("No Changes Detected, Client And Server Are On Perfect Sync.")

        time.sleep(10)  # Sleep for 10 seconds before the next check


# Create a helper thread for automatic synchronization
cka0054_helperThread = threading.Thread(target=cka0054_automaticDirectorySync)
cka0054_helperThread.start()
