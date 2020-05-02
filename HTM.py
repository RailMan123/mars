import random
import sys
import requests
import pygame
import os
import math
from flask import Flask, url_for, render_template, request, json

app = Flask(__name__)
params = {}
car_imgs = ['mars1.jpeg', 'mars2.jpeg', 'mars3.jpg', 'mars2.jpg']


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


@app.route('/table/<category>/<int:age>', methods=["GET", "POST"])
def customize(category, age):
    print(category, age)
    return render_template('customize.html', params=[age, category])


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


@app.route('/galery', methods=['POST', 'GET'])
def carousel():
    global car_imgs
    if request.method == 'GET':
        return render_template('carousel.html', title='Красная планета', car_imgs=car_imgs, count=len(car_imgs))

    elif request.method == 'POST':
        f = request.files['file']
        map_file = f"static/img/mars{len(car_imgs) + 1}.jpg"
        with open(map_file, "wb") as file:
            file.write(f.read())
        car_imgs.append(f'mars{len(car_imgs) + 1}.jpg')
        return render_template('carousel.html', title='Красная планета', car_imgs=car_imgs, count=len(car_imgs))


@app.route('/member', methods=['POST', 'GET'])
def member_card():
    with open("templates/members.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        data = data["all_members"][random.randint(0, len(data['all_members']) - 1)]
        name = data["name"] + ' ' + data["surname"]
        photo = data["photo"]
        prof = sorted(data["professions"])
    return render_template('member_card.html', datas=[name, photo, ", ".join(prof)])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
