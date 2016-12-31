from flask import Flask
app = Flask(__name__)




@app.route("/")
def hello():
    htmlFileAsString = readFile()
    return htmlFileAsString

def readFile():
    file = open("index.html", "r")
    return file.read()


if __name__ == "__main__":
    app.run()
