from django.shortcuts import render
import pyrebase
import pandas as pd
config = {
  "apiKey": "AIzaSyBbtURa7On-Q3N32PILG_eQsDHsbDymdjA",
  "authDomain": "db78-36a53.firebaseapp.com",
  "databaseURL": "https://db78-36a53.firebaseio.com",
  "storageBucket": "db78-36a53.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db=firebase.database()

# Create your views here.

def details(request):
     
        users = db.get().val()
        a=[]
        a=list(users.values())
        c= {}
        c=a[0]
        print(c.values)
        d,e=c.values()
        data={"temp":d,"humi":e}

        return render(request,'details/details.html',data)
