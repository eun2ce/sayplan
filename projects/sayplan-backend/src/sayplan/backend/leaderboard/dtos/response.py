from sayplan.shared_kernel.infra.fastapi.dtos.response import ResponseDto
from .schemas import LreaderBoardReadSchema


LeaderBoardResponse = ResponseDto[list[LreaderBoardReadSchema]]
