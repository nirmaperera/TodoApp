from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
import requests
import json
import os


# creates a Flask application, named app
app = Flask(__name__)

global myCookie

# the profile(Home) route.
@app.route("/")
def home():
    return render_template('index.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['username']:
            username = request.form['username']
            r = requests.post('https://hunter-todo-api.herokuapp.com/user',
                              data=json.dumps({'username': username}))

            r = requests.post('https://hunter-todo-api.herokuapp.com/auth',
                              data=json.dumps({'username': username}))
            cookie = r.json()
            value = cookie['token']
            print(value)

            resp = make_response(redirect('/todo'))
            resp.set_cookie('sillyauth', value)
            return resp

    return render_template('register.html')

# the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username']:
            username = request.form['username']
            r = requests.post('https://hunter-todo-api.herokuapp.com/auth',
                              data=json.dumps({'username': username}))
            cookie = r.json()
            value = cookie['token']
            print(value)

            resp = make_response(redirect('/todo'))
            resp.set_cookie('sillyauth', value)
            return resp

    return render_template('login.html')

# the todo route
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    myCookie = request.cookies.get('sillyauth')
    c = {'sillyauth': myCookie}

    # ACCESS TODOS FOR USER
    url2 = 'https://hunter-todo-api.herokuapp.com/todo-item'
    r = requests.get(url2, cookies=c)
    todo = r.json()
    # print(r.json())
    return render_template('todo.html', todos=todo)


# # the todo route
@app.route('/add', methods=['GET', 'POST'])
def get_a_todo():

    if request.method == 'POST':
        myCookie = request.cookies.get('sillyauth')
        c = {'sillyauth': myCookie}
        if request.form['TODO']:
            myTodo = request.form['TODO']
            payload = {'content': myTodo}
            print(myTodo)
            r = requests.post(
                'https://hunter-todo-api.herokuapp.com/todo-item', json=payload, cookies=c)

            url2 = 'https://hunter-todo-api.herokuapp.com/todo-item'
            r = requests.get(url2, cookies=c)
            todo = r.json()
            return redirect(url_for('todo', todos=todo))
    return render_template('todo.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():

    if request.method == 'POST':
        myCookie = request.cookies.get('sillyauth')
        c = {'sillyauth': myCookie}
        item_id = request.form['todoId']

        url = "https://hunter-todo-api.herokuapp.com/todo-item/"+item_id
        r = requests.delete(
            url,  cookies=c)
        return redirect(url_for('todo'))
    else:
        return render_template('todo.html')


@app.route('/complete', methods=['GET', 'POST'])
def completed():

    if request.method == 'POST':
        myCookie = request.cookies.get('sillyauth')
        c = {'sillyauth': myCookie}
        item_id = request.form['todoId']
        payload2 = {'completed': True}
        url = "https://hunter-todo-api.herokuapp.com/todo-item/"+item_id

        r = requests.put(
            url, json=payload2, cookies=c)
        return redirect(url_for('todo'))
    else:
        return render_template('todo.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():

    if request.method == 'POST':
        item_id = request.form['logout']
        return redirect(url_for('login'))
    else:
        return render_template('todo.html')


# run the application
if __name__ == "__app__":
    app.run(debug=True)
