from PubApi import app, cache, db
from PubApi.models import Submit_data
from flask import render_template, request, jsonify, flash, redirect, url_for
import requests


@cache.cached()
def api_call():
    url = 'https://api.publicapis.org/entries'
    data = requests.get(url).json()['entries']
    url = 'https://api.publicapis.org/categories'
    categories = requests.get(url).json()['categories']
    return data,categories

@app.route('/get_data',methods=['GET'])
def get_data():
    data,_ = api_call()
    page = request.args.get('page',1,type=int)
    per_page = 50
    start_index = (page - 1) * per_page
    print(start_index)
    end_index = start_index + per_page
    paginated_data = data[start_index:end_index]
    return jsonify({'data': paginated_data})

@app.route('/filter',methods=['GET'])
def filter():
    cate = request.args.get('cate','',type=str)
    data, _ = api_call()
    filter_data = []
    for item in data:
        if item['Category'] == cate:
            filter_data.append(item)
    return jsonify({'data':filter_data})


@app.route('/')
def home():
    _ , categories = api_call()
    return render_template('home.html',categories=categories)

@app.route('/random')
def random():
    url = 'https://api.publicapis.org/random'
    data = requests.get(url).json()['entries'][0]
    return render_template('random.html',data=data)

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        api_email = request.form['api_email']
        api_name = request.form['api_name']
        api_desc = request.form['api_desc']
        api_auth = request.form['api_auth']
        api_https = bool(request.form.getlist('api_https'))
        api_cors = bool(request.form.getlist('api_cors'))
        api_link = request.form['api_link']
        api_category = request.form['api_category']
        try:
            data = Submit_data(api_email=api_email,api_name=api_name,api_desc=api_desc,api_auth=api_auth,api_https=api_https,api_cors=api_cors,api_link=api_link,api_category=api_category)
            db.session.add(data)
            db.session.commit()
            flash('The form has been submitted. We will let you know if the api is add or not by the email provided by you. Thanks for your contribution')
        except :
            flash('There was an error. Feel free to submit again')
        return redirect(url_for('submit'))
