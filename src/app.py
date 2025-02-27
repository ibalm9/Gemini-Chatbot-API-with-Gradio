import os
import sys
from flask import Flask
from interface import create_interface

app = Flask(__name__)
interface = create_interface()

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=8080)
