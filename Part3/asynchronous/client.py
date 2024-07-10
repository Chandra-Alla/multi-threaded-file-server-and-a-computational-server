# Import the necessary libraries
import asyncio
import rpyc
import os

# Define the server port
cka0054_server_port = 3000

# Connect to the server
cka0054_server_connection = rpyc.connect("localhost", cka0054_server_port)

# Define a function for background tasks
async def cka0054_simulate_background_tasks():
    cka0054_start_with = 0
    cka0054_end_at = 10
    while cka0054_start_with < cka0054_end_at:
        print(f"Simulated Background Task {cka0054_start_with + 1} running ")
        await asyncio.sleep(2)
        cka0054_start_with += 1

# Define a function to execute client operations
async def cka0054_execute_client_operations():
    print(
        "\nList Of Available operations:\n"
        "\n 1. Add"
        "\n 2. Sort"
        "\n 3. Exit\n")

    cka0054_selected_option = input("Choose any of the above options: ")

    if cka0054_selected_option == "1":
        cka0054_number1 = input("Enter number 1: ")
        cka0054_number2 = input("Enter number 2: ")

        # Asynchronous call to the addFunction on the server
        cka0054_async_add_op = rpyc.async_(cka0054_server_connection.root.addFunction)
        cka0054_addition_result = cka0054_async_add_op(int(cka0054_number1), int(cka0054_number2))

        # Define an asynchronous function to check the status of the addition operation result
        async def cka0054_addition_result_status(cka0054_op_res):
            if cka0054_op_res.ready:
                print(cka0054_op_res)
                print(f"\nResult: {cka0054_op_res.value}\n")
                return
            else:
                await asyncio.sleep(5)
                await cka0054_addition_result_status(cka0054_op_res)
        print(cka0054_addition_result)
        await cka0054_addition_result_status(cka0054_addition_result)
    elif cka0054_selected_option == "2":
        print("Hint: Enter values like this: 10, 20, 1, 3")
        cka0054_array_input = input("Enter comma-separated integer values: ")
        cka0054_array_input_list = list(map(int, cka0054_array_input.split(',')))

        # Asynchronous call to the sortFunction on the server
        cka0054_async_sort_op = rpyc.async_(cka0054_server_connection.root.sortFunction)
        cka0054_sorting_result = cka0054_async_sort_op(cka0054_array_input_list)

        print(f"\nUnsorted Array: {cka0054_array_input_list}\n")

        # Define an asynchronous function to check the status of the sorting operation result
        async def cka0054_sorting_result_status(cka0054_op_res):
            if cka0054_op_res.ready:
                print(cka0054_op_res)
                print(f"\nSorted Array: {cka0054_op_res.value}\n")
            else:
                await asyncio.sleep(5)
                await cka0054_sorting_result_status(cka0054_op_res)
        print(cka0054_sorting_result)
        await cka0054_sorting_result_status(cka0054_sorting_result)
    elif cka0054_selected_option == "3":
        os._exit(0)
    else:
        print("\nInvalid Input")

# Define the main function
async def cka0054_main_function():
    while True:
        # Run both client operations and background tasks concurrently
        await asyncio.gather(cka0054_execute_client_operations(), cka0054_simulate_background_tasks())

# Run the main function using asyncio
asyncio.run(cka0054_main_function())
