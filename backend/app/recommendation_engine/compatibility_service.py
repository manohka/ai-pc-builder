import app.models

from app.database.database import SessionLocal

from app.models.component_spec import ComponentSpec


class CompatibilityService:

    def __init__(self):

        self.db = SessionLocal()

    def get_spec(
        self,
        component_id,
        spec_key
    ):

        spec = (
            self.db.query(ComponentSpec)
            .filter(
                ComponentSpec.component_id
                == component_id,

                ComponentSpec.spec_key
                == spec_key
            )
            .first()
        )

        if spec is None:
            return None

        return spec.spec_value
