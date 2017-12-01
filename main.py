from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return render_template('hello_greeting.html' , name=first_name)

@app.route('/validate-time')
def display_time_form():
    return render_template('time_form.html')

tasks = []

@app.route('/todos' , methods=['POST' , 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    if request.method == 'GET':
        tasks = []
        
    return render_template('todos.html', title="TODOs" , tasks=tasks)


app.run()
