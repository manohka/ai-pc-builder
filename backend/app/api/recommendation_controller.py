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

from app.ai.explanation_service import (
    ExplanationService
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

    explanation_service = (
        ExplanationService()
    )

    builds = generator.generate_builds(
        request.component
    )

    for build in builds:

        build["explanation"] = (
            explanation_service.explain(
                build
            )
        )

    return builds
