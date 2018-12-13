from flask import Flask
import os

app = Flask(__name__)


@app.route("/", methods=['GET'])
def myfunc():
    return "Hey World!!!"

@app.route("/db")
def db():
    return "This is the part where you add a db service to the app"

@app.route("/vcapvars")
def vars():
    return os.environ['VCAP_SERVICES']
    

if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')
