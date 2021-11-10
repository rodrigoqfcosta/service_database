from datetime import datetime
from log import Base
from sqlalchemy import Column, Integer, String, DateTime


class Log(Base):
   def __init__(self, tipo_oper, operacao, args):
      self.tipo_oper = tipo_oper
      self.operacao  = operacao
      self.args      = args

   __tablename__ = 'log'

   id        = Column(Integer, primary_key=True, autoincrement='ignore_fk')
   data_oper = Column(DateTime(timezone=True), default=datetime.utcnow)
   tipo_oper = Column(String(length=100))
   operacao  = Column(String(length=100))
   args      = Column(String(length=100))
