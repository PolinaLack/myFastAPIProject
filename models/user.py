from pydantic import BaseModel


class User(BaseModel):
    name: str
    holis_ids: list[int]

