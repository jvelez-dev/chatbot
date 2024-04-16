from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear una instancia del chatbot
bot = ChatBot('DataGovernor')

# Datos de entrenamiento: párrafo y preguntas asociadas con respuestas
datos_entrenamiento = [
    {
        'texto': "Este es el textode entrenamiento",
        'opciones': [
            {
                'opcion': "Opción 1",
                'preguntas_respuestas': [
                    {'pregunta': "¿Qué es un ejemplo básico?", 'respuesta': "Un ejemplo básico es..."},
                    {'pregunta': "¿Qué queremos que el chatbot pueda hacer?", 'respuesta': "Queremos que el chatbot pueda..."},
                    {'pregunta': "¿Puedo agregar más información aquí?", 'respuesta': "Sí, puedes agregar más información..."}
                ]
            },
            {
                'opcion': "Opción 2",
                'preguntas_respuestas': [
                    {'pregunta': "Pregunta 1 para Opción 2", 'respuesta': "Respuesta 1 para Opción 2"},
                    {'pregunta': "Pregunta 2 para Opción 2", 'respuesta': "Respuesta 2 para Opción 2"},
                    {'pregunta': "Pregunta 3 para Opción 2", 'respuesta': "Respuesta 3 para Opción 2"}
                ]
            },
            {
                'opcion': "Opción 3",
                'preguntas_respuestas': [
                    {'pregunta': "Pregunta 1 para Opción 3", 'respuesta': "Respuesta 1 para Opción 3"},
                    {'pregunta': "Pregunta 2 para Opción 3", 'respuesta': "Respuesta 2 para Opción 3"},
                    {'pregunta': "Pregunta 3 para Opción 3", 'respuesta': "Respuesta 3 para Opción 3"}
                ]
            }
        ]
    }
]

# Entrenar al chatbot con los datos de entrenamiento
trainer = ListTrainer(bot)

for data in datos_entrenamiento:
    trainer.train([data['texto']])
    for opcion in data['opciones']:
        trainer.train([opcion['opcion']])
        for qa_pair in opcion['preguntas_respuestas']:
            trainer.train([
                qa_pair['pregunta'],
                qa_pair['respuesta']
            ])

# Presentar el menú de opciones
print("¡Bienvenido a DataGovernor!")
print("Por favor, selecciona una opción:")
for i, opcion in enumerate(datos_entrenamiento[0]['opciones'], start=1):
    print(f"{i}. {opcion['opcion']}")
print("0. Salir")

# Interactuar con el chatbot entrenado
while True:
    try:
        opcion_elegida = int(input("Selecciona una opción (0 para salir): "))
        if opcion_elegida == 0:
            print("¡Hasta luego!")
            break
        elif opcion_elegida in range(1, len(datos_entrenamiento[0]['opciones']) + 1):
            opcion = datos_entrenamiento[0]['opciones'][opcion_elegida - 1]
            print(f"\nOpción seleccionada: {opcion['opcion']}\n")
            
            while True:
                print("Selecciona una pregunta:")
                for j, qa_pair in enumerate(opcion['preguntas_respuestas'], start=1):
                    print(f"{j}. {qa_pair['pregunta']}")
                print("0. Volver al menú principal")
                
                pregunta_elegida = int(input("Selecciona una pregunta (0 para volver al menú principal): "))
                if pregunta_elegida == 0:
                    break
                elif pregunta_elegida in range(1, len(opcion['preguntas_respuestas']) + 1):
                    pregunta = opcion['preguntas_respuestas'][pregunta_elegida - 1]['pregunta']
                    respuesta = bot.get_response(pregunta)
                    print(f"\nRespuesta: {respuesta}\n")
                else:
                    print("Opción no válida. Por favor, selecciona una pregunta válida.")
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
    except (ValueError, IndexError):
        print("Error: ingresa un número válido para seleccionar una opción o pregunta.")
