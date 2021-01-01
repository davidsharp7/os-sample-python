from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "with a new stage - this is cool"

if __name__ == "__main__":
    application.run()
