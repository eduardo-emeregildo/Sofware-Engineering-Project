from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from  kivy.uix.widget import Widget
import requests
import pyrebase
#ask team about storing rep_score as soon as someone signs in
#ask team if they want to store pwd in db

#dictionary containing data to connect to firebase
config = {					
	"apiKey": "AIzaSyA3jmvr2W79q49qKP3-Meya2U6yMb9Prtk",
	"authDomain": "csc322-project.firebaseapp.com",
	"databaseURL": "https://csc322-project.firebaseio.com",
	"projectId": "csc322-project",
	"storageBucket": "csc322-project.appspot.com",
	"messagingSenderId": "1010821296449",
	"appId": "1:1010821296449:web:3bb6c7c6fd51f0024631c0",
	"measurementId": "G-B97101DQ0C"
	}

def sign_up():
	firebase = pyrebase.initialize_app(config)
	name = input("Enter your name ")
	email = input("Enter your email ")
	pwd = input("Enter your password ")
	reference = input("Enter the email of the reference ")
	priv = 0  				   # initilaized to 0 when you first sign up. 0 is OU,1 is VIP, 2 is SU
	db = firebase.database()   # databse object to deal wih db operations
	auth = firebase.auth()	   #authentication object to deal auth operations

	data = {
	"name": name,
	"email":email,
	"password":pwd,
	"reference":reference,
	"priviledge":priv
	}

	try:
		auth.create_user_with_email_and_password(email,pwd)
		print("data added to authentication")
		db.child("users").push(data)
		print("data added to db")
	except requests.exceptions.HTTPError:
		print("invalid another email or password.(Passwords must be at least 6 characters long)")



def log_in():
	firebase = pyrebase.initialize_app(config)
	email = input("Enter your email ")
	password = input("Enter your password ")
	auth = firebase.auth()
	try:
		auth.sign_in_with_email_and_password(email,password)
		print("Success")
	except:
		print("you have entered wrong email or password")


def get_key(email): #returns key in db given the existing email of user in the system
	firebase= pyrebase.initialize_app(config)
	db = firebase.database()
	all_users = db.child("users").get() 

	for users in all_users.each():
		a=users.val()
		if a['email'] == email:
			return users.key()
			


def delete_record_db(key): #deletes user from db given their corresponding key
	firebase= pyrebase.initialize_app(config)
	db = firebase.database()
	db.child("users").child(key).remove() #key has to be given
	print("user removed")



#delete_record_db(get_key("jdoe@gmail.com"))
#sign_up()
#log_in()
# a = get_key("maria@gmail.com")
# print(a)

#graphics stu
class MainApp(App):
    def build(self):
        return GridLayout()

MainApp().run()
