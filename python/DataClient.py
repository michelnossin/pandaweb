#!/data/anaconda3/bin/python
#This is just some werkzeug client which you can use from the commandline to test the backend!
import requests
import json

my_server = "localhost"
my_port = 8080

def main():
    url = "http://" + str(my_server) + ":" + str(my_port) + "/data"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "search_text",
        "params": ["myquery"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print ("response is:" + str(response))
    print ("result json is:" + str(response['result']))

if __name__ == "__main__":
    main()
