import app.models

from app.database.database import SessionLocal

from app.models.component import Component
from app.models.component_alias import ComponentAlias
from app.models.recommendation_rule import RecommendationRule


class CandidateGenerator:

    def __init__(self):

        self.db = SessionLocal()

    def generate(self, user_input: str):

        alias = (
            self.db.query(ComponentAlias)
            .filter(
                ComponentAlias.alias.ilike(
                    user_input.lower()
                )
            )
            .first()
        )

        if alias is None:

            return []

        source_component = (
            self.db.query(Component)
            .filter(
                Component.id == alias.component_id
            )
            .first()
        )

        if source_component is None:

            return []

        rule = (
            self.db.query(RecommendationRule)
            .filter(
                RecommendationRule.source_component_type
                == source_component.component_type,

                RecommendationRule.source_tier
                == source_component.tier
            )
            .first()
        )

        if rule is None:

            return []

        candidates = (
            self.db.query(Component)
            .filter(
                Component.component_type
                == rule.target_component_type,

                Component.tier >= rule.min_target_tier,

                Component.tier <= rule.max_target_tier
            )
            .all()
        )

        return candidates
