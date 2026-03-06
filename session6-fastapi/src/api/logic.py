from api.models import Meeting
import json

def salvar_meeting(meeting: Meeting):
    with open("meeting.json", "w") as f:
        json.dump(meeting.dict(), f)
