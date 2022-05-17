import requests 
import tkinter 
from tkinter import *
import dogfacts 
import image
import urllib.request, json
from PIL import ImageTk, Image

def Dogfacts():
  win= Tk()
  win.title("Dog Facts!")
#Set the geometry
  win.geometry("750x700")

#Create a canvas object
  canvas= Canvas(win, width= 750, height= 700, bg="blue")

#Add a text in Canvas
  quotes = dogfacts.Facts()
  response = quotes.get()
  #Positions Text
  canvas.create_text(370, 50, text= (response.json()["facts"]), fill="black", font=('Courier 7 bold'))
  canvas.pack()


  x = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random/dog")
  data = json.loads(x.read())
  ok = data["status"] == "success"
  imgurl = data["message"][0] if ok else None
  print(imgurl)

  urllib.request.urlretrieve(imgurl, "dog.jpg")
  img = ImageTk.PhotoImage(Image.open("dog.jpg"))
  canvas.create_image(50, 70, anchor=NW, image=img)
  canvas.pack()

  win.mainloop()



def main():
  Dogfacts()

main()