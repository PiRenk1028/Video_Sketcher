import socket
import time
import json
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#client.sendto(str(time.time_ns()).encode(),("127.0.0.1",9999))

import flask

app = flask.Flask(__name__,template_folder='templates')

##def threaded(function):
##    threading.Thread(target=function).start()

##@threaded
@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        data = flask.request.get_json()
        client.sendto(json.dumps(data).encode(),("127.0.0.1",9999))
        
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = False)
