from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    port_num = os.getenv("PORT")
    return jsonify({"Choo Choo": f'PORT:{port_num}'})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
