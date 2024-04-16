from flask import Flask, render_template, request
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

nlp = spacy.load("es_core_news_sm")

# Crear una instancia del chatbot
bot = ChatBot('DataGovernor', preprocessors=['chatterbot.preprocessors.clean_whitespace', 'chatterbot.preprocessors.unescape_html'], storage_adapter="chatterbot.storage.SQLStorageAdapter", logic_adapters=["chatterbot.logic.BestMatch", "chatterbot.logic.TimeLogicAdapter"], spacy_language=nlp)

# Datos de entrenamiento
datos_entrenamiento = [
    {
        'texto': "El proyecto 'Plataforma Piloto para el Fortalecimiento de Procesos de Gobernanza en el Sistema de CTeI con Estrategias Participativas, Descentralizadas, Basadas en Datos y en las Capacidades Científicas, Tecnológicas y de Innovación en las Subregiones de Caldas' tiene como objetivo principal mejorar la gobernanza en el campo de la Ciencia, Tecnología e Innovación (CTeI) en Caldas.",
        'preguntas_respuestas': [
            {"pregunta": "¿Cuál es el objetivo principal del proyecto?", "respuesta": "El objetivo principal es mejorar la gobernanza en el campo de la Ciencia, Tecnología e Innovación (CTeI) en Caldas."},
            {"pregunta": "¿Cuál es el alcance geográfico del proyecto?", "respuesta": "El proyecto se centra en las subregiones de Caldas."},
            {"pregunta": "¿Qué estrategias se utilizan para fortalecer los procesos de gobernanza en el ámbito de la CTeI?", "respuesta": "Se utilizan estrategias participativas, descentralizadas, basadas en datos y en las capacidades científicas, tecnológicas y de innovación."}
        ]
    },
    {
        'texto': "Para ello, contamos con un equipo de desarrollo compuesto por 13 personas, que incluye una diseñadora visual, 2 estudiantes de semillero de la Facultad de Ingeniería de la Universidad de Caldas y el resto ingenieros. Este equipo se divide en tres subdivisiones: el equipo base, los módulos complementarios y los asesores.",
        'preguntas_respuestas': [
            {"pregunta": "¿Cuántas personas componen el equipo de desarrollo del proyecto?", "respuesta": "El equipo de desarrollo está compuesto por 13 personas."},
            {"pregunta": "¿Qué disciplinas o roles específicos están representados en el equipo de desarrollo?", "respuesta": "Incluye una diseñadora visual, 2 estudiantes de semillero de la Facultad de Ingeniería de la Universidad de Caldas, y el resto son ingenieros."},
            {"pregunta": "¿Cómo se divide el equipo de desarrollo del proyecto?", "respuesta": "Se divide en tres subdivisiones: el equipo base, los módulos complementarios y los asesores."}
        ]
    },
    {
        'texto': "Las reuniones se llevan a cabo semanalmente, donde el líder del equipo se reúne individualmente con cada miembro del equipo base para revisar avances y resolver dudas. Además, se realizan reuniones con los asesores cuando se requiere asistencia experta, y una reunión general con todos los miembros del objetivo III del proyecto para presentar los avances. La comunicación se realiza a través de tres mecanismos principales: un grupo de WhatsApp para comunicaciones rápidas, el correo institucional para formalidades y un dashboard que muestra visualmente el estado de las tareas asignadas a cada miembro del equipo base.",
        'preguntas_respuestas': [
            {"pregunta": "¿Con qué frecuencia se llevan a cabo las reuniones dentro del equipo de desarrollo?", "respuesta": "Las reuniones se llevan a cabo semanalmente."},
            {"pregunta": "¿Qué tipos de reuniones se realizan y con qué propósito?", "respuesta": "Se realizan reuniones individuales con el líder del equipo base para revisar avances y resolver dudas, reuniones con los asesores cuando se requiere asistencia experta, y una reunión general con todos los miembros del objetivo III del proyecto para presentar los avances."},
            {"pregunta": "¿Cuáles son los mecanismos de comunicación utilizados dentro del equipo de desarrollo?", "respuesta": "Se utilizan un grupo de WhatsApp para comunicaciones rápidas, el correo institucional para formalidades y un dashboard para visualizar el estado de las tareas asignadas a cada miembro del equipo base."}
        ]
    }
]

# Entrenar al chatbot
trainer = ListTrainer(bot)
for data in datos_entrenamiento:
    trainer.train([data['texto']])
    for qa_pair in data['preguntas_respuestas']:
        trainer.train([
            qa_pair['pregunta'],
            qa_pair['respuesta']
        ])

def menu_ppal():
    lst_parrafos=["Plataforma piloto", "Equipo de desarrollo", "Metodología para la gestión del proceso de desarrollo"]
    lst_menu=[]
    for i, data in enumerate(datos_entrenamiento, start=1):
        lst_menu.append("{}. {}".format(i,lst_parrafos[i-1]))
    lst_menu.append("0. Salir")
    return lst_menu

@app.route('/old')
def index_old():
    menu_ppal_datos = menu_ppal()
    return render_template('index.html',menu_ppal=menu_ppal_datos,menu_ppal_len=len(menu_ppal_datos),datos_entrenamiento=datos_entrenamiento)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        opcion_seleccionada = int(request.form['opcion'])
        if opcion_seleccionada in range(1, len(datos_entrenamiento) + 1):
            data = datos_entrenamiento[opcion_seleccionada - 1]
            pregunta = data['texto']
            respuesta = bot.get_response(pregunta).text
            return render_template('respuesta.html', pregunta=pregunta, respuesta=respuesta)
        elif opcion_seleccionada == 0:
            return "Esto finaliza nuestra interacción. ¡Vuelve pronto!"
        else:
            return "Opción no válida. Por favor, selecciona una opción válida."
    else:
        menu_ppal_datos = menu_ppal()
        return render_template('index.html', menu_ppal=menu_ppal_datos, menu_ppal_len=len(menu_ppal_datos), datos_entrenamiento=datos_entrenamiento)


@app.route('/respuesta', methods=['POST'])
def respuesta():
    opcion_elegida = int(request.form['opcion'])
    if opcion_elegida in range(1, len(datos_entrenamiento) + 1):
        data = datos_entrenamiento[opcion_elegida - 1]
        preguntas = [qa_pair['pregunta'] for qa_pair in data['preguntas_respuestas']]
        return render_template('preguntas.html', preguntas=preguntas)
    elif opcion_elegida == 0:
        return "Esto finaliza nuestra interacción. ¡Vuelve pronto!"
    else:
        return "Opción no válida. Por favor, selecciona una opción válida."

@app.route('/respuesta_chat_old', methods=['POST'])
def respuesta_chat_old():
    pregunta_seleccionada = request.form['pregunta']
    respuesta = bot.get_response(pregunta_seleccionada)
    return respuesta.text

from flask import render_template

@app.route('/respuesta_chat', methods=['POST'])
def respuesta_chat():
    pregunta_seleccionada = request.form['pregunta']
    respuesta = bot.get_response(pregunta_seleccionada)
    
    # Aquí establece el índice del menú de preguntas anterior
    menu_anterior = 1  # Esto debería ser el índice correcto del menú de preguntas anterior
    
    return render_template('respuesta_chat.html', respuesta=respuesta.text, menu_anterior=menu_anterior)

@app.route('/preguntas_anteriores', methods=['POST'])
def preguntas_anteriores():
    # Obtener el índice del menú de preguntas anterior del formulario POST
    menu_anterior = int(request.form['menu_anterior'])
    
    # Lógica para obtener y renderizar el menú de preguntas anterior
    menu_ppal_datos = obtener_menu_anterior(menu_anterior)  # Implementa esta función según tu lógica de aplicación
    
    return render_template('index.html', menu_ppal=menu_ppal_datos, menu_ppal_len=len(menu_ppal_datos), datos_entrenamiento=datos_entrenamiento)

@app.route('/menu_anterior/<int:menu_anterior>', methods=['GET'])
def menu_anterior(menu_anterior):
    # Aquí puedes manejar la lógica para mostrar el menú de preguntas anterior
    # Puedes utilizar el valor de menu_anterior para determinar qué menú mostrar
    # Por ejemplo, si menu_anterior es 1, puedes mostrar el primer menú, si es 2, el segundo menú, y así sucesivamente
    
    # Después de procesar la lógica, renderiza la plantilla correspondiente
    return render_template('menu_anterior.html', menu_anterior=menu_anterior)

if __name__ == '__main__':
    app.run(debug=True)
