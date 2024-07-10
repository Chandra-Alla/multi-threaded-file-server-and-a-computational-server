from xmlrpc.server import SimpleXMLRPCServer  # Import the SimpleXMLRPCServer class for creating an XML-RPC server
from socketserver import \
    ThreadingMixIn as cka0054_CreateThread  # Import the ThreadingMixIn class to enable multi-threading
import xmlrpc.client  # Import the XML-RPC client library
import os  # Import the os library for file operations

# Define Constants
cka0054_port = 3000  # The port on which the server is running
cka0054_serverDataLocation = "./files/server/"  # The directory where server files are stored


# Define a custom class for the XML-RPC server
class cka0054_CustomXMLRPCServer(cka0054_CreateThread, SimpleXMLRPCServer):
    pass


# Function to upload a file to the server
def cka0054_uploadFileToServer(cka0054_name_file: str, cka0054_directory_file):
    try:
        # Construct the full path to the server file
        cka0054_location = os.path.join(cka0054_serverDataLocation, cka0054_name_file)

        # Open the file in binary write mode and write the uploaded binary data to it
        with open(cka0054_location, 'wb') as cka0054_file:
            cka0054_file.write(cka0054_directory_file.data)
    except OSError:
        # Print an error message if the upload fails
        print(f"\nInvalid File: {cka0054_name_file}")
        return "Error Occurred"
    return "Successful"  # Return without errors if successful


# Function to download a file from the server
def cka0054_downloadFileFromServer(cka0054_name_file: str):
    try:
        # Construct the full path from where the file will be read
        cka0054_location = os.path.join(cka0054_serverDataLocation, cka0054_name_file)

        # Open the file in binary read mode and wrap it in XML-RPC Binary for transfer
        with open(cka0054_location, 'rb') as cka0054_file:
            return xmlrpc.client.Binary(cka0054_file.read())
    except OSError:
        # Print an error message if the download fails
        print(f"\nInvalid File: {cka0054_name_file}")
        return "Error Occurred"


# Function to delete a file from the server
def cka0054_deleteFileFromServer(cka0054_name_file: str):
    try:
        # Remove the specified file from the server
        os.remove(os.path.join(cka0054_serverDataLocation, cka0054_name_file))
        # Print a success message
        print(f"\nFile: {cka0054_name_file} deleted.")
    except OSError:
        # Print an error message if the deletion fails
        print(f"\nInvalid File: {cka0054_name_file}")
        return "Error Occurred"
    return "Successful"  # Return without errors if successful


# Function to rename a file on the server
def cka0054_renameFileInServer(cka0054_name_file_old: str, cka0054_name_file_new: str):
    try:
        # Rename the file on the server from old name to new name
        os.rename(os.path.join(cka0054_serverDataLocation, cka0054_name_file_old),
                  os.path.join(cka0054_serverDataLocation, cka0054_name_file_new))

        # Print a success message
        print(f"\nFile: {cka0054_name_file_old} has been renamed to {cka0054_name_file_new}.")
    except OSError:
        # Print an error message if the renaming fails
        print(f"\nInvalid File: {cka0054_name_file_old}")
        return "Error Occurred"
    return "Successful"  # Return without errors if successful


# Create an instance of the custom server class and register functions
with cka0054_CustomXMLRPCServer(('localhost', cka0054_port), allow_none=True) as cka0054_server:
    cka0054_server.register_introspection_functions()  # Register functions for introspection
    cka0054_server.register_function(cka0054_uploadFileToServer, "UploadFile")  # Register upload function
    cka0054_server.register_function(cka0054_downloadFileFromServer, "DownloadFile")  # Register download function
    cka0054_server.register_function(cka0054_renameFileInServer, "RenameFile")  # Register rename function
    cka0054_server.register_function(cka0054_deleteFileFromServer, "DeleteFile")  # Register delete function

    print(f"Server is running on {cka0054_port}...")  # Print a message indicating the server is running
    cka0054_server.serve_forever()  # Start the server and keep it running
