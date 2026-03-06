
from datetime import datetime
from http.client import HTTPException
from fastapi import FastAPI
from api.models import Meeting, MeetingRequest, MeetingResponse



api = FastAPI()


@api.get("/", response_model=list[Meeting])
def list_meeting(title:str = "", owner:str = "", date:datetime | None = None) -> list[Meeting]:
    return list[Meeting]()



@api.post("/", response_model=MeetingResponse)
def create_meeting(meeting:MeetingRequest):
    title_received = meeting.title
    owner_received = meeting.owner
    datetime_received = meeting.date
    id = "1234"
    return MeetingResponse(id=id)



@api.get("/{meeting_id}", response_model=Meeting)
def get_meeting(meeting_id:str):
    if meeting_id not in db_meetings:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return db_meetings[meeting_id]
                       

    


    #GET = Obtem recursos
    #POST = Cria novos 
    #PUT = Atualiza existentes 
    #DELETE = Remove-os