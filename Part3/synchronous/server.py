# Import necessary libraries
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn as CreateThread

# Define the port for the server connection
cka0054_port = 3000


# Define a custom XML-RPC server class that inherits from CreateThread and SimpleXMLRPCServer
class cka0054_CustomXMLRPCServer(CreateThread, SimpleXMLRPCServer):
    pass


# Function to perform addition operation
def cka0054_additionSync(cka0054_number1, cka0054_number2):
    # Calculate the addition operation result
    cka0054_addOperationResult = cka0054_number1 + cka0054_number2

    # Return the result
    return cka0054_addOperationResult


# Function to perform sorting operation
def cka0054_sortingSync(cka0054_input_list):
    # Sort the input list in ascending order
    cka0054_input_list.sort()

    # Return the sorted list
    return cka0054_input_list


# Create an instance of the custom server class and register functions
with cka0054_CustomXMLRPCServer(('localhost', cka0054_port), allow_none=True) as cka0054_server:
    # Register standard introspection functions
    cka0054_server.register_introspection_functions()

    # Register the cka0054_additionSync function with the name "additionFunction"
    cka0054_server.register_function(cka0054_additionSync, "additionFunction")

    # Register the cka0054_sortingSync function with the name "sortFunction"
    cka0054_server.register_function(cka0054_sortingSync, "sortFunction")

    # Print a message indicating that the server is running
    print(f"\nServer is running on port {cka0054_port}")

    # Start serving requests indefinitely
    cka0054_server.serve_forever()
