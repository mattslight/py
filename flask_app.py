#!/usr/bin/env python3
from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def main():
    API_KEY = "231506b67b2f31242d542c0de6287cd3"
    PASSWORD = "***REMOVED***"
    REQ_URL = "https://prosfx.myshopify.com"
    REQ_GET_ORDER = "/admin/orders.json"
    REQ_PUT_ORDER =  "/admin/orders/%s.json" # %s should be order id
    TAG = "Quote" #tag to check for and add
    STATUS = 0

    resp = requests.get(REQ_URL + REQ_GET_ORDER, auth=(API_KEY, PASSWORD))
    orders_data = json.loads(resp.text)

    #iterate orders over dict obj
    for order in orders_data['orders']:
        if order['gateway'] == "Quotation Only": #check if payment gateway matches 'Quotation Only'
            if(TAG not in order['tags']):
                if (order['tags']):
                    TAGS = order['tags'] + (", %s" % TAG)
                else:
                    TAGS = TAG

                PAYLOAD = '{"order": {"id": "%s", "tags": "%s"}}' % (order['id'], TAGS)

                r_url=(REQ_URL + (REQ_PUT_ORDER % order['id']))
                r_headers = {'Content-Type': 'application/json'}

                r = requests.put(url=r_url, data=PAYLOAD, auth=(API_KEY, PASSWORD), headers=r_headers)
                STATUS = r.status_code
    return ("Status %s" % STATUS)
