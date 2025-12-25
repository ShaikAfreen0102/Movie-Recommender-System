🎬 Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit. This application suggests movies similar to a user's choice by analyzing metadata like genres, keywords, cast, and crew.

🚀 Project Overview
Finding the perfect movie to watch can be a challenge. This project uses **Machine Learning** and **Natural Language Processing (NLP)** to find similarities between over 5,000 movies from the TMDB dataset, providing instant recommendations through an interactive web interface.

✨ Key Features
- **Smart Search:** Select a movie from a dropdown of 5,000+ titles.
- **Instant Recommendations:** Get 5 similar movie suggestions instantly.
- **Dynamic UI:** Clean and responsive interface built with Streamlit.


## 🛠️ Tech Stack
| Category | Tools / Libraries |
| :--- | :--- |
| **Language** | Python |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (Cosine Similarity, CountVectorizer) |
| **NLP** | NLTK (Stemming) |
| **Web Framework** | Streamlit |

## 🧠 How it Works
1. **Data Preprocessing:** Merged the `tmdb_5000_movies` and `tmdb_5000_credits` datasets.
2. **Feature Engineering:** Combined genres, keywords, overview, cast, and crew into a single "tags" column.
3. **Vectorization:** Used `CountVectorizer` to convert text tags into a 5,000-dimensional vector for each movie.
4. **Similarity Calculation:** Applied **Cosine Similarity** to measure the distance between movie vectors. 
5. **Pickling:** Exported the processed data and similarity matrix as `.pkl` files for the web app.


 📂 Project Structure
├── app.py              # Streamlit web application
├── movies.pkl          # Processed movie list (Serialized)
├── similarity.pkl      # Similarity matrix (Serialized)
├── requirements.txt    # List of dependencies
├── setup.sh            # Configuration for deployment
├── procfile            # Deployment instructions for Heroku/Render
└── .gitignore          # Files excluded from GitHub (like large .pkl files)
