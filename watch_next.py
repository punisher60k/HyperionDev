#import spacy and model to use
import spacy
nlp = spacy.load('en_core_web_md')


def next_movie(description):
    """
    Returns movie with most similar description to input when read from table "movies.txt"

    Parameters:
        description(String): any String variable that contains a movie description
    
    """
    try:
        movie_comparisons = {} #initalises dictionary
        model_description = nlp(description)
        
        #open "movies.txt" as read only
        #splits each line via ' :' separator to distinguish between movie title and description
        #each description is compared to input parameter of function, with comparison value stored in movie_comparisons
        #returns key based on MAX value in dictionary
        with open("movies.txt", "r") as file:
            for line in file:
                movie_description = line.strip()
                movie_description = movie_description.split(' :')
                similarity = nlp(movie_description[1]).similarity(model_description)
                movie_comparisons[movie_description[0]] = similarity
        most_similar_movie = max(movie_comparisons, key=movie_comparisons.get)
        return most_similar_movie
    
    except FileNotFoundError:
        print("File not found")

#input variable
hulk_description = "Will he save their world or destroy it? When the hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#store function result "next_movie" in variable recommendation
recommendation = next_movie(hulk_description)

#prints to user result
print(f"After watching \"Planet Hulk\" you should try \"{recommendation}\".")
