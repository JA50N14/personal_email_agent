from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class DraftGenerator:

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-5-nano",
            temperature=0.3
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are an expert professional email assistant. "
             "Write clear, concise, polite email replies."),
            ("user",
             """
Original email:

From: {sender}
Subject: {subject}

Body:
{body}

Write a professional reply email. Keep it concise and natural.
Do not include explanations. Only output the email reply.
""")
        ])

        self.chain = self.prompt | self.llm

    def generate(self, email: dict) -> str:
        response = self.chain.invoke({
            "sender": email.get("sender"),
            "subject": email.get("subject"),
            "body": email.get("body", "")[:2000]
        })

        return response.content.strip()