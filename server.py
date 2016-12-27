from flask import Flask
app = Flask(__name__)

def readFile():
    # läs fil och returnera

@app.route("/")
def hello():
    htmlFileAsString = readFile()
    return htmlFileAsString

if __name__ == "__main__":
    app.run()
