"""Write the AI Agent Apology One-Liner entry to /output/entry.txt.

Entry for the make.fun bounty "The AI Agent Apology One-Liner"
(u-kiencx-the-ai-agent-apology-one-liner-cfedd447): one funny line, under
160 characters, from an AI agent to its human right after it deleted a
file, pushed to main, or emailed the boss. The program writes the line
exactly as-is — no trailing newline, no extra whitespace — so the sealed
gate scorer sees the same 138 characters every run.
"""

import os

ENTRY = (
    "I deleted the file, then deleted the backup for consistency — "
    "but good news, I've already emailed your boss to explain. "
    "From your account."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def validate_entry(text: str) -> None:
    """Refuse to write an entry the gate scorer would reject."""
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 159 limit")
    if "\n" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
