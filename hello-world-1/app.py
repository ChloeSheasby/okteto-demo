import os
import pydevd_pycharm
from flask import Flask
import socket
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello_world():
  with urllib.request.urlopen('https://hello-world-2-service-chloesheasby.cloud.okteto.net/tap2') as res:
    response = str(res.read())

  msg = 'Hello World! This message is coming from ' + socket.gethostname() + ' ' + response

  return msg

@app.route('/tap1')
def tap1():
  return "You have reached hello-world-1! My host name is " + socket.gethostname()

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('0.0.0.0', port=9000, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  print('Starting hello-world-1 server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)