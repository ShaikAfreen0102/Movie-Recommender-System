import streamlit as st
import pickle
import pandas as pd
import requests


st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
    }

    h1, h2, h3, h4, h5, h6, p {
        color: white;
    }

    .movie-card {
        background-color: #1f2933;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
    }

    img {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    data = response.json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies)

similarity = pickle.load(open("similarity.pkl", "rb"))


st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "🎥 Select a movie you like",
    movies["title"].values
)

if st.button("✨ Recommend Movies"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    for col, name, poster in zip(
        [col1, col2, col3, col4, col5],
        names,
        posters
    ):
        with col:
            st.markdown(
                f"""
                <div class="movie-card">
                    <h4>{name}</h4>
                    <img src="{poster}" width="100%">
                </div>
                """,
                unsafe_allow_html=True
            )