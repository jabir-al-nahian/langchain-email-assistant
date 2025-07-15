import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

def summarize_email(email_text: str) -> str:
    prompt = f"Please provide a concise summary of the following email:\n\n{email_text}"
    response = llm.generate([{"role": "user", "content": prompt}])
    return response.generations[0][0].text.strip()

def generate_reply(email_text: str) -> str:
    prompt = f"Write a polite and professional reply to the following email:\n\n{email_text}"
    response = llm.generate([{"role": "user", "content": prompt}])
    return response.generations[0][0].text.strip()
