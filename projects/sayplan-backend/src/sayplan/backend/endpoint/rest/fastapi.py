from fastapi import APIRouter
from sayplan.backend.leaderboard.rest.fastapi import router as leaderboard_router

endpoint = APIRouter(prefix="/api/v1")

