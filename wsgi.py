from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "please please work"

if __name__ == "__main__":
    application.run()
