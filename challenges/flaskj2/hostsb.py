#!/usr/bin/python 3

from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)
app.secret_key = "playswithsquirrels"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        hostname1 = request.form.get("hostname")
        ip1 = request.form.get("ip")
        fqdn1 = request.form.get("fqdn")
        newgroup = {"hostname": hostname1, "ip": ip1, "fqdn": fqdn1}
        groups.append(newgroup)
        return "<a href='/'> Add more Here</a> or <a href='/host'>Finish</a>"
    else:
       return  render_template("post.html")
       
@app.route("/host")
def host():
    with open("newhosts.conf", "w") as hostList:

        for item in groups:
            print(item)
            hostitem = render_template("hosts.txt", **item)
            print(hostitem, file=hostList)
    return "newhosts.conf written"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port =2224)
