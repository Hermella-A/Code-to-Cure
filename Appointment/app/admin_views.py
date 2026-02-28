from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import bcrypt

from app import app

client = MongoClient(
  'mongodb+srv://pojectz:admin1234@cluster0.0yqmce2.mongodb.net/?retryWrites=true&w=majority'
)
patient_db = client.get_database('ps')
accounts_db = client.get_database('accounts')
staff_rec = accounts_db.staff_info
patient_records = patient_db.patient_info
booked_patients = patient_db.booked_patients
users = accounts_db.user_data
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# the success route
@app.route('/success')
def success():
  return render_template('public/success.html')


@app.route('/admin')
def admin():
  if "user" in session:
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
  else:
    return redirect(url_for('login'))
  return render_template('admin/admin.html', all=all, id=id, count=count_dict)


@app.route('/admin/staffreg', methods=['GET', 'POST'])
def staffreg():
  if "user" in session:
    if request.method == "POST":
      req = request.form

      name = req['name']
      Fname = req['fname']
      Gname = req['Gname']

      ph_no = req['phno']
      city = req['city']
      title = req['title']
      role = req['role']
      # Halle added the username and password variable
      email = req['email'].lower()
      username = req['username'].lower()
      password = req['password']

      user_found = staff_rec.find_one({"username": username})
      email_found = staff_rec.find_one({"email": email})
      if user_found:
        message = "Username already exisits use another"
        return render_template('admin/staffreg.html', message=message)
      elif email_found:
        message = "Email already exisits in the databse use another email"
        return render_template('admin/staffreg.html', message=message)
      else:
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        newStaff = {
          'Name': name,
          'Father name': Fname,
          'Grand father name': Gname,
          'Phone Number': ph_no,
          'City': city,
          'Role': role,
          'Title': title,
          'Email': email,
          'username': username,
          'password': hashed
        }
        # dedicated dictionary for password and username storage
        staffAcc = {'email': email, 'username': username, 'password': hashed}
        staff_rec.insert_one(newStaff)
        users.insert_one(staffAcc)
        return redirect(url_for('admin'))

    return render_template('admin/staffreg.html')
  else:
    return redirect(url_for('login'))


# bro what went wrong??
# the database name i'm changeing it wait
# Route for English registeration page
#owk


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
    patient_db['_update']
    return redirect(url_for('reg_success'))

  return render_template('admin/register.html')


# Route for amharic registeration page


@app.route('/Amh_register', methods=['GET', 'POST'])
def Amh_register():
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
    patient_db['_update']
    return redirect(url_for('amh_reg_success'))

  return render_template('admin/Amh_register.html')


# Route for English appointment page


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
    patient_db['_update']
    return redirect(url_for('ap_success'))
  return render_template('admin/appointment.html')


# Route for amharic appointment page


@app.route('/Amh_appointment', methods=['GET', 'POST'])
def amh_appoint():
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
    patient_db['_update']
    return redirect(url_for('amh_ap_success'))
  return render_template('admin/Amh_appointment.html')


@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    req = request.form
    username = req['username'].lower()
    password = req['password'].encode('utf-8')
    user = users.find_one({"username": username})
    if user:
      if bcrypt.checkpw(password, user['password']):
        session["user"] = username
        return redirect("/admin")
      else:
        return "Invalid username or password"
    else:
      return "Username not found"
  return render_template("public/login.html")


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   return render_template('public/login.html')
