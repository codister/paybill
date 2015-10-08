#PYTHON 3.4
import requests
import json
import base64
import hashlib
import time
import hmac

bitfinexURL = 'https://api.bitfinex.com/v1/deposit/new'
bitfinexKey = 'J4HZgO4DWeKDV9el4NcGcuHPRsOXzOSpGhczVyzpBSM'
bitfinexSecret = b'C9Jl818rNbUUzoOKAsoEYIBUdy8kBQLM0uRmZLAP1zL' #the b is deliberate, encodes to bytes

def start():
    payloadObject = {
            'request':'/v1/deposit/new',
            'nonce':str(time.time() * 100000), #convert to string
            'method':'bitcoin',
            'wallet_name':'deposit',
            'renew':1
    }

    payload_json = json.dumps(payloadObject)

    payload = base64.b64encode(bytes(payload_json, "utf-8"))


    m = hmac.new(bitfinexSecret, payload, hashlib.sha384)
    m = m.hexdigest()

    #headers
    headers = {
          'X-BFX-APIKEY' : bitfinexKey,
          'X-BFX-PAYLOAD' : base64.b64encode(bytes(payload_json, "utf-8")),
          'X-BFX-SIGNATURE' : m
    }

    r = requests.get(bitfinexURL, data={}, headers=headers)
    bit_data = r.json()
    return bit_data['address']['address']
