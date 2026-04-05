from app.domain.models import Meeting
from app.storage.json_repository import load_meetings, save_meetings

meetings: list[Meeting] = load_meetings()
