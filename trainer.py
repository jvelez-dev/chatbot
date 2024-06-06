import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from load_QA_files import read_file

nlp = spacy.load("es_core_news_sm")

bot = ChatBot('DataGovernor', preprocessors=['chatterbot.preprocessors.clean_whitespace', 'chatterbot.preprocessors.unescape_html'],
              storage_adapter="chatterbot.storage.SQLStorageAdapter", logic_adapters=["chatterbot.logic.BestMatch", "chatterbot.logic.TimeLogicAdapter"], spacy_language=nlp)

objective_one_QA = read_file("objective_1.txt")
objective_two_QA = read_file("objective_2.txt")
objective_three_QA = read_file("objective_3.txt")
objective_four_QA = read_file("objective_4.txt")

training_data =[
    {
        'Text':'objective1',
        'Questions_Answers':objective_one_QA
    },
    {
        'Text':'objective2',
        'Questions_Answers':objective_two_QA
    },
    {
        'Text':'objective3',
        'Questions_Answers':objective_three_QA
    },
    {
        'Text':'objective4',
        'Questions_Answers':objective_four_QA
    },
]

def train_bot():
    trainer = ListTrainer(bot)
    for data in training_data:
        trainer.train([data['Text']])
        for qa_pair in data['Questions_Answers']:
            trainer.train([
                qa_pair['Question'],
                qa_pair['Answer']
            ])
    return trainer

def get_bot():
    return bot

def get_objectives_QA():
    return objective_one_QA,objective_two_QA,objective_three_QA,objective_four_QA

