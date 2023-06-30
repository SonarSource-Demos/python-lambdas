import simpledb
from flask import Flask
app = Flask(__name__)


app.add_url_rule('/simpledb/safe1', view_func=simpledb.safe1)
app.add_url_rule('/simpledb/vuln1', view_func=simpledb.vuln1)
app.add_url_rule('/simpledb/vuln2', view_func=simpledb.vuln2)
