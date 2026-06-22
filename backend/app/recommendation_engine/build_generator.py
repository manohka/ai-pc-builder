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

    def generate_builds(self, user_input):

        cpu_candidates = self.candidate_generator.generate(
            user_input
        )

        builds = []

        for cpu in cpu_candidates:

            socket = self.compatibility_service.get_spec(
                cpu.id,
                "socket",
            )

            memory_type = self.compatibility_service.get_spec(
                cpu.id,
                "memory_type",
            )

            motherboards = (
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
                    for board in motherboards
                    if self.compatibility_service.get_spec(
                        board.id,
                        "socket",
                    )
                    == socket
                ),
                None,
            )

            ram_options = (
                self.db.query(Component)
                .filter(
                    Component.component_type == "RAM"
                )
                .all()
            )

            ram = next(
                (
                    item
                    for item in ram_options
                    if self.compatibility_service.get_spec(
                        item.id,
                        "memory_type",
                    )
                    == memory_type
                ),
                None,
            )

            psu = (
                self.db.query(Component)
                .filter(
                    Component.component_type == "PSU"
                )
                .order_by(Component.tier)
                .first()
            )

            builds.append(
                {
                    "cpu": cpu.name,
                    "motherboard": (
                        motherboard.name
                        if motherboard
                        else None
                    ),
                    "ram": (
                        ram.name
                        if ram
                        else None
                    ),
                    "psu": (
                        psu.name
                        if psu
                        else None
                    ),
                }
            )

        return builds
