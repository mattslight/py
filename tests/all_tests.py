import json
from urllib.request import urlopen, Request
from flask import Flask
from flask_testing import LiveServerTestCase
from urllib.error import URLError, HTTPError

class MyTest(LiveServerTestCase):

  def create_app(self):
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['LIVESERVER_PORT'] = 8943
    return app

  def test_flask_application_is_up_and_running(self):
    print(self.get_server_url())
    req = Request(self.get_server_url())
    req.add_header('user-agent', 'Mozilla/5.0')
    try:
      response = urlopen(req)
    except HTTPError as e:
      self.assertEqual(e.code, 404) 
    else:
      self.assertEqual(response.code, 200) 
