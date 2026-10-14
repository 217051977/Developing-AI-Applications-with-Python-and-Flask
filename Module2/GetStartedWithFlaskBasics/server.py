"""This class is an api server example"""
from flask import Flask
# Creates an instance of the 'Flask' class with this module class name as @arg
app = Flask(__name__)

# Set the method URL routing
@app.route("/")
@app.route("/hello-world")
def home_page():
    """Function that handles the request for this specific URL route"""
    # Prints 'Hello World' on the page
    return "Hello World"

# Set the method URL routing
@app.route("/json")
def json_page():
    """Prints 'Hello World' on the page"""
    return {"message": "Hello World"}

# Use the command flask --app server --debug run:
# --app <module_name> -> Selects the module that contains the flask application
# --debug -> Enables the debug mode
# run -> Deploys the server
