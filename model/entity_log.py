from log import db
from datetime import datetime


class Log(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    data_oper = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_oper = db.Column(db.String(length=100))
    operacao  = db.Column(db.String(length=100))
    args      = db.Column(db.String(length=100))
