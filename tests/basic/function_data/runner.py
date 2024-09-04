import os
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler as Sampler

def custom_function(arguments):
    # all print statement will be available in job logs
    print("Running function...")
    message = arguments.get("message")
    if message == "delete":
        os.remove("/function_data/sample.txt")
        return
    
    if os.path.exists("/function_data/sample.txt"):
        line = f" {message}"
        write_file = open("/function_data/sample.txt", "a")
        write_file.writelines(line)
        write_file.close()
    else:
        line = f" {message}"
        write_file = open("/function_data/sample.txt", "w")
        write_file.writelines(line)
        write_file.close()

    print("Completed running pattern.")
    read_file = open("/function_data/sample.txt", "r+")
    data = read_file.readlines()
    read_file.close()

    return {"message": data}

class Runner:
    def run(self, arguments: dict) -> dict:
        return custom_function(arguments)
