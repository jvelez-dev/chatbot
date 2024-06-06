"""
Flask web application for interacting with a chatbot and navigating through different objectives.

Routes:
    - '/' (GET): Renders the main page with menu options for different objectives.
    - '/response/<int:option>/<string:source>' (GET): Renders pages with questions based on selected option.
    - '/response_one/<int:option>/<string:source>/<string:item>' (GET): Renders chatbot responses for objective 1.
    - '/response_two/<int:option>/<string:source>/<string:item>' (GET): Renders chatbot responses for objective 2.
    - '/response_three/<int:option>/<string:source>/<string:item>' (GET): Renders chatbot responses for objective 3.
    - '/response_four/<int:option>/<string:source>/<string:item>' (GET): Renders chatbot responses for objective 4.
    - '/back' (GET): Redirects to the main page.

Attributes:
    - app: Flask application instance.
    - trainer: Instance for training the chatbot.
    - bot: Instance of the chatbot.
    - obj1_menu, obj2_menu, obj3_menu, obj4_menu: Menu options for different objectives.

"""
from flask import render_template
from flask import Flask, render_template, request, url_for, redirect
from generate_menus import generate_all_menus
from trainer import train_bot, get_bot


app = Flask(__name__)

app.static_folder = 'static'

trainer = train_bot()
bot = get_bot()
obj1_menu, obj2_menu, obj3_menu, obj4_menu = generate_all_menus()

def convert_newlines_to_br(text):
    """
    Convert newlines to <br> tags for HTML rendering.
    """
    return text.replace('\n', '<br>').replace('\\n', '<br>')


@app.route('/', methods=['GET'])
def index():
    """
    Renders the main page with menu options for different objectives.
    """
    main_options = ['Objetivo 1. Ciencia, innovación y desafíos locales: Un análisis integral de Caldas','Objetivo 2. Ampliando capacidades colectivas en los territorios para participar en CTeI a partir de procesos formativos','Objetivo 3. Indicadores para el sistema CTeI de las subregiones de Caldas','Objetivo 4. Ciencia, innovación y desafíos locales: Un análisis integral de Caldas']
    source='home'
    return render_template('index.html', main_menu=main_options,source=source, newline_to_html=True)

@app.route('/response/<int:option>/<string:source>')
def response(option,source):
    """
    Renders pages with questions based on selected option.
    """
    if option == 1:
        return render_template('questions_obj1.html', menu=obj1_menu, source='obj1', newline_to_html=True)
    elif option == 2:
        return render_template('questions_obj2.html', menu=obj2_menu, source='obj2', newline_to_html=True)
    elif option == 3:
        return render_template('questions_obj3.html', menu=obj3_menu, source='obj3', newline_to_html=True)
    else:
        return render_template('questions_obj4.html', menu=obj4_menu, source='obj4', newline_to_html=True)

@app.route('/response_one/<int:option>/<string:source>/<string:item>')
def response_one(option,source,item):
    """
    Renders chatbot responses for objective 1.
    """
    answer = convert_newlines_to_br(bot.get_response(item).text)
    return render_template('chat_response.html',source='obj1',answer=answer, newline_to_html=True)

@app.route('/response_two/<int:option>/<string:source>/<string:item>')
def response_two(option,source,item):
    """
    Renders chatbot responses for objective 2.
    """
    answer = convert_newlines_to_br(bot.get_response(item).text)
    return render_template('chat_response.html',source='obj2',answer=answer, newline_to_html=True)

@app.route('/response_three/<int:option>/<string:source>/<string:item>')
def response_three(option,source,item):
    """
    Renders chatbot responses for objective 3.
    """
    answer = convert_newlines_to_br(bot.get_response(item).text)
    return render_template('chat_response.html',source='obj3',answer=answer, newline_to_html=True)

@app.route('/response_four/<int:option>/<string:source>/<string:item>')
def response_four(option,source,item):
    """
    Renders chatbot responses for objective 4.
    """
    answer = convert_newlines_to_br(bot.get_response(item).text)
    return render_template('chat_response.html',source='obj4',answer=answer, newline_to_html=True)
    
@app.route('/back')
def go_back():
    """
    Redirects to the main page.
    """
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
