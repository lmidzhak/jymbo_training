from pydantic import BaseModel


class BaseModelWithTime(BaseModel):
    created_at: int
    updated_at: int
