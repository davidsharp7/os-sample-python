from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "t123455555"

if __name__ == "__main__":
    application.run()
