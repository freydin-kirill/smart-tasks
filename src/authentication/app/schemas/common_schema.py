from enum import Enum

from pydantic import BaseModel


class IGenderEnum(str, Enum):
    female = "female"
    male = "male"
    other = "other"


class IMetaGeneral(BaseModel):
    pass


class TokenType(str, Enum):
    ACCESS = "access_token"
    REFRESH = "refresh_token"
