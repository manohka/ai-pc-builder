class PromptBuilder:

    def build_prompt(
        self,
        build
    ):

        return f"""
Explain why the following PC build was selected.

CPU:
{build['cpu']}

Motherboard:
{build['motherboard']}

RAM:
{build['ram']}

PSU:
{build['psu']}

Explain:
1. Why the CPU was chosen
2. Why the motherboard is compatible
3. Why the RAM is compatible
4. Why the PSU is suitable

Keep the explanation simple and beginner friendly.
"""
