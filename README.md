---
title: Email Classifier Project
emoji: 📉
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 📧 Email Classifier with PII Masking

An intelligent tool that classifies emails into categories like Work, Personal, Spam, etc., while protecting sensitive information through PII (Personally Identifiable Information) masking.

**🔗 Live Demo:** [🌐 Try it on Hugging Face Spaces](https://huggingface.co/spaces/Irannas/Masked_Email_Classification)  
**📁 GitHub Repo:** [GitHub Repository](https://github.com/IrannaSS/Masked_Email_Classification)

---

## 🚀 Features

- 🔐 **PII Masking**: Automatically detects and masks sensitive information such as names, phone numbers, email addresses, and more.
- 🧠 **Email Classification**: Uses a fine-tuned transformer model to classify email content into predefined categories.
- ⚡ **Real-Time Inference**: Deployed with Streamlit for fast and user-friendly web interaction.
- 📂 **Batch Upload Support**: Upload multiple email files (TXT format) and process them in one go.

---

## 🧰 Tech Stack

- **Language:** Python 3.10+
- **NLP Libraries:** Transformers (Hugging Face), spaCy, scikit-learn
- **Model:** DistilBERT / Custom Transformer
- **Deployment:** Streamlit, Hugging Face Spaces
- **PII Detection:** Regex + spaCy NER

---

## 📁 Project Structure

Email_Classifier_Project/
├── app/                      # Streamlit App
│   └── app.py
├── model/                    # Trained model and tokenizer
│   └── classifier_model/
├── data/                     # Sample email data
│   └── sample_emails/
├── utils/                    # Helper functions (PII masking, preprocessing, etc.)
│   └── preprocess.py
├── requirements.txt
├── Dockerfile               
└── README.md



---

## ⚙️ Installation

Clone the repository and install the requirements:

```bash
git clone https://github.com/IrannaSS/Masked_Email_Classification
cd your-repo-name
pip install -r requirements.txt


Run the Streamlit app locally:

        streamlit run app/app.py



