from flask import render_template
from flask import Flask, render_template, request, url_for, redirect
from generate_menus import generate_all_menus
from trainer import train_bot, get_bot

app = Flask(__name__)

app.static_folder = 'static'

trainer = train_bot()
bot = get_bot()
obj1_menu, obj2_menu, obj3_menu, obj4_menu = generate_all_menus()
@app.route('/', methods=['GET'])
def index():
    main_options = ['Objetivo 1. Ciencia, innovación y desafíos locales: Un análisis integral de Caldas','Objetivo 2. Ampliando capacidades colectivas en los territorios para participar en CTeI a partir de procesos formativos','Objetivo 3. Indicadores para el sistema CTeI de las subregiones de Caldas','Objetivo 4. Ciencia, innovación y desafíos locales: Un análisis integral de Caldas']
    source='home'
    return render_template('index.html', main_menu=main_options,source=source)

@app.route('/response/<int:option>/<string:source>')
def response(option,source):
    if option == 1:
        return render_template('questions_obj1.html', menu=obj1_menu, source='obj1')
    elif option == 2:
        return render_template('questions_obj2.html', menu=obj2_menu, source='obj2')
    elif option == 3:
        return render_template('questions_obj3.html', menu=obj3_menu, source='obj3')
    else:
        return render_template('questions_obj4.html', menu=obj4_menu, source='obj4')

@app.route('/response_one/<int:option>/<string:source>/<string:item>')
def response_one(option,source,item):
    answer = bot.get_response(item)
    return render_template('chat_response.html',source='obj1',answer=answer)

@app.route('/response_two/<int:option>/<string:source>/<string:item>')
def response_two(option,source,item):
    answer = bot.get_response(item)
    return render_template('chat_response.html',source='obj2',answer=answer)

@app.route('/response_three/<int:option>/<string:source>/<string:item>')
def response_three(option,source,item):
    answer = bot.get_response(item)
    return render_template('chat_response.html',source='obj3',answer=answer)

@app.route('/response_four/<int:option>/<string:source>/<string:item>')
def response_four(option,source,item):
    answer = bot.get_response(item)
    return render_template('chat_response.html',source='obj4',answer=answer)
    
@app.route('/back')
def go_back():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
