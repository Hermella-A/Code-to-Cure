# # from flask import Flask, redirect, render_template, request, session
# # from app import app
# # from pymongo import MongoClient
# # from flask import Flask, render_template, request, session, redirect
# # from app import app
# # from pymongo import MongoClient
# # import bcrypt

# # # Replace the placeholder value with your MongoDB Atlas connection string
# # client = MongoClient('mongodb+srv://pojectz:admin1234@cluster0.0yqmce2.mongodb.net/?retryWrites=true&w=majority')
# # accounts_db = client.get_database('sitota')
# # users = accounts_db.user_data
# # # Set the secret key for the session
# # app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# # req = request.form

# # # Route for the registration page
# # @app.route("/register", methods=["GET", "POST"])
# # def register():
# #     if request.method == "POST":
# #       # Get the data from the form
# #       userName = req['username']
# #       password =req['password'].encode()

# #       # Hash the password using bcrypt
# #       hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# #       # Store the data in the MongoDB collection
# #       newUser = {
# #           'Username': userName,
# #           'password': hashed_password
# #       }
# #       users.insert_one(newUser)

# #       # Redirect the user to the login page
# #       return redirect("public/login.html")

# #     # Render the registration page
# #     return render_template("admin/register.html")

# # Route for the login page
# @app.route("/login", methods=["GET", "POST"])
# def login():
#   if request.method == "POST":
#     req = request.form
#     # Get the data from the form
#     username = req['username']
#     password = req['password'].encode()

#     # Find the user in the MongoDB collection
#     user = users.find_one({"username": username})

#     # Check if the user exists and the password is correct
#     if user and bcrypt.checkpw(password, user["password"]):
#       # Store the user's data in the session
#       session["user"] = user

#       # Redirect the user to the homepage
#       return redirect("/admin")

#     # If the login is invalid, return an error message
#     return "Invalid username or password"

#   # Render the login page
#   return render_template("public/login.html")

# # # Route for the homepage
# # @app.route("/admin")
# # def admin():
# #     # Check if the user is logged in
# #     if "user" in session:
# #         # Render the homepage
# #         return render_template("admin/admin.html", username=session["user"]["username"])

# #     # If the user is not logged in, redirect them to the login page
# #     return redirect("/login")
#here bro
#don't worry I only need the code
# what about this file ??
#just paste it down here
#tnx man

from flask import Flask, render_template, request, redirect, url_for
from app import app
from pymongo import MongoClient

client = MongoClient(
  'mongodb+srv://pojectz:admin1234@cluster0.0yqmce2.mongodb.net/?retryWrites=true&w=majority'
)
db = client.get_database('ps')

patient_records = db.patient_info
booked_patients = db.booked_patients

all = []
id = []
count_records = 0

for i in booked_patients.find({}, {'_id': 0}):
  ld = i
  all.append(ld)
  count_records += 1
  id.append(count_records)

count_dict = 0
for j in all:
  j['id'] = id[count_dict]
  count_dict += 1


@app.route('/admin')
def admin():
  return render_template('admin/admin.html', all=all, id=id, count=count_dict)


@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == "POST":
    req = request.form

    username = req['name']
    Fname = req['fname']
    Gname = req['Gname']

    ph_no = req['phno']
    city = req['city']

    newPatient = {
      'Name': username,
      'Father name': Fname,
      'Grand father name': Gname,
      'Phone Number': ph_no,
      'City': city,
    }
    patient_records.insert_one(newPatient)

    return redirect(url_for('reg_success'))

  return render_template('admin/register.html')


@app.route('/appointment', methods=['GET', 'POST'])
def appoint():
  if request.method == "POST":
    req = request.form

    fullName = req['fullName']
    phone_number = req['phno']
    sex = req['sex']
    doctor = req['doctors']
    date = req['date']
    time = req['time']

    bookedPatient = {
      'Full Name': fullName,
      'Phone Number': phone_number,
      'Sex': sex,
      'Doctor': doctor,
      'Date': date,
      'Time': time
    }
    booked_patients.insert_one(bookedPatient)
    db['_update']
    return redirect(url_for('ap_success'))
  return render_template('admin/appointment.html')
