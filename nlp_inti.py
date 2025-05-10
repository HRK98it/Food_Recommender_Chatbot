import re
import nltk
import pandas as pd
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
df = pd.read_csv("restaurant_food_data_100.csv")

all_ingredients = set()
for ing_list in df['ingredients'].dropna():
    all_ingredients.update([i.strip().lower() for i in ing_list.split(',')])

possible_ingredients = list(all_ingredients)

def extract_ingredients(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    found = [word for word in tokens if word in possible_ingredients]
    return found
