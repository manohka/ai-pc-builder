import json
from pathlib import Path

import app.models

from app.database.database import SessionLocal
from app.models.component import Component
from app.models.component_alias import ComponentAlias


def main():

    db = SessionLocal()

    try:

        seed_file = (
            Path(__file__)
            .resolve()
            .parents[3]
            / "seed"
            / "aliases.json"
        )

        with open(seed_file, "r") as file:
            aliases = json.load(file)

        for item in aliases:

            component = (
                db.query(Component)
                .filter(
                    Component.name == item["component_name"]
                )
                .first()
            )

            if component is None:
                continue

            existing_alias = (
                db.query(ComponentAlias)
                .filter(
                    ComponentAlias.alias == item["alias"]
                )
                .first()
            )

            if existing_alias:
                continue

            alias = ComponentAlias(
                component_id=component.id,
                alias=item["alias"]
            )

            db.add(alias)

        db.commit()

        print(
            f"Loaded {len(aliases)} aliases."
        )

    finally:
        db.close()


if __name__ == "__main__":
    main()
