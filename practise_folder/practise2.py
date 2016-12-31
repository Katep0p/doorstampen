from flask import Flask
app = Flask(__name__)

@app.route("/file:///Users/Kate/Kod/doorstampen/practise_folder/practis2.html")
def hello():
    htmlFileAsString = readFile()
    return htmlFileAsString


if __name__ == "__main__":
    app.run()

print "hello"
import time
# dd/mm/yyyy
print "The date is", (time.strftime("%d:%m:%Y"))
