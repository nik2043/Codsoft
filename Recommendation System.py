movies = {
    "Agnipath": {"genres": ["Action", "Adventure"]},
    "Dream Girl": {"genres": ["Comedy", "Romance"]},
    "Iron Man": {"genres": ["Action", "Sci-Fi"]},
    "Rush Hour": {"genres": ["Action", "Comedy"]},
    "Sultan": {"genres": ["Drama", "Romance"]},
    "Dune": {"genres": ["Adventure", "Romance"]},
}

def similarity(movie1, movie2):
    genres1 = set(movies[movie1]["genres"])
    genres2 = set(movies[movie2]["genres"])
    common_genres = genres1.intersection(genres2)
    score = len(common_genres) / len(genres1.union(genres2))
    return score

def recommend(user_likes):
    recommendations = {}
    for movie in movies:
        if movie not in user_likes:
            similarity_score = sum(similarity(movie, liked_movie) for liked_movie in user_likes)
            recommendations[movie] = similarity_score
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

user_input = input("Enter your favorite movies separated by commas: ")
user_likes = [movie.strip() for movie in user_input.split(",")]

top_recommendations = recommend(user_likes)[:5]
print("Top movie recommendations:")
for movie, score in top_recommendations:
    print(f"{movie} (Similarity Score: {score:.2f})")
