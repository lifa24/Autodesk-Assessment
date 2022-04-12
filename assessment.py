import flask
import logging
from logging.config import fileConfig
import requests

app = flask.Flask(__name__)

app.config["DEBUG"] = True

URL = "https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases"

@app.route('/', methods=['GET'])
def home():
    response = requests.get(url = URL)
    data = response.json()

    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    logger.disabled = False

    logger.debug("Some debugging message")
    logger.info('Info level log')
    logger.warning('Warning level log')

    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0")