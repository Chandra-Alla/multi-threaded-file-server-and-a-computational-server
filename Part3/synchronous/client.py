# Import the necessary libraries
import xmlrpc.client
import os
import threading

# Define the port for the server connection
cka0054_port = 3000

# Create an XML-RPC client proxy to communicate with the server
cka0054_rpc_server = xmlrpc.client.ServerProxy(f"http://localhost:{cka0054_port}")


# Function to perform addition operation and print the result
def cka0054_additionSync(cka0054_number1, cka0054_number2):
    # Call the addition function on the server and get the result
    cka0054_addOperationResult = cka0054_rpc_server.additionFunction(cka0054_number1, cka0054_number2)

    # Print the result of the addition
    print(f"\n{cka0054_number1} + {cka0054_number2} = {cka0054_addOperationResult}")
    return


# Function to perform sorting operation and print the result
def cka0054_sortSync(cka0054_input_list):
    # Call the sorting function on the server and get the result
    cka0054_sortOperationResult = cka0054_rpc_server.sortFunction(cka0054_input_list)

    # Print the unsorted and sorted lists
    print(f"\nSorted: {cka0054_sortOperationResult}")
    return


# Function to handle user input and execute operations
def cka0054_execute_client_operations():
    while True:
        print(
            "\n\nAvailable Operations:\n"
            "\n 1. Add"
            "\n 2. Sort"
            "\n 3. Exit\n")

        # Get the user's input for the selected operation
        cka0054_selected_option = input("Please select an option: ")

        if cka0054_selected_option == "3":
            # Exit the program
            os._exit(0)
        elif cka0054_selected_option == "1":
            cka0054_number_input1 = input("Enter Number 1: ")
            cka0054_number_input2 = input("Enter Number 2: ")

            # Perform addition operation with the provided numbers
            cka0054_additionSync(int(cka0054_number_input1), int(cka0054_number_input2))
        elif cka0054_selected_option == "2":
            print("Hint, Enter values like this: 10,20,1,3")
            cka0054_array_input = input("Enter comma separated integer values: ")
            cka0054_array_values = list(map(int, cka0054_array_input.split(',')))

            # Perform sorting operation with the provided array
            cka0054_sortSync(cka0054_array_values)
        else:
            print("\nInvalid Input")


# Create a thread to execute client operations
cka0054_main_thread = threading.Thread(target=cka0054_execute_client_operations)
cka0054_main_thread.start()
