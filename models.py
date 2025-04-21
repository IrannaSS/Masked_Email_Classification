"""Model training and prediction logic for email classification."""

import pickle  # Standard library import first
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_model():
    """
    Train a logistic regression model to classify email types.

    Loads a dataset, preprocesses the text, vectorizes it using TF-IDF, 
    trains a logistic regression classifier, and saves the model and vectorizer.
    """
    df = pd.read_csv("combined_emails_with_natural_pii.csv")
    df.dropna(subset=["email", "type"], inplace=True)

    email_texts = df["email"]
    labels = df["type"]

    vectorizer = TfidfVectorizer(
        stop_words="english", ngram_range=(1, 2), max_df=0.95, min_df=2
    )
    vectorized_emails = vectorizer.fit_transform(email_texts)

    model = LogisticRegression(max_iter=1000)
    model.fit(vectorized_emails, labels)

    with open("classifier_model.pkl", "wb") as f:
        pickle.dump((model, vectorizer), f)


def map_prediction(raw_label):
    """
    Map internal model label to a user-friendly category.

    Args:
        raw_label (str): The raw label predicted by the model.

    Returns:
        str: Human-readable label for UI display.
    """
    label_map = {
        "Incident": "Technical Support",
        "Problem": "Billing Issues",
        "Request": "Account Management",
        "Change": "Account Management",
    }
    return label_map.get(raw_label, raw_label)


def predict_category(text):
    """
    Predict the category of the given email content.

    Args:
        text (str): The masked or original email content.

    Returns:
        str: Predicted email category.
    """
    with open("classifier_model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)

    vec_text = vectorizer.transform([text])
    return model.predict(vec_text)[0]
