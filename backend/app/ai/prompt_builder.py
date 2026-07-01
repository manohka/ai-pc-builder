class PromptBuilder:

    def build_prompt(
        self,
        build
    ):

        return f"""
You are an expert PC hardware consultant.

Explain why the following PC build
was selected.

CPU:
{build['cpu']}

Motherboard:
{build['motherboard']}

RAM:
{build['ram']}

PSU:
{build['psu']}

Requirements:

- Explain compatibility.
- Explain performance balance.
- Explain memory selection.
- Explain PSU suitability.
- Keep explanation under 120 words.
- Use beginner friendly language.
"""
