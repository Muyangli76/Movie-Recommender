import streamlit as st
import pickle
import requests

# Function to fetch movie poster using movie ID (no longer needed for display)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb686d19ceb9bb1&language=en-US"
    
    response = requests.get(url)
    if response.status_code != 200:
        return "https://via.placeholder.com/500"  # Return a placeholder image if request fails
    
    data = response.json()
    
    if 'poster_path' in data and data['poster_path']:
        full_path = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    else:
        full_path = "https://via.placeholder.com/500"  # Return a placeholder image if no poster is available
    
    return full_path

# Load movie data and similarity matrix
try:
    movies = pickle.load(open("movies_list.pkl", 'rb'))
    similarity = pickle.load(open("similarity.pkl", 'rb'))
    movies_list = movies['title'].values
except FileNotFoundError:
    st.error("Movie data files not found. Please check the file paths.")
    movies_list = []

# Set header for the web app
st.header("Movie Recommender System")

# Create a dropdown to select a movie
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    # Find the index of the selected movie from the dataframe based on its title
    index = movies[movies['title'] == movie].index[0]

    # Calculate similarity score
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommend_movie = []
    
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]]['title'])

    return recommend_movie

if st.button("Recommend"):
    recommended_movies = recommend(selectvalue)
    
    # Display only the movie names
    for movie in recommended_movies:
        st.write(movie)  # This will display the movie names without images
