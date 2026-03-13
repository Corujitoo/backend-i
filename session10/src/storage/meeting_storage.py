from src.models.meeting_models import Meeting
from uuid import UUID

meeting_storage: dict[UUID, Meeting] = {}
