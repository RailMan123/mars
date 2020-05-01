import sys
import requests
import pygame
import os
import math
from flask import Flask, url_for, render_template, request

app = Flask(__name__)
params = {}

@app.route('/<title_name>')
@app.route('/index/<title_name>')
def index(title_name):
    return render_template('base.html', title=title_name)


@app.route('/training/<prof>')
def Profession(prof):
    return render_template('base2.html', prof=prof.lower())


@app.route('/distribution')
def Distrib():
    profs = ['Ридли Скотт', 'Энди Уир', 'Верката Капур', 'Тедди Сандерс', 'Шон Бин', 'Марк Уотни']
    return render_template('spisok.html', profs=profs)




@app.route('/answer')
def answer():
    return render_template('answer.html', **params)


@app.route('/auto_answer', methods=['POST', 'GET'])
def auto_answer():
    if request.method == 'GET':
        return render_template('auto_answer.html')
    elif request.method == 'POST':
        params["title"] = request.form['title']
        params["surname"] = request.form['surname']
        params["name"] = request.form['name']
        params["education"] = request.form['education']
        params["profession"] = request.form['profession']
        params["sex"] = request.form['sex']
        params["motivation"] = request.form['motivation']
        if request.form['accept'] == 'on':
            params["ready"] = 'True'
        else:
            params['ready'] = 'False'
        return "Отправлено, теперь перейдите на /answer"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')