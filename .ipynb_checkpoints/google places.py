import requests
from tkinter import *
from tkinter import ttk
#api = AIzaSyBhxkX-tvhGNEPtVRw272V5LIolba9FYSc
"""
resp = requests.get("https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Lu&types=(cities)&language=ENG&key=AIzaSyBhxkX-tvhGNEPtVRw272V5LIolba9FYSc")

json = resp.json()
city = json["predictions"]
print(json)
print(city)

cityList=[]
for data in city:
    cityList.append(data['structured_formatting']['main_text'])
for i in cityList:
    print(i)
"""
root = Tk()
city = Label(root,text="Enter city")
city.pack()
ent = Entry(root)
ent.pack()
def activatePlacesSearch():
        inp = ent.get()
        autocomplete = google.maps.places.Autocomplete(inp)

resp = requests.get("https://maps.googleapis.com/maps/api/js?key=AIzaSyBhxkX-tvhGNEPtVRw272V5LIolba9FYSc&libraries=places&callback=activatePlacesSearch")
print(resp)
combo = ttk.Combobox(root)
combo['values']=resp
combo.pack()
root.config(background="#33E6FF",padx=100,pady=100)
root.mainloop()






