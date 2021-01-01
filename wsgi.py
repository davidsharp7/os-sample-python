from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "This was deployed automatically!!"

if __name__ == "__main__":
    application.run()
