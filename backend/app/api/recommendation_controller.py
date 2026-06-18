from fastapi import APIRouter

from app.schemas.recommendation_request import (
    RecommendationRequest
)

from app.schemas.recommendation_response import (
    RecommendationResponse
)

from app.recommendation_engine.build_generator import (
    BuildGenerator
)

router = APIRouter()

generator = BuildGenerator()


@router.post(
    "/recommendations",
    response_model=RecommendationResponse
)
def recommend_build(
    request: RecommendationRequest
):

    build = generator.generate_build(
        request.component
    )

    return RecommendationResponse(
        cpu=build.get("cpu"),
        motherboard=build.get("motherboard"),
        ram=build.get("ram"),
        psu=build.get("psu")
    )
