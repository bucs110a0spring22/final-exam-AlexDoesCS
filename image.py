import requests
import tkinter 
import urllib.request
from PIL import ImageTk,Image 

class Images:
  def __init__(self):
    self.api_url = (urllib.request.urlretrieve("https://dog.ceo/api/breeds/image/random/dog"))

  def get(self):
    reqs = requests.get(self.api_url)
    return reqs

  def response(self):
    request = self.get()
    response = request.json()
    return response



  

