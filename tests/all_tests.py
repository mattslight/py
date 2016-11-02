import json
from urllib.request import urlopen
from flask import Flask
from flask_testing import LiveServerTestCase

class MyTest(LiveServerTestCase):

  def create_app(self):
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['LIVESERVER_PORT'] = 8943
    return app

  def test_flask_application_is_up_and_running(self):
    print(self.get_server_url())
    response = urlopen(self.get_server_url())
    self.assertEqual(response.code, 200) 
