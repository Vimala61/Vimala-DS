import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Load dataset
df = pd.read_csv("titles.csv")

# Convert text data into numerical vectors
vectorizer = TfidfVectorizer()
genre_m = vectorizer.fit_transform(df['genres'])

# Compute cosine similarity
similarity = cosine_similarity(genre_m)

def index(request):
    return render(request, "index.html")

# Recommendation function
def Youtube_Recommendation(title):
    try:
        idx = df[df['title'].str.lower() == title.lower()].index[0]  # Get the index of the movie
        #print("idx ",idx)
        
        similar_films = list(enumerate(similarity[idx]))  # Get similarity scores
        #print("similar_films ",similar_films)
        
        sorted_movies = sorted(similar_films, key=lambda x: x[1], reverse=True)[1:5]  # Sort and get top 2
        #print("sorted_movies ", sorted_movies)
        
        recommendations = [{"title": df['title'][i[0]], "genres": df['genres'][i[0]]} for i in sorted_movies]
        #print("recommendations ", recommendations)
        
        return recommendations
    except IndexError:
        return {"error": "Title not found"}

# API View
@api_view(['GET'])
def recommend_movie(request, title):
    recommendations = Youtube_Recommendation(title)
    return Response(recommendations)
