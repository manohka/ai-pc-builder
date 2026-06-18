from pydantic import BaseModel


class RecommendationRequest(BaseModel):

    component: str
