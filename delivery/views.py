from app import app

@app.route("/") # decorator
def index():
    return "<h1>Hello World</h1>"

@app.route("/contato") #VIEWS
def sobre():
    return "<form><input type='text'></input></form>"