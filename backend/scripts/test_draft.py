from app.email_providers.gmail_provider import GmailProvider
from app.agents.draft_generator import DraftGenerator

provider = GmailProvider()
generator = DraftGenerator()

email = provider.get_messages()[0]

draft = generator.generate(email)

print(draft)