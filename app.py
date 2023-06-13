from flask import Flask, render_template, request, jsonify
from flask_caching import Cache
import requests

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

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

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/api')
def api():
    return render_template('apidocs.html')

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.101')