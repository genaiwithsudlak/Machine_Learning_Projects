<<<<<<< HEAD
# Book Recommender

This repository contains an end-to-end, GitHub-ready Book Recommender project using content-based filtering (TF-IDF).

## Structure
- `data/` - place your `books_data.csv` and `books_rating.csv` here.
- `src/` - preprocessing, model building and recommender functions.
- `models/` - generated pickles after running `scripts/build_model.py`.
- `app.py` - Streamlit app to run the recommender.

## Quick start
1. Put `books_data.csv` and `books_rating.csv` into `data/`.
2. Create a virtualenv and install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Build the model:
   ```
   python scripts/build_model.py
   ```
   This generates files in `models/`.
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

=======
# Machine_Learning_Projects
>>>>>>> 360b28ebbfbfd155ef7c2eff6cc54addf3360328
