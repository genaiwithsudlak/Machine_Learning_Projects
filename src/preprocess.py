import pandas as pd

def preprocess_books(books_df):
    books_df = books_df[["Title", "description", "authors", "categories", "ratingsCount"]]
    books_df = books_df.dropna(subset=["Title"])

    books_df["description"] = books_df["description"].fillna("No description available")
    books_df["authors"] = books_df["authors"].fillna("Unknown Author")
    books_df["categories"] = books_df["categories"].fillna("Unknown")
    books_df["ratingsCount"] = books_df["ratingsCount"].fillna(0)

    return books_df

def preprocess_ratings(ratings_df):
    ratings_df = ratings_df[["Id", "Title", "review/score", "review/summary", "review/text"]]
    ratings_df = ratings_df.dropna(subset=["Title"])
    ratings_df["summary"] = ratings_df["review/summary"].fillna("")
    ratings_df["review/score"] = ratings_df["review/score"].astype(float)

    # Join summary + text
    ratings_df["review_text"] = ratings_df["review/summary"].astype(str) + " / " + ratings_df["review/text"].astype(str)

    # Drop old cols
    ratings_df = ratings_df.drop(columns=["review/summary", "review/text"])
    ratings_df = ratings_df.drop(columns=["summary"])

    return ratings_df
