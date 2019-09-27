from flask import Flask, render_template
from plots import mpg, horsepower
from cleaning_data import data_mobil, data_ranking, data_ranking2
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data_mobil()
    return render_template('table_data.html', data= data)

@app.route('/plots') 
def plots():
    data = mpg()
    data2 = horsepower()
    return render_template('plots.html', data= data, data2= data2)

@app.route('/stats')
def stats():
    data = data_ranking()
    data2 = data_ranking2()
    return render_template('stats.html', data= data, data2 = data2)

# @app.route('/hello')
# def hello():
#     hasil = 9+2
#     return 'Ini Route Hello' + str(hasil)

# @app.route('/template')
# def template():
#     return render_template('contoh.html') # bikin foldernya harus 'templates' yee bray

# @app.route('/template-with-data')
# def template_with_data():
#     data ={
#         'name'  : 'Anugrah',
#         'name2' : 'Anya',
#         'name3' : 'luvly'
#     }
#     return render_template('data.html', nama =data) 


# @app.route('/template-with-data2')
# def template_with_data2():
#     data =['anugrah','anya','cayo']
#     return render_template('data2.html', nama =data, panjang =len(data)) # ini bisa langsung di ambil bray setiap indexnya yaaa 

if __name__ == '__main__':
    app.run(debug=True, port=5000)