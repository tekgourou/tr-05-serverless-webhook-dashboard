from flask import Flask
from flask import request
import json

app = Flask(__name__)

# here is how we are handling routing with flask:

def index():
    return '<h1>Flask Receiver App is Up!</h1>', 200


@app.route('/webhook', methods=['POST'])  # create a route for /webhook, method POST
def webhook():
    if request.method == 'POST':
        print('Webhook Received')
        request_json = request.json

        # print the received notification
        print('Payload: ')
        # Change from original - remove the need for function to print
        print(json.dumps(request_json,indent=4))

        return 'Webhook notification received', 202
    else:
        return 'Only POST Method supported', 405

# include this for local dev

if __name__ == '__main__':
    app.run()