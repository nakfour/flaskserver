import os
import kfp
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

print("Flask Server")


app = Flask(__name__)
print("HTTP Server started")
@app.route('/',methods = ['POST', 'GET'])
# ‘/’ URL is bound with hello_world() function.
def launchPipeline():
    client = kfp.Client(host='http://ml-pipeline-ui:80')
    print(client.list_experiments())
    run_result = client.run_pipeline(experiment_id='64d106b9-d17e-4ff1-a8fa-004fa3e75891', job_name='elyra-kubeflow-pytorchxx', pipeline_id='14bfa53a-7e0a-4919-a303-a65b8908247b', params=None)
    print("Sent Pipeline Run")
    print(run_result)
    return 'Pipeline Run Success'
  
app.run(host='0.0.0.0', port=8080)


