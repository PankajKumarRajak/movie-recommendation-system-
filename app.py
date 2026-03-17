import streamlit as st
import pickle

# Load model
movies = pickle.load(open('model/movies.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]


# UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    results = recommend(selected_movie)

    for movie in results:
        st.write(movie)