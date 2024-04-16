from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear una instancia del chatbot
bot = ChatBot('DataGovernor')

# Datos de entrenamiento: párrafos y preguntas con respuestas asociadas
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

trainer = ListTrainer(bot)

# Entrenar al chatbot con los párrafos completos de texto
for data in datos_entrenamiento:
    trainer.train([data['texto']])
    
for data in datos_entrenamiento:
    trainer.train([data['texto']])
    for qa_pair in data['preguntas_respuestas']:
        trainer.train([
            qa_pair['pregunta'],
            qa_pair['respuesta']
        ])

print("¡Hola!, soy DataGovernor y estoy aquí para informarte sobre la implementación de un modelo de gobernanza de datos para el Sistema de CTeI del departamento de  Caldas, que garantice su calidad, interoperabilidad, transaccionalidad frente a las necesidades de las  subregiones en Caldas.")
print("Por favor, selecciona el tema que te gustaría explorar:")


def menu_ppal():
    lst_parrafos=["Plataforma piloto", "Equipo de desarrollo", "Metodología para la gestión del proceso de desarrollo"]
    for i, data in enumerate(datos_entrenamiento, start=1):
        print("{}. {}".format(i,lst_parrafos[i-1]))
    print("0. Salir")

menu_ppal()
# Procesar la selección del usuario
while True:
    try:
        opcion_elegida = int(input("Selecciona una opción (0 para salir): "))
        if opcion_elegida == 0:
            print("Esto finaliza nuestra interacción. ¡Vuelve pronto!")
            break
        elif opcion_elegida in range(1, len(datos_entrenamiento) + 1):
            data = datos_entrenamiento[opcion_elegida - 1]
            print(f"\nPárrafo seleccionado: {data['texto']}\n")
            
            while True:
                print("Selecciona una pregunta:")
                for j, qa_pair in enumerate(data['preguntas_respuestas'], start=1):
                    print(f"{j}. {qa_pair['pregunta']}")
                print("{}. Haz tu propia pregunta".format(j+1))
                print("0. Volver al menú principal")
                
                pregunta_elegida = int(input("Selecciona una pregunta (0 para volver al menú principal): "))
                if pregunta_elegida == 0:
                    menu_ppal()
                    break
                elif pregunta_elegida in range(1, len(data['preguntas_respuestas']) + 1):
                    pregunta = data['preguntas_respuestas'][pregunta_elegida - 1]['pregunta']
                    respuesta = bot.get_response(pregunta)
                    print(f"\nRespuesta: {respuesta}\n")
                elif pregunta_elegida == len(datos_entrenamiento) + 1:
                    pregunta_usuario = input("Por favor, ingresa tu pregunta: ")
                    respuesta = bot.get_response(pregunta_usuario)
                    print(f"\nRespuesta: {respuesta}\n")
                else:
                    print("Opción no válida. Por favor, selecciona una pregunta válida.")
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
    except (ValueError, IndexError):
        print("Error: ingresa un número válido para seleccionar una opción o pregunta.")
