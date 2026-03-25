import requests
import pandas as pd

# 1. Setup API (TMDB key yahan dalo)
API_KEY = "YOUR_TMDB_API_KEY_HERE" 
BASE_URL = "https://api.themoviedb.org/3"

def get_recommendations(movie_name):
    # Movie Search
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
    data = requests.get(search_url).json()
    
    if not data['results']:
        return "Movie not found! Check spelling."

    movie_id = data['results'][0]['id']
    title = data['results'][0]['title']
    
    # Recommendation Fetch
    rec_url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}"
    rec_data = requests.get(rec_url).json()
    
    print(f"\nBecause you watched '{title}', you might like:\n")
    
    results = []
    for movie in rec_data['results'][:5]:
        results.append({
            "Title": movie['title'],
            "Rating": movie['vote_average'],
            "Release Date": movie['release_date']
        })
    
    return pd.DataFrame(results)

# 2. Input
movie_query = input("Enter a movie name: ")
print(get_recommendations(movie_query))
