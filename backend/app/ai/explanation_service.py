from app.ai.prompt_builder import (
    PromptBuilder
)


class ExplanationService:

    def __init__(self):

        self.prompt_builder = (
            PromptBuilder()
        )

    def explain(
        self,
        build
    ):

        prompt = (
            self.prompt_builder
            .build_prompt(build)
        )

        explanation = (
            f"The {build['cpu']} was selected "
            f"because it provides a balanced "
            f"performance level for this build. "

            f"The motherboard was selected "
            f"because it supports the CPU "
            f"socket requirements. "

            f"The RAM is compatible with the "
            f"motherboard and CPU memory type. "

            f"The PSU provides sufficient power "
            f"for the selected components."
        )

        return explanation
