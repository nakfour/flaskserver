import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

print("Flask Server")


app = Flask(__name__)
print("HTTP Server started")
app.run(host='0.0.0.0', port=8080)
