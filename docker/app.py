#imports the socket module
import socket
#Imports the module Flask, and creates references to all public objects defined by that module in the current namespace (that is, everything that doesn’t have a name starting with _) or whatever name you mentioned.
from flask import Flask

app = Flask(__name__)

#Sets the application route
@app.route('/')
#Creates the function 'hello' to return message
def hello():
    hostname = socket.gethostname()
    return 'Hello, I am {}\n'.format(hostname)