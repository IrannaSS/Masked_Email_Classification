# pylint: disable=line-too-long
"""This module defines an API endpoint for classifying email content."""

from fastapi import APIRouter
from pydantic import BaseModel

from utils import mask_pii
from models import predict_category

router = APIRouter()


class EmailInput(BaseModel):
    # pylint: disable=too-few-public-methods
    """Represents the input model for the classify_email endpoint.

    input_email_body (str): The raw email body text provided by the user.
    """

    input_email_body: str


@router.post("/classify")
def classify_email(input_data: EmailInput):
    """
    Classifies the content of an email after masking any PII.

    Args:
        input_data (EmailInput): The input data containing the raw email body.

    Returns:
        dict: A dictionary containing:
            - input_email_body (str): The original email body.
            - list_of_masked_entities (list): The list of detected and masked PII entities.
            - masked_email (str): The email body after masking PII.
            - category_of_the_email (str): The predicted category of the email.
    """
    original_email = input_data.input_email_body
    masked_email, entities = mask_pii(original_email)
    category = predict_category(masked_email)

    return {
        "input_email_body": original_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category,
    }
