import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./applymate.db')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SCRAPE_USER_AGENT = os.getenv('SCRAPE_USER_AGENT', 'ApplyMateBot/1.0')
SCRAPE_INTERVAL_MINUTES = int(os.getenv('SCRAPE_INTERVAL_MINUTES', 60))
