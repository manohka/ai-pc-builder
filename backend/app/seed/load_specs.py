import json
from pathlib import Path

import app.models

from app.database.database import SessionLocal
from app.models.component import Component
from app.models.component_spec import ComponentSpec


def main():

    db = SessionLocal()

    try:

        seed_file = (
            Path(__file__)
            .resolve()
            .parents[3]
            / "seed"
            / "specs.json"
        )

        with open(seed_file, "r") as file:
            specs = json.load(file)

        for item in specs:

            component = (
                db.query(Component)
                .filter(
                    Component.name == item["component_name"]
                )
                .first()
            )

            if component is None:
                continue

            existing_spec = (
                db.query(ComponentSpec)
                .filter(
                    ComponentSpec.component_id == component.id,
                    ComponentSpec.spec_key == item["spec_key"]
                )
                .first()
            )

            if existing_spec:
                continue

            spec = ComponentSpec(
                component_id=component.id,
                spec_key=item["spec_key"],
                spec_value=item["spec_value"]
            )

            db.add(spec)

        db.commit()

        print(
            f"Loaded {len(specs)} specs."
        )

    finally:
        db.close()


if __name__ == "__main__":
    main()
