import time


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    htmlFileAsString = readFile()
    My_Calendar = (time.strftime("%d:%m:%Y"))
    My_Calendar2 = (time.strftime("%A %B %d %Y"))
    htmlFileAsString = htmlFileAsString.replace("{{todays date}}", My_Calendar)
    htmlFileAsString = htmlFileAsString.replace("{{todays_date2}}", My_Calendar2)
    return htmlFileAsString

def readFile():
    file = open("index.html", "r")
    return file.read()


if __name__ == "__main__":
    app.run()
