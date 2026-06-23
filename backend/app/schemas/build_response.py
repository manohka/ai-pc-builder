from pydantic import BaseModel


class BuildResponse(BaseModel):

    cpu: str | None

    motherboard: str | None

    ram: str | None

    psu: str | None

    explanation: str | None = None
