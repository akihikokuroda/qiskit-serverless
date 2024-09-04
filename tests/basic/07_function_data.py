import os
from qiskit_serverless import QiskitFunction, ServerlessClient

serverless = ServerlessClient(
     token=os.environ.get("GATEWAY_TOKEN", "awesome_token"),
     host=os.environ.get("GATEWAY_HOST", "http://localhost:8000"),
)

help = """
title: function-data
description: sample function implemented in a custom image
arguments:
     service: service created with the accunt information
     circuit: circuit
     observable: observable
"""

function_data_function = QiskitFunction(
     title="function-data",
     image="function_data:latest",
     provider=os.environ.get("PROVIDER_ID", "mockprovider"),
     description=help
)
serverless.upload(function_data_function)

my_function = serverless.get("function-data")
job = my_function.run(message="This")
print(job.result())
job = my_function.run(message="is")
print(job.result())
job = my_function.run(message="the")
print(job.result())
job = my_function.run(message="example")
print(job.result())
job = my_function.run(message="delete")

print(job.result())
job = my_function.run(message="This")
print(job.result())
job = my_function.run(message="is")
print(job.result())
job = my_function.run(message="the")
print(job.result())
job = my_function.run(message="next")
print(job.result())
job = my_function.run(message="example")
print(job.result())
print(job.logs())
job = my_function.run(message="delete")


