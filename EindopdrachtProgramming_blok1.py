# Prototype small talk Chatbot made by Anthony Voogt
# Version 1.0
# this version is in the dutch streetlanguage 
# ask the bot basic small talk questions and it will answer in the dutch street leanguage


import os
import random
from time import sleep

import spacy.cli 
spacy.cli.download("en")

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Get the location of this python file
work_dir = os.path.abspath(os.path.dirname(__file__))

# Get the location of the database file
filename = os.path.join(work_dir, "straattaal2.txt")
with open (filename,'r') as f: 
   training_data = [l.strip().lower() for l in f.readlines()]

# Structure the data in the right format
datasets = []
current_trigger = None
for sentence in training_data:
    if current_trigger == None:
        current_trigger = sentence
        continue

    if sentence.strip() == "":
        current_trigger = None
        continue

    datasets.append([current_trigger, sentence])

# Create the chatbot that works with a 'best match' respose method
chatbot = ChatBot(
    name= '213', 
    read_only=True,
    logic_adapters=['chatterbot.logic.BestMatch'])

# Create a trainer for the chatbot
list_trainer = ListTrainer(chatbot)

# Train the chatbot
for data in datasets: 
    list_trainer.train(data)
print("Bot trained.")

# Get name for the user
username = input("Enter your name: ")

print(f"Welcome {username}, start chatting with the bot.\n\n")
while(True):
    # Get user input
    user_input = input(f"[{username}] ").lower()
    
    # Get chatbot response
    response = str(chatbot.get_response(user_input))

    # Wait a little longer to return long responses for realism
    response_length = len(response)
    sleep_time = response_length // 20
    sleep(sleep_time)

    # Print the chatbot's response
    print("[ChatBot]", chatbot.get_response(user_input)) 