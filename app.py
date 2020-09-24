from flask import Flask
import requests
import re

app = Flask(__name__)

@app.route("/")
def ip_addr():
    ip = requests.get("http://httpbin.org/ip").text
    ip_2 = re.findall('origin": "(.*)"',ip)
    return ip_2[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0")
