"""Model for the uweb3 test server"""

from uweb3 import model

class SignedExample(model.SecureCookie):
  """Model for the Singed Cookie example"""

class Fish(model.Record):
  """Model for the Sqlite example"""
  _CONNECTOR = 'sqlite'

class Tank(model.Record):
  """Model for the Mysql example"""

class Posts(model.Record):
  """Model for the Mysql example"""
  _CONNECTOR = 'restfulljson'

class Albums(model.Record):
  """Model for the Mysql example"""
  _CONNECTOR = 'restfulljson'
