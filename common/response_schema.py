from typing import TypeVar, Generic

from pydantic import BaseModel

DataType = TypeVar("DataType")


class IResponseBase(BaseModel, Generic[DataType]):
    message: str = ""
    meta: dict | None = {}
    data: DataType | None = None


class IGetResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str | None = "Data got correctly"


class IPostResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str | None = "Data created correctly"


class IPutResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str | None = "Data updated correctly"


class IDeleteResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str | None = "Data deleted correctly"


def create_response(
        data: DataType,
        message: str | None = None,
        meta: dict | None = None,
) -> dict[str, DataType | str | None]:
    if message is None:
        return {"data": data, "meta": meta}
    return {"data": data, "message": message, "meta": meta}
