from typing import Optional, List

from starlette import status
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class ErrorInfoModel:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __repr__(self):
        return f"code:{self.code},message:{self.message}"
    

class ErrorInfoContainer:
    unhandled_error = ErrorInfoModel(code=1, message="Internal server error")


class ExceptionHandlers:
    @staticmethod
    def unhandled_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ExceptionHandlers.__get_error_content(
                error_info=ErrorInfoContainer.unhandled_error,
            ),
        )
    
    @staticmethod
    def __get_error_content(error_info: ErrorInfoModel, error_detail: Optional[str] = None):
        return jsonable_encoder(
            dict(
                error_code=error_info.code,
                error_message=error_info.message,
                error_detail=error_detail if error_detail else error_info.message,
            )
        )