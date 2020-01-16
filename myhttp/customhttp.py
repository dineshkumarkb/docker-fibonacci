from flask import Flask
import logging,json

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)



@app.route('/')
def hello():
    log.info(" Entering root path ")
    return json.dumps("<html><h1>Hello World</h1></html>")

@app.route('/dinesh',methods=['GET'])
def get_handler():
    log.info(" This is a GET request ")
    return "200   Success"


if __name__ == "__main__":
    PORT = 8000
    HOST = '0.0.0.0'
    log.info(" Server starting...")
    log.info(" CustomHTTP : " + " Server started and listening at port %s " % (PORT))
    app.run(host=HOST,port=PORT,debug=True)