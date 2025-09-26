import pickle
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel

def load_models(models_dir='models'):
    books = pickle.load(open(f"{models_dir}/books_list.pkl", 'rb'))
    tfidf_matrix = pickle.load(open(f"{models_dir}/tfidf_matrix.pkl", 'rb'))
    return books, tfidf_matrix

def content_recommender(title, books, tfidf_matrix, top_n=5):
    indices = pd.Series(books.index, index=books['Title']).drop_duplicates()
    if title not in indices:
        return pd.DataFrame()
    idx = indices[title]
    sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    sim_indices = sim_scores.argsort()[-top_n-1:][::-1][1:top_n+1]
    return books.iloc[sim_indices][['Title', 'authors', 'categories']]
