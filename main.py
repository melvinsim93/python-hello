from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello I am Melvin's python module copied from Anil Bidari, this is for the actual Assessment!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
