import json
from urllib.request import urlopen
from flask import Flask
from flask_testing import LiveServerTestCase

class MyTest(LiveServerTestCase):

  def create_app(self):
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

  def test_flask_application_is_up_and_running(self):
    response = urlopen(self.get_server_url())
    self.assertEqual(response.code, 200) 
