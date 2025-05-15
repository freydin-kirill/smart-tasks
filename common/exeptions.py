from fastapi import HTTPException
from starlette import status


class BadRequestException(HTTPException):
    def __init__(self,
                 detail: str = "Bad Request",
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class InactiveUserException(HTTPException):
    def __init__(self,
                 detail: str = "Inactive user",
                 status_code: int = status.HTTP_400_BAD_REQUEST,
                 headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class IncorrectCredentialsException(HTTPException):
    def __init__(self,
                 detail: str = "Incorrect username or password",
                 status_code: int = status.HTTP_401_UNAUTHORIZED,
                 headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class InvalidCredentialsException(HTTPException):
    def __init__(self,
                 detail: str = "Invalid authentication credentials",
                 status_code: int = status.HTTP_401_UNAUTHORIZED,
                 headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class NotFoundException(HTTPException):
    def __init__(self,
                 detail: str = "Not Found",
                 status_code: int = status.HTTP_404_NOT_FOUND,
                 headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class InternalServerErrorException(HTTPException):
    def __init__(self,
                 detail: str = "Internal Server Error",
                 status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
                 headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)