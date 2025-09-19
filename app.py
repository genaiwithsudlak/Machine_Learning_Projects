import streamlit as st
import pickle
from src.recommender import load_models, content_recommender

st.set_page_config(page_title='Book Recommender', layout='wide')
st.header('📚 Book Recommender')

# Load models
try:
    books, tfidf_matrix = load_models()
except Exception as e:
    st.error(f"Models not found. Run `python scripts/build_model.py` first. Error: {e}")
    st.stop()

book_list = books['Title'].values
selected = st.selectbox('Choose a book', book_list)

if st.button('Show Recommendations'):
    recs = content_recommender(selected, books, tfidf_matrix, top_n=5)
    if recs.empty:
        st.warning('No recommendations found.')
    else:
        cols = st.columns(5)
        for i, (_, row) in enumerate(recs.iterrows()):
            with cols[i]:
                st.subheader(row['Title'])
                st.caption(row['authors'])
                st.text(row['categories'])
