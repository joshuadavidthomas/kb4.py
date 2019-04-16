class KnowBe4Exception(Exception):
  pass

class ConfigurationError(KnowBe4Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg

class HTTPError(KnowBe4Exception):
  def __init__(self, message, code):
    self.status_code = code
    self.msg = '{}: {}'.format(code, message)

  def __str__(self):
    return self.msg