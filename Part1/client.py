import xmlrpc.client  # Import the XML-RPC client library
import os  # Import the os library for file operations
import threading  # Import the threading library for multi-threading support

# Define constants
cka0054_port = 3000  # The port on which the server is running
cka0054_clientDataLocation = "./files/client/"  # The directory where client files are stored

# Create an XML-RPC client proxy to communicate with the server
cka0054_server_proxy = xmlrpc.client.ServerProxy(f"http://localhost:{cka0054_port}")


# Function to upload a file to the server
def cka0054_uploadFileToServer(fileName):
    try:
        # Construct the full path to the client file
        cka0054_location = os.path.join(cka0054_clientDataLocation, fileName)

        # Open the file in binary read mode and send it to the server as binary data
        with open(cka0054_location, 'rb') as cka0054_fo:
            cka0054_server_proxy.UploadFile(fileName, xmlrpc.client.Binary(cka0054_fo.read()))

        # Print a success message
        print(f"\nFile: {fileName} uploaded from client to server.")
    except OSError:
        # Print an error message if the upload fails
        print("\nUpload Failed.")


# Function to download a file from the server
def cka0054_downloadFileFromServer(fileName):
    try:
        # Construct the full path where the downloaded file will be saved
        cka0054_location = os.path.join(cka0054_clientDataLocation, fileName)

        # Open a file in binary write mode and write the downloaded binary data to it
        cka0054_binary_data = cka0054_server_proxy.DownloadFile(fileName)
        print(cka0054_binary_data, 'cka0054_Binary_data');
        if cka0054_binary_data is not None and cka0054_binary_data != 'Error Occurred' and cka0054_binary_data.data is not None:
            with open(cka0054_location, 'wb') as cka0054_fo:
                cka0054_fo.write(cka0054_binary_data.data)
            # Print a success message
            print(f"\nFile: {fileName} downloaded from server to client.")
        else:
            # Print a failure message
            print(f"\nDownload Failed: File {fileName} not found on the server or there was an error during download.")
    except OSError:
        # Print an error message if the download fails
        print("\nDownload Failed.")


# delete file function
def cka0054_deleteFileFromServer(cka0054_name_f: str):
    try:
        # Remove the specified file from the server
        cka0054_result = cka0054_server_proxy.DeleteFile(cka0054_name_f)
        if (cka0054_result == "Successful"):
            # Print a success message
            print(f"\nFile: {cka0054_name_f} deleted on server.")
        else:
            # Print a failure message
            print(f"\nFile Deletion Failed, please check the filename")
    except OSError:
        # Print an error message if the deletion fails
        print("\nDelete Failed.")
    return


# rename file function
def cka0054_renameFileInServer(cka0054_name_f_old: str, cka0054_name_f_new: str):
    try:
        # calling the RPC to rename file on the server
        cka0054_result = cka0054_server_proxy.RenameFile(cka0054_name_f_old, cka0054_name_f_new)
        if (cka0054_result == "Successful"):
            # Print a success message
            print(f"\nFile: {cka0054_name_f_old} has been renamed to {cka0054_name_f_new}.")
        else:
            # Print a failure message
            print(f"\nFile Rename Failed, please check the filename")
    except OSError:
        # Print an error message if the renaming fails
        print(f"\nInvalid File: {cka0054_name_f_old}")
    return


# Function to handle user input and execute operations
def cka0054_startClientExecution():
    while True:
        print(
            "\n\nAvailable Operations\n"
            "\n 1. Upload"
            "\n 2. Download"
            "\n 3. Delete"
            "\n 4. Rename"
            "\n 5. Exit\n")

        # Get the user's choice of operation
        cka0054_selectedOption = input("Please choose operation number: ")

        if cka0054_selectedOption == "1":
            cka0054_enteredFileName = input("File Name With Extension: ")
            cka0054_uploadFileToServer(cka0054_enteredFileName)
        elif cka0054_selectedOption == "2":
            cka0054_enteredFileName = input("File Name With Extension: ")
            cka0054_downloadFileFromServer(cka0054_enteredFileName)
        elif cka0054_selectedOption == "3":
            cka0054_enteredFileName = input("File Name With Extension: ")
            cka0054_deleteFileFromServer(cka0054_enteredFileName)
        elif cka0054_selectedOption == "4":
            cka0054_oldFileName = input("Old File Name With Extension: ")
            cka0054_newFileName = input("New File Name With Extension: ")
            cka0054_renameFileInServer(cka0054_oldFileName, cka0054_newFileName)
        elif cka0054_selectedOption == "5":
            os._exit(0)
        else:
            print("\nInvalid Input")


# Create a thread for client execution
cka0054_masterThread = threading.Thread(target=cka0054_startClientExecution)
cka0054_masterThread.start()
