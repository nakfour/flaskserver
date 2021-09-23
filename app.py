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
    return 'Hello World'
  
app.run(host='0.0.0.0', port=8080)


