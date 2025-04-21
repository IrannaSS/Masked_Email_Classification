"""Core logic for email classification and PII masking pipeline."""

from utils import mask_pii
from models import predict_category


def classify_email_pipeline(original_email: str):
    """Process the input email by masking PII and classifying the email category.

    Args:
        original_email (str): The raw email text provided by the user.

    Returns:
        dict: A dictionary containing:
            - input_email_body (str): The original email content.
            - list_of_masked_entities (list): List of detected and masked PII entities.
            - masked_email (str): The email content with PII masked.
            - category_of_the_email (str): The predicted category of the email.
    """
    masked_email, entities = mask_pii(original_email)
    category = predict_category(masked_email)

    return {
        "input_email_body": original_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category,
    }
