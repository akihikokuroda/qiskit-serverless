from django.shortcuts import render

from django.http import HttpResponse
import requests
import json


def target(request):
    return HttpResponse(content=json.dumps({"job_id": "This is job id"}) )

def handle_runtime_request(request):
    print(type(request))
    print(request)
    #runtime_service_response = requests.post(url="http://127.0.0.1/target/", json=request.json)
    runtime_service_response = requests.post(url="http://127.0.0.1:8000/api/target")

    # get primitive job id and save it to job
    print(runtime_service_response.content)
    primitive_job_id = json.loads(runtime_service_response.content).get("job_id")
    gateway_response = requests.post(
        url="api/v1/jobs/program_job_id/primitives", 
        json={"primitive_id": primitive_job_id})

    return runtime_service_response
