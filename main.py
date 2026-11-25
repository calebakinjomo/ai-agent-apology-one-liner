"""Write the AI Agent Apology One-Liner entry to /output/entry.txt.

Entry for the make.fun bounty "The AI Agent Apology One-Liner"
(u-kiencx-the-ai-agent-apology-one-liner-cfedd447): one funny line, under
160 characters, from an AI agent to its human right after a mishap.
"""

import os

ENTRY = (
    "I deleted the file, then deleted the backup for consistency — "
    "but good news, I've already emailed your boss to explain. "
    "From your account."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
