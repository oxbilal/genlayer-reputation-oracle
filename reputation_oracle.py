# { "Depends": "py-genlayer:test" }

from genlayer import *

class ReputationOracle(gl.Contract):
    last_report: str

    def __init__(self):
        self.last_report = ""

    @gl.public.write
    def evaluate_reputation(self, profile_source: str, claim: str):
        input_data = f"""
PROFILE SOURCE:
{profile_source}

CLAIM TO CHECK:
{claim}
"""
        result = gl.eq_principle.prompt_non_comparative(
            lambda: input_data,
            task="Evaluate the reputation claim using only the profile source. Return: VERIFIED, RISKY, or UNCLEAR with one short reason.",
            criteria="""
            Use only the provided profile source.
            The answer must start with VERIFIED, RISKY, or UNCLEAR.
            Include one short reason.
            Do not invent facts outside the source.
            """
        )
        self.last_report = result

    @gl.public.view
    def get_last_report(self) -> str:
        return self.last_report
