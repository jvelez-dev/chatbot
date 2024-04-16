from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear una instancia del chatbot
bot = ChatBot('Terminal')

# Datos de entrenamiento: párrafo y preguntas asociadas con respuestas
datos_entrenamiento = [
    {
        'texto': "Hola, soy DataGovernor. Soy el ChatBOT que te brindará información sobre cada objetivo del proyecto de gobernanza de datos.",
        'preguntas_respuestas': [
            {'pregunta': "¿Qué es un ejemplo básico?", 'respuesta': "Un ejemplo básico es..."},
            {'pregunta': "¿Qué queremos que el chatbot pueda hacer?", 'respuesta': "Queremos que el chatbot pueda..."},
            {'pregunta': "¿Puedo agregar más información aquí?", 'respuesta': "Sí, puedes agregar más información..."}
        ]
    }
]

# Entrenar al chatbot con los datos de entrenamiento
trainer = ListTrainer(bot)

for data in datos_entrenamiento:
    trainer.train([data['texto']])
    for qa_pair in data['preguntas_respuestas']:
        trainer.train([
            qa_pair['pregunta'],
            qa_pair['respuesta']
        ])

# Interactuar con el chatbot entrenado
while True:
    try:
        pregunta = input("Haz una pregunta sobre el texto: ")
        respuesta = bot.get_response(pregunta)
        print(respuesta)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
