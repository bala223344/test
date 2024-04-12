from flask import Flask
from getpass4 import getpass



def create_app(*args, **kwargs):
    app = Flask(__name__)
    print (kwargs["phrase"])  #secret
    global_decryptor = kwargs["phrase"]

    @app.route("/")
    def index():
        return "decryptor entered : " + global_decryptor
    
    return app



myapp = create_app



