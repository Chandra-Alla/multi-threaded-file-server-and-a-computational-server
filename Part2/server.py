# Import necessary libraries
from xmlrpc.server import SimpleXMLRPCServer  # Import the SimpleXMLRPCServer class for creating an XML-RPC server
from socketserver import ThreadingMixIn as CreateThread  # Import the ThreadingMixIn class to enable multi-threading
import os  # Import the os library for file operations

# Define Constants
cka0054_port = 3000  # The port on which the server is running
cka0054_serverFilesLocation = "./files/server/"  # The directory where server files are stored


# Define a custom class for the XML-RPC server
class cka0054_CustomXMLRPCServer(CreateThread, SimpleXMLRPCServer):
    pass


# Function to upload a file to the server
def cka0054_uploadFileToServer(fileName: str, directoryName):
    try:
        # Construct the full path to the server file
        cka0054_location = os.path.join(cka0054_serverFilesLocation, fileName)

        # Open the file in binary write mode and write the uploaded binary data to it
        with open(cka0054_location, 'wb') as cka0054_file:
            cka0054_file.write(directoryName.data)

        return "Successful"  # Return without errors if successful
    except OSError:
        # Print an error message if the upload fails
        print(f"\nInvalid File: {fileName}")
        return "Error Occured"


# Function to delete a file from the server
def cka0054_deleteFileFromServer(fileName: str):
    try:
        # Remove the specified file from the server
        os.remove(os.path.join(cka0054_serverFilesLocation, fileName))

        # Print a success message
        print(f"\nFile: {fileName} deleted.")
        return "Successful"  # Return without errors if successful
    except OSError:
        # Print an error message if the deletion fails
        print(f"\nInvalid File: {fileName}")
        return "Error Occured"


# Create an instance of the custom server class and register functions
with cka0054_CustomXMLRPCServer(('localhost', cka0054_port), allow_none=True) as cka0054_server:
    cka0054_server.register_introspection_functions()  # Register functions for introspection
    cka0054_server.register_function(cka0054_uploadFileToServer, "UploadFile")  # Register upload function
    cka0054_server.register_function(cka0054_deleteFileFromServer, "DeleteFile")  # Register delete function

    print(f"Server is running on {cka0054_port}")  # Print a message indicating the server is running
    cka0054_server.serve_forever()  # Start the server and keep it running
