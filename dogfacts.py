import requests 

class Facts:
  def __init__(self):
    self.api_url = "http://dog-api.kinduff.com/api/facts"

  def get(self):
    reqs = requests.get(self.api_url)
    return reqs

