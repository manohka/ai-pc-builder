import json
from pathlib import Path

import app.models

from app.database.database import SessionLocal
from app.models.component import Component


def main():

    db = SessionLocal()

    try:

        seed_file = (
            Path(__file__)
            .resolve()
            .parents[3]
            / "seed"
            / "components.json"
        )

        with open(seed_file, "r") as file:
            components = json.load(file)

        for item in components:

            exists = (
                db.query(Component)
                .filter(
                    Component.name == item["name"]
                )
                .first()
            )

            if exists:
                continue

            component = Component(
                name=item["name"],
                component_type=item["component_type"],
                brand=item["brand"],
                tier=item["tier"],
                price=item["price"]
            )

            db.add(component)

        db.commit()

        print(
            f"Loaded {len(components)} components."
        )

    finally:
        db.close()


if __name__ == "__main__":
    main()
