from flask import Flask
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)

@app.route("/")
def hello_world():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return "<p>Hello, World!</p>"

from view import routes

if __name__ == '__main__':
  app.run()