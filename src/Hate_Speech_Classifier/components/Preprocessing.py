import sys
from src.Hate_Speech_Classifier.logger import logging
from src.Hate_Speech_Classifier.exception import CustomException
from src.Hate_Speech_Classifier.components.data_ingestion import DataIngestion
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import re
import string




class FeaturesPreprocessing:
    def __init__(self):
        self.stop_words =  set(stopwords.words("english"))
        self.stemmer = PorterStemmer()

    def remove_urls(self, text):
        pattern = re.compile(r"https?://\S+/www/\S+")
        return pattern.sub('', text)
    
    def remove_html_tags(self, text):
        return BeautifulSoup(text, "html.parser").get_text()
    
    def remove_emojis(self, text):
        emoji_pattern = re.compile("[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]|[\U00002702-\U000027B0]", flags=re.UNICODE)
        return emoji_pattern.sub('', text)
    
    def remove_punctuation(self, text):
        exclude = set(string.punctuation)
        return text.translate(str.maketrans("", "", ''.join(exclude)))
    
    def tokenize_and_stem(self, data):
            
        # Tokenize the data into words
            words = word_tokenize(data)

            # Remove stopwords and apply stemming
            stemmed_words = [self.stemmer.stem(word) for word in words if word.lower() not in stopwords.words('english')]

            # Join the stemmed words back into a single string
            stemmed_text = ' '.join(stemmed_words)

            return words
        
    def preprocess_text(self, data):

        try:
            # logging.info("Lets applying freatures Preprocessing")

            # Remove URLs
            data = self.remove_urls(data)

            # Remove HTML tags
            data = self.remove_html_tags(data)

            # Handle emojis
            data = self.remove_emojis(data)

            # Remove punctuation
            data = self.remove_punctuation(data)

            # Tokenize the data
            tokens = word_tokenize(data)

            # Remove stopwords and apply stemming
            filtered_words = [self.stemmer.stem(word) for word in tokens if word.lower() not in self.stop_words]

            # Join the filtered words
            filtered_text = ' '.join(filtered_words)

            data = self.tokenize_and_stem(filtered_text)
            
            # logging.info("Successfully tokenization function")

            return data
        
        except Exception as e:
                logging.info(f"An exception has occurred : {e}")
                raise Exception(e, sys)


    