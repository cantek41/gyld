"""
This is to handle the text data preprocessing and feature engineering.

"""

import re

# Spacy Processor
# Preprocessing with spaCy
import spacy
from gensim.parsing.preprocessing import strip_tags


# Simple Preprocessing to convert text into lower case and remove special characters
def preprocess_text_simple(text):
    # remove backslash-apostrophe
    text = re.sub("\'", "", text)
    # remove everything except alphabets
    text = re.sub("[^a-zA-Z]", " ", text)
    # remove whitespaces
    text = ' '.join(text.split())
    # convert text to lowercase
    text = text.lower()

    return text


"""

The function below can be used on either one text body, or onto the entire dataset to produce a tokenized training set.
It is used in the fill_tags.py script as our named entities/tokens can be used to fill missing tags.

"""


# This code will process the text data using spaCy, and also extracts the 'named' entities.
# df_test['Description'].apply(lambda x: pp.preprocess_text_spaCy(x))
def preprocess_text_spaCy(text):
    nlp = spacy.load("en_core_web_sm")
    text = str(text)
    original_text = str(strip_tags(text))
    print(original_text)
    original_text = original_text.replace('\t', ' ')
    original_text = original_text.replace('\n', ' ').replace('\r', ' ')
    original_text = original_text.replace('&amp;', 'and').replace('&gt;', '>').replace('&lt;', '<')

    doc = nlp(original_text)
    ents = [str(entity).strip() for entity in doc.ents]  # Named entities.

    # Keep only words (no numbers, no punctuation).
    # Lemmatize tokens, remove punctuation and remove stopwords.
    doc = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

    # Add named entities, but only if they are a compound of more than word.
    relevant_entities = [str(entity) for entity in ents if len(entity) > 1]
    doc.extend(relevant_entities)

    game_token = doc

    print('Game Token:', game_token)

    return game_token


# Main Function
if __name__ == "__main__":
    pass
