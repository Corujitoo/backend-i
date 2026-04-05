import logging
from uuid import uuid4
from app.domain.models import Meeting
from app.services.memory_store import meetings, save_meetings
from app.core.errors import NotFoundError

logger = logging.getLogger(__name__)


def create_meeting(title: str, date: str, owner: str) -> Meeting:
    meeting = Meeting(id=str(uuid4()), title=title, date=date, owner=owner)
    meetings.append(meeting)
    save_meetings(meetings)
    logger.info("Creating meeting", extra={"title": title, "date": date})
    return meeting


def list_meetings() -> list[Meeting]:
    logger.info("Listing meetings")
    return meetings


def get_meeting(meeting_id: str) -> Meeting:
    for meeting in meetings:
        if meeting.id == meeting_id:
            return meeting
    raise NotFoundError(f"Meeting {meeting_id} not found")


def delete_meeting(meeting_id: str) -> None:
    global meetings
    meetings = [m for m in meetings if m.id != meeting_id]
    save_meetings(meetings)
    logger.info("Deleting meeting", extra={"meeting_id": meeting_id})
