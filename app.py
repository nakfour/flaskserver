import os
import kfp
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

print("Flask Server")


app = Flask(__name__)
print("HTTP Server started")
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def launchPipeline():
    client = kfp.Client(host='http://ml-pipeline-ui:80')
    print(client.list_experiments())
    run_result = client.run_pipeline(experiment_id='f0d0fad9-ebc0-42c7-a781-67bb64e17bc6', job_name='elyra-kubeflow-pytorch', pipeline_package_path='elyra-kubeflow-pytorch', params=None)
    print("Sent Pipeline Run")
    print(run_result)
    return 'Pipeline Run Success'
  
app.run(host='0.0.0.0', port=8080)


