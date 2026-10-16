#!/usr/bin/env python3
"""Update the pinned upstream Fullsend review harness when a newer commit exists."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


REPOSITORY = "fullsend-ai/agents"
REVIEW_PATH = Path(".fullsend/harness/review.yaml")
COMMIT_API = f"https://api.github.com/repos/{REPOSITORY}/commits/main"
RAW_REVIEW = "https://raw.githubusercontent.com/fullsend-ai/agents/{sha}/harness/review.yaml"
BASE_PATTERN = re.compile(
    r"^(base:\s+https://raw\.githubusercontent\.com/fullsend-ai/agents/)"
    r"([0-9a-f]{40})(/harness/review\.yaml#sha256=)([0-9a-f]{64})(\s*)$",
    re.MULTILINE,
)


def fetch(url: str) -> bytes:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            return response.read()
    except (HTTPError, URLError) as error:
        raise RuntimeError(f"Unable to fetch {url}: {error}") from error


def latest_commit() -> str:
    try:
        data = json.loads(fetch(COMMIT_API))
    except json.JSONDecodeError as error:
        raise RuntimeError(f"GitHub returned invalid JSON for {COMMIT_API}") from error

    sha = data.get("sha")
    if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise RuntimeError(f"GitHub response did not contain a commit SHA: {data!r}")
    return sha


def main() -> int:
    if not REVIEW_PATH.is_file():
        print(f"Missing {REVIEW_PATH}", file=sys.stderr)
        return 1

    current = REVIEW_PATH.read_text(encoding="utf-8")
    match = BASE_PATTERN.search(current)
    if not match:
        print(f"Could not find the expected pinned review base in {REVIEW_PATH}", file=sys.stderr)
        return 1

    upstream_sha = latest_commit()
    current_sha = match.group(2)
    if upstream_sha == current_sha:
        print(f"Fullsend review harness is current at {current_sha}.")
        return 0

    review_url = RAW_REVIEW.format(sha=upstream_sha)
    digest = hashlib.sha256(fetch(review_url)).hexdigest()
    if digest == match.group(4):
        print(f"The upstream commit changed, but the review harness content is unchanged ({digest}).")
        return 0

    replacement = f"{match.group(1)}{upstream_sha}{match.group(3)}{digest}{match.group(5)}"
    REVIEW_PATH.write_text(current[: match.start()] + replacement + current[match.end() :], encoding="utf-8")
    print(f"Updated Fullsend review harness: {current_sha} -> {upstream_sha}")
    print(f"Updated review harness content hash: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
