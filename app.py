from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    logging.info("App started for checking")
    return "My name is Sumay Chatterjee"
#logging.info("App is running succesfully")

if __name__=="__main__":
    app.run(debug=True)
    
    

