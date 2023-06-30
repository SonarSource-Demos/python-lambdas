import rds
from flask import Flask
app = Flask(__name__)


app.add_url_rule('/rds-data/vuln1', view_func=rds.vuln1)
app.add_url_rule('/rds-data/vuln2', view_func=rds.vuln2)
app.add_url_rule('/rds-data/safe1', view_func=rds.safe1)
app.add_url_rule('/rds-data/safe2', view_func=rds.safe2)
