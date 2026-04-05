from fastapi import FastAPI
from app.api.routers import meetings, action_items

app = FastAPI(
    title="Meeting Note Assistant API",
    version="0.2.0",
    description="Meetings, notes, and action items management",
)

app.include_router(meetings.router)
app.include_router(action_items.router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/dashboard/summary")
def dashboard_summary():
    return {
        "total_meetings": len(meetings.DB),
        "total_action_items": sum(
            len(items) for items in action_items.ACTION_DB.values()
        ),
    }
