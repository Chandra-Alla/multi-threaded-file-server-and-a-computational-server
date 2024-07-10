Multi-Threaded File Server and Computational Server

This project introduces a multi-threaded file server and a computational server, implementing Remote Procedure Call (RPC) based communication in Python.

Requirements:

1. Python3
2. rpyc Library

Instructions:

1. Unzip the Project: Begin by unzipping the project zip file into a designated folder.
2. Open Terminals: Open two separate terminal windows.
3. Set Project Directory: Navigate to the project root directory in both terminals using the command below. Replace "YOUR PROJECT ROOT DIRECTORY" with your specific project root directory.

   cd YOUR PROJECT ROOT DIRECTORY

Part 1 Execution:

1. Set Directory: Navigate to Part1 in both terminals using the following command.
   cd Part1

2. Run Server: Execute the following command in one of the terminals to start the server.
   python server.py

3. Run Client: Launch the client in the other terminal with this command.
   python client.py

4. Client Operations: Utilize the client terminal to select the desired operation: Upload, Download, Delete, or Rename.

5. Follow Instructions: Adhere to the instructions displayed in the terminal to initiate the chosen operation.

6. Check Directories: Examine the server (./Part1/files/server) and client (./Part1/files/client) directories for file modifications based on the executed operation.

Part 2 Execution:

1. Set Directory: Access Part2 in both terminals with the following command.
   cd Part2

2. Run Server: Initiate the server in one terminal via this command.
   python server.py

3. Run Client: In the other terminal, run the client using this command.
   python client.py

4. Client Logs: Review the client terminal for logs detailing changes made to files in the server directory.

5. Check Directories: Inspect the server (./Part2/files/server) and client (./Part2/files/client) directories to confirm file alterations in line with the executed operation, as shown in the client terminal.

Part 3 Execution:

Synchronous:

1. Set Directory: Navigate to Part3\synchronous in both terminals with this command.
   cd Part3\synchronous

2. Run Server: Commence the server in one terminal using this command.
   python server.py

3. Run Client: In the other terminal, launch the client with the following command.
   python client.py

4. Client Operations: Utilize the client terminal to select the operation to be performed: ADD or SORT.

5. Follow Instructions: Adhere to the instructions displayed in the terminal to initiate the chosen operation.

6. Check Client Terminal: Review the client terminal for the result based on the executed operation.

Asynchronous:

1. Set Directory: Navigate to Part3\asynchronous in both terminals using this command.
   cd Part3\asynchronous

2. Run Server: Commence the server in one terminal with this command.
   python server.py

3. Run Client: In the other terminal, launch the client using this command.
   python client.py

4. Client Operations: Utilize the client terminal to select the operation to be performed: ADD or SORT.

5. Follow Instructions: Adhere to the instructions displayed in the terminal to initiate the chosen operation.

6. Check Client Terminal: Review the client terminal for the result based on the executed operation.
