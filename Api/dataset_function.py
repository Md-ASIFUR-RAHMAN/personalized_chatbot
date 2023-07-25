import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
import re


# Chatbot function
def chatbot(value,given_msg):
    topic = str(value)
    print(topic)

    # Read the dataframes
    bakery_df = pd.read_csv("dataset/Bakery.csv")
    ecommerce_df = pd.read_csv("dataset/ecommerce.csv")
    restaurant_df = pd.read_csv("dataset/Restaurant.csv")

    fitness_df = pd.read_csv("dataset/Fitness_Studio.csv")
    school_df = pd.read_csv("dataset/Language_school.csv")
    wedding_plan_df = pd.read_csv("dataset/wedding_planning_service.csv")

    realstate_df = pd.read_csv("dataset/Real_State.csv")
    home_cleaning_df = pd.read_csv("dataset/home_cleaning.csv")
    pet_df = pd.read_csv("dataset/pet.csv")
    software_dev_df = pd.read_csv("dataset/software_dev.csv")
    tutor_service_df = pd.read_csv("dataset/tutor_service.csv")
    web_dev_df = pd.read_csv("dataset/web_dev.csv")





    # Train a vectorizer for bakery-related questions
    bakery_vectorizer = TfidfVectorizer()
    bakery_question_vectors = bakery_vectorizer.fit_transform(bakery_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    ecommerce_vectorizer = TfidfVectorizer()
    ecommerce_question_vectors = ecommerce_vectorizer.fit_transform(ecommerce_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    restaurant_vectorizer = TfidfVectorizer()
    restaurant_question_vectors = restaurant_vectorizer.fit_transform(restaurant_df['Question'].values.astype('U'))

    #####

    # Train a vectorizer for bakery-related questions
    fitness_vectorizer = TfidfVectorizer()
    fitness_question_vectors = fitness_vectorizer.fit_transform(fitness_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    school_vectorizer = TfidfVectorizer()
    school_question_vectors = school_vectorizer.fit_transform(school_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    wedding_plan_vectorizer = TfidfVectorizer()
    wedding_plan_question_vectors = wedding_plan_vectorizer.fit_transform(wedding_plan_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    realstate_vectorizer = TfidfVectorizer()
    realstate_question_vectors = realstate_vectorizer.fit_transform(realstate_df['Question'].values.astype('U'))

    ####################

    # Train a vectorizer for bakery-related questions
    home_cleaning_vectorizer = TfidfVectorizer()
    home_cleaning_question_vectors = home_cleaning_vectorizer.fit_transform(home_cleaning_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    pet_vectorizer = TfidfVectorizer()
    pet_question_vectors = pet_vectorizer.fit_transform(pet_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    software_dev_vectorizer = TfidfVectorizer()
    software_dev_question_vectors = software_dev_vectorizer.fit_transform(software_dev_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    tutor_service_vectorizer = TfidfVectorizer()
    tutor_service_question_vectors = tutor_service_vectorizer.fit_transform(tutor_service_df['Question'].values.astype('U'))

    # Train a vectorizer for cricket-related questions
    web_dev_vectorizer = TfidfVectorizer()
    web_dev_question_vectors = web_dev_vectorizer.fit_transform(web_dev_df['Question'].values.astype('U'))

    ignore_words = ["what", "how", "where", "is", "are", "why", "when"]

    # Remove ignore words from the input question
    question_words = re.findall(r'\b\w+\b', given_msg.lower())
    filtered_question = " ".join([word for word in question_words if word not in ignore_words])
    given_msg = filtered_question


    if topic.lower() == 'bakery' or topic.lower() == 'pastry' or topic.lower() == 'bakery and pastry':
        question = given_msg
        question_vector = bakery_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, bakery_question_vectors)[0]
        print(similarity_scores)
        most_similar_index = similarity_scores.argmax()
        print(most_similar_index)
        print(similarity_scores[most_similar_index])

        if similarity_scores[most_similar_index] > 0.2:
            answer = bakery_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'ecommerce' or topic.lower() == 'e-commerce' or topic.lower() == 'ecomerce':
        question = given_msg
        question_vector = ecommerce_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, ecommerce_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = ecommerce_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'restaurant' or topic.lower() == 'resturent' or topic.lower() == 'restaurent':
        question = given_msg
        question_vector = restaurant_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, restaurant_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = restaurant_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'fitness' or topic.lower() == 'gym' or topic.lower() == 'body fitness' or topic.lower() == 'body-fitness':
        question = given_msg
        question_vector = fitness_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, fitness_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0:
            answer = fitness_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'language school' or topic.lower() == 'language' or topic.lower() == 'school':
        question = given_msg
        question_vector = school_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, school_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0:
            answer = school_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'wedding planning' or topic.lower() == 'wedding planner':
        question = given_msg
        question_vector = wedding_plan_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, wedding_plan_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0:
            answer = wedding_plan_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence"

    elif topic.lower() == 'realstate' or topic.lower() == 'real-state' or topic.lower() == 'real state':
        question = given_msg
        question_vector = realstate_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, realstate_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = realstate_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."




        #############

    elif topic.lower() == 'home clean' or topic.lower() == 'home cleaner' or topic.lower() == 'home cleaning':
        question = given_msg
        question_vector = home_cleaning_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, home_cleaning_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = home_cleaning_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'pet' or topic.lower() == 'pet service' or topic.lower() == 'pet-service' or topic.lower() == 'petservice':
        question = given_msg
        question_vector = pet_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, pet_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = pet_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'software' or topic.lower() == 'software service' or topic.lower() == 'it and technology' or topic.lower() == 'it consultancy':
        question = given_msg
        question_vector = software_dev_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, software_dev_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0:
            answer = software_dev_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    elif topic.lower() == 'tutor service' or topic.lower() == 'tutor':
        question = given_msg
        question_vector = tutor_service_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, tutor_service_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = tutor_service_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence"

    elif topic.lower() == 'website development' or topic.lower() == 'web development' or topic.lower() == 'web' or topic.lower() == 'website' :
        question = given_msg
        question_vector = web_dev_vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, web_dev_question_vectors)[0]
        most_similar_index = similarity_scores.argmax()

        if similarity_scores[most_similar_index] > 0.3:
            answer = web_dev_df['Answer'][most_similar_index]
            msg = answer
        else:
            msg = "Pardon me. Please ask me with a meaningful keyword or sentence."

    else:
        msg = "Ask me relative question please"
    return msg


# Start the chatbot
# chatbot()
