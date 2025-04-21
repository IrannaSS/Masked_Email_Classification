"""Utility functions for detecting and masking Personally Identifiable Information (PII) in text."""

import re


def mask_pii(text):
    """
    Detect and mask personally identifiable information (PII) in the input text.

    Args:
        text (str): The raw input text (e.g., an email body).

    Returns:
        tuple:
            - masked_text (str): Text with PII replaced by placeholder tags.
            - entities (list): A list of dictionaries, each containing:
                - position (list): Start and end character positions of the PII.
                - classification (str): Type of PII (e.g., 'email', 'phone_number').
                - entity (str): The original PII detected.
    """
    entities = []
    masked_text = text

    patterns = {
        "aadhar_num": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
        "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
        "expiry_no": r"\b(0[1-9]|1[0-2])\/(\d{2}|\d{4})\b",
        "cvv_no": r"\b\d{3}\b",
        "dob": r"\b\d{2}/\d{2}/\d{4}\b",
        "phone_number": r"\b[6-9]\d{9}\b",
        "email": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
        "full_name": (
            r"(?i)\b(?:i\s*am|i'm|my\s*name\s*is|this\s*is)\s+"
            r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)"
        ),
    }

    matches = []
    # for label, pattern in patterns.items():
    #     for match in re.finditer(pattern, text):
    #         matches.append((match.start(), match.end(), label, match.group(1)))

    # matches.sort(reverse=True)
    # print(matches)

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            # If pattern includes a capturing group (like "full_name"), use the group
            if label == "full_name" and match.lastindex:
                start, end = match.span(1)  # span of the captured name only
                original_value = match.group(1)
            else:
                start, end = match.span()  # span of the full match
                original_value = match.group()
            matches.append((start, end, label, original_value))
    matches.sort(reverse=True)
    for start, end, label, original_value in matches:
        masked_text = masked_text[:start] + f"[{label}]" + masked_text[end:]
        entities.append(
            {
                "position": [start, end],
                "classification": label,
                "entity": original_value,
            }
        )

    return masked_text, entities
