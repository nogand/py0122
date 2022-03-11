from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_en():
    return "Hello World!"

@app.route("/es")
def hello_sp():
    return "¡Hola, Mundo!"

@app.route("/no")
def hello_no():
    return "Hei, Labbetuss!"

if __name__ == "__main__":
    app.run()

