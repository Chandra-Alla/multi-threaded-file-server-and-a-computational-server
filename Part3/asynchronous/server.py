# Import the necessary libraries
import rpyc
from rpyc.utils.server import ThreadedServer
import time

# Define the port for the server
cka0054_port = 3000


# Create a custom XML-RPC server using RPyC's Service class
class cka0054_CustomXMLRPCServer(rpyc.Service):

    # This method is called when a client connects to the server
    def on_connect(self, cka0054_conn):
        print(f"\nClient is connected on port {cka0054_port} ")

    # This method is called when a client disconnects from the server
    def on_disconnect(self, cka0054_conn):
        print(f"\nClient is disconnected.")

    # Expose the "addFunction" method to clients
    def exposed_addFunction(self, cka0054_i1, cka0054_i2):
        print(f"\nPerforming addition: {cka0054_i1} + {cka0054_i2}")

        # Perform the addition asynchronously
        self.cka0054_additionResult = cka0054_additionAsync(cka0054_i1, cka0054_i2)

        # Simulate some processing time
        time.sleep(2)

        # Notify the client that the result is ready and return it
        print(f"\nAddition result is ready for the client. Sum: {self.cka0054_additionResult}\n")
        return self.cka0054_additionResult

    # Expose the "sortFunction" method to clients
    def exposed_sortFunction(self, cka0054_li):
        print(f"\nPerforming array sorting: {cka0054_li}")

        # Perform the sorting asynchronously
        self.cka0054_sortingResult = cka0054_sortAsync(cka0054_li)

        # Simulate some processing time
        time.sleep(1)

        # Notify the client that the result is ready and return it
        print(f"\nSorting result is ready for the client. Sorted Array: {self.cka0054_sortingResult}\n")
        return self.cka0054_sortingResult


# Asynchronous function to perform addition
def cka0054_additionAsync(cka0054_i1, cka0054_i2):
    return int(cka0054_i1) + int(cka0054_i2)


# Asynchronous function to perform sorting
def cka0054_sortAsync(cka0054_li):
    return sorted(cka0054_li)


# Create a threaded server with the custom XML-RPC server class
cka0054_server = ThreadedServer(cka0054_CustomXMLRPCServer, port=cka0054_port)

# Start the server and listen for incoming client connections
cka0054_server.start()
