from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "please please work this time you mutha"

if __name__ == "__main__":
    application.run()
