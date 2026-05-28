from flask import Flask
import os
import random
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    logger.info("Home page accessed")
    return f"Hello DevOps! Version: 2.0. Random: {random.randint(1,100)}"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
