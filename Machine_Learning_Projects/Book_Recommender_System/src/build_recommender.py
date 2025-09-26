import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from src.preprocess import preprocess_books

def build(data_path='data/books_data.csv', models_dir='models'):
    os.makedirs(models_dir, exist_ok=True)
    books_df = pd.read_csv(data_path)
    books_clean = preprocess_books(books_df)

    books_clean['metadata'] = (
        books_clean['Title'].astype(str) + ' ' +
        books_clean['authors'].astype(str) + ' ' +
        books_clean['categories'].astype(str) + ' ' +
        books_clean['description'].astype(str)
    )

    tfidf = TfidfVectorizer(stop_words='english', max_features=50000)
    tfidf_matrix = tfidf.fit_transform(books_clean['metadata'])

    # Save artifacts
    pickle.dump(books_clean, open(os.path.join(models_dir, 'books_list.pkl'), 'wb'))
    pickle.dump(tfidf_matrix, open(os.path.join(models_dir, 'tfidf_matrix.pkl'), 'wb'))
    pickle.dump(tfidf, open(os.path.join(models_dir, 'tfidf_vectorizer.pkl'), 'wb'))
    print('Model build complete. Files saved to', models_dir)

if __name__ == '__main__':
    build()
