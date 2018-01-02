# -*- coding: utf-8 -*-

import requests, json

def send_message(recommendations):

    try:

        data = "\n".join(recommendations)
        slack_data = {"text" : data}
        webhook_url = "https://hooks.slack.com/services/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"
        response = requests.post(webhook_url, data=json.dumps(slack_data), headers={"Content-Type":"application/json"})

        if response.status_code != 200:
             raise ValueError("Request to slack returned an error %s the response is: \n%s" %(response.status_code, response.text))
    except:
        print("Error in Communicator: Could not send message")
        pass