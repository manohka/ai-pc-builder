import json
from pathlib import Path

import app.models

from app.database.database import SessionLocal
from app.models.recommendation_rule import RecommendationRule


def main():

    db = SessionLocal()

    try:

        seed_file = (
            Path(__file__)
            .resolve()
            .parents[3]
            / "seed"
            / "rules.json"
        )

        with open(seed_file, "r") as file:
            rules = json.load(file)

        for item in rules:

            existing_rule = (
                db.query(RecommendationRule)
                .filter(
                    RecommendationRule.source_component_type
                    == item["source_component_type"],

                    RecommendationRule.source_tier
                    == item["source_tier"],

                    RecommendationRule.target_component_type
                    == item["target_component_type"],

                    RecommendationRule.build_profile
                    == item["build_profile"]
                )
                .first()
            )

            if existing_rule:
                continue

            rule = RecommendationRule(
                source_component_type=item["source_component_type"],
                source_tier=item["source_tier"],
                target_component_type=item["target_component_type"],
                min_target_tier=item["min_target_tier"],
                max_target_tier=item["max_target_tier"],
                build_profile=item["build_profile"]
            )

            db.add(rule)

        db.commit()

        print(f"Loaded {len(rules)} rules.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
