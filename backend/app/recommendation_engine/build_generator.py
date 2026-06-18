import app.models

from app.database.database import SessionLocal

from app.models.component import Component

from app.recommendation_engine.candidate_generator import CandidateGenerator
from app.recommendation_engine.compatibility_service import CompatibilityService


class BuildGenerator:

    def __init__(self):

        self.db = SessionLocal()

        self.candidate_generator = CandidateGenerator()

        self.compatibility_service = CompatibilityService()

    def generate_build(
        self,
        user_input
    ):

        cpu_candidates = (
            self.candidate_generator.generate(
                user_input
            )
        )

        if not cpu_candidates:

            return None

        cpu = cpu_candidates[0]

        socket = (
            self.compatibility_service.get_spec(
                cpu.id,
                "socket"
            )
        )

        memory_type = (
            self.compatibility_service.get_spec(
                cpu.id,
                "memory_type"
            )
        )

        motherboard = (
            self.db.query(Component)
            .filter(
                Component.component_type
                == "MOTHERBOARD"
            )
            .all()
        )

        motherboard = next(
            (
                board
                for board in motherboard
                if self.compatibility_service.get_spec(
                    board.id,
                    "socket"
                )
                == socket
            ),
            None
        )

        ram = (
            self.db.query(Component)
            .filter(
                Component.component_type
                == "RAM"
            )
            .all()
        )

        ram = next(
            (
                item
                for item in ram
                if self.compatibility_service.get_spec(
                    item.id,
                    "memory_type"
                )
                == memory_type
            ),
            None
        )

        psu = (
            self.db.query(Component)
            .filter(
                Component.component_type
                == "PSU"
            )
            .first()
        )

        return {
            "cpu": cpu.name,
            "motherboard":
                motherboard.name
                if motherboard
                else None,
            "ram":
                ram.name
                if ram
                else None,
            "psu":
                psu.name
                if psu
                else None
        }
