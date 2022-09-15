from flask import Flask, request, json
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command')
args = parser.parse_args()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'deploy-to-cms'


@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    with open('temp.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

    subprocess.Popen(['bash', args.command])

    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
