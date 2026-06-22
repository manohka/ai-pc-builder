from typing import List

from fastapi import APIRouter

from app.schemas.recommendation_request import (
    RecommendationRequest
)

from app.schemas.build_response import (
    BuildResponse
)

from app.recommendation_engine.build_generator import (
    BuildGenerator
)

router = APIRouter()

generator = BuildGenerator()


@router.post(
    "/recommendations",
    response_model=List[BuildResponse]
)
def recommend_build(
    request: RecommendationRequest
):

    builds = generator.generate_builds(
        request.component
    )

    return builds
