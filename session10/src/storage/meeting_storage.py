from ..models.meeting_models import Meeting
from uuid import UUID

meeeting_storage: dict[UUID, Meeting] = {}
