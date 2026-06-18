from pydantic import BaseModel


class RecommendationResponse(BaseModel):

    cpu: str | None

    motherboard: str | None

    ram: str | None

    psu: str | None
