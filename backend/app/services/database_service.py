from supabase import create_client

from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


class DatabaseService:
    def __init__(self):
        self.client = create_client(
            SUPABASE_URL,
            SUPABASE_SECRET_KEY,
        )


database_service = DatabaseService()