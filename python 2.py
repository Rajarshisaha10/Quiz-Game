import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd
data = pd.read_csv('tripadvisor_hotel_reviews.csv')
#print(data.head())
#print(data['Review'][0])
data['review_lowercase'] = data['Review'].str.lower()
#print(data.head())
en_stopwords = stopwords.words('english')
en_stopwords.remove('not')  # 'not' is often used in negation, so we keep it
data['Review_no-stopwords'] = data['review_lowercase'].apply(lambda x: ' '.join([word for word in x.split() if word not in en_stopwords]))
#print(data['Review_no-stopwords'][0])
data['Review_no-punctuation'] = data['Review_no-stopwords'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
#print(data['Review_no-punctuation'][0])
# Removed redundant punctuation removal
#print(data['Review_no-punctuation'][0])
#print(data.head())
data['tokensized'] = data['Review_no-punctuation'].apply(word_tokenize)
#print(data['tokensized'][0])
ps = PorterStemmer()
data['stemmed'] = data['tokensized'].apply(lambda tokens: [ps.stem(word) for word in tokens])
#print(data['stemmed'][0])
print(data.head())
lemmatizer = WordNetLemmatizer()
data['lemmatized'] = data['tokensized'].apply(lambda tokens: [lemmatizer.lemmatize(token) for token in tokens])
tokens_clean = sum(data['lemmatized'], [])
unigrams = pd.Series(nltk.ngrams(tokens_clean, 1)).value_counts()
print(unigrams[0:10])