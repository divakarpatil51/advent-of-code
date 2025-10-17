import os
from pathlib import Path


def read_input(year: str, day: str, env: str | None = None) -> str:
    """
    Read input data for Advent of Code problems.

    Args:
        year: Year (e.g., "2023", "2024")
        day: Day (e.g., "1", "2")
        env: Environment ("real" or "test"). If None, uses AOC_ENV environment variable.

    Returns:
        Input data as string
    """
    if env is None:
        env = os.getenv("AOC_ENV", "real")

    input_path = Path.cwd() / "inputs" / year / env / f"{day}.txt"
    return input_path.read_text().strip()
