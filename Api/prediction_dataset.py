import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



def chatbot_new(value,given_msg):
    topic = value

    df = pd.read_csv("dataset/{}.csv".format(value))

    # Combine the datasets

    # Split the combined dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        df['Question'], df['Answer'], test_size=0.2, random_state=42
    )

    # Train a classifier for bakery-related questions
    bakery_classifier = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    bakery_classifier.fit(X_train, y_train)

    # Train a classifier for cricket-related questions
    cricket_classifier = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    cricket_classifier.fit(X_train, y_train)

    # Evaluate accuracy
    # bakery_accuracy = accuracy_score(y_train, bakery_classifier.predict(X_train))
    # bakery_accuracy = bakery_accuracy * 100

    if topic.lower() == topic:
        question = given_msg
        answer = bakery_classifier.predict([question])[0]
        msg = answer

    else:
        msg = 'Ask me relative question'

    return msg
