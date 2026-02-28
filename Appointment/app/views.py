from flask import Flask, render_template, request, redirect, url_for
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
  req = request.form
  amh = req.get('Amh')
  en = req.get('En')
  if request.method == "POST":
    if amh == 'Amharic':
      return redirect(url_for('amh_home'))
    if en == 'English':
      return redirect(url_for('home'))

  return render_template('chooseLang.html')


@app.route('/home')
def home():
  return render_template('public/home.html')


@app.route('/Amh_home')
def amh_home():
  return render_template('public/Amh_home.html')



# Route for English registered success


@app.route('/registered_success')
def reg_success():
  return render_template('public/registered_success.html')


# Route for Amharic registered scuccess


@app.route('/Amh_registered_success')
def amh_reg_success():
  return render_template('public/Amh_registered_success.html')


# Route for English apponintment success


@app.route('/appoint_success')
def ap_success():
  return render_template('public/appoint_success.html')


# Route for Amharic apponintment success


@app.route('/Amh_appoint_success')
def amh_ap_success():
  return render_template('public/Amh_appoint_success.html')
