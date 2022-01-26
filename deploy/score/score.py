import os
import logging
import json
import numpy
import joblib
from transformers import pipeline
def init():
    global token_classifier
    token_classifier = pipeline( "token-classification", 
      model="huggingface-course/bert-finetuned-ner", 
    i aggregation_strategy="simple" )
    logging.info("Init complete")
def run(raw_data):
    logging.info("Request processing...")
    return str(token_classifier(raw_data))

