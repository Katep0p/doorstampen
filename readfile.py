from flask import Flask
app = Flask(__name__)

file = open("/Users/Kate/Kod/doorstampen/index.html", "r")
print file.read()


@app.route("/")
def hello():
    htmlFileAsString = readFile()
    return htmlFileAsString


# med den har taggen under far man en sjuk felkod?
#Tar man bort den ar allt lungt

#if __name__ == "__main__":
#    app.run()
