import requests
from requests.auth import HTTPBasicAuth
import json
import os1
import boto
debug = False
paypal_url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
headers = {'Accept': 'application/json', 'Accept-Language': 'en_US', 'content-type': 'application/x-www-form-urlencoded'}
params = {'grant_type': 'client_credentials'}
response = requests.post(paypal_url, headers = headers, params = params, auth = HTTPBasicAuth(paypal_userid, paypal_secret))

this is response text