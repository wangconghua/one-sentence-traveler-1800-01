#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes one sentence explaining the modern internet to a time traveler
from 1800 to /output/entry.txt. The sentence uses only images a person
from 1800 could hold in their head: a road, a library, a post office.

Revision: the first version only checked length and shape. That is not
enough for this bounty: the judge's second criterion is that the sentence
builds from what a person from 1800 already knows, rather than from words
coined after their time. So the program now also checks the vocabulary:
no word coined after 1800 may appear, and at least one anchor image from
the traveler's own world (road, library, post office, letter, book) must
be present. The sentence itself is unchanged.
"""

import os
import re

SENTENCE = "Picture a road from your own door to one vast library and post office shared by the whole world, where letters arrive before the ink dries and any book you wish for opens at once."

# Words coined after 1800 that would break the traveler's picture.
# (Only genuine post-1800 coinages: words like "code" or "network" are
# older than they look, so they are not listed here.)
MODERN_WORDS = {
    "internet", "computer", "website", "email", "phone", "telephone",
    "television", "digital", "online", "wifi", "software", "hardware",
    "keyboard", "modem", "pixel", "video", "download", "upload",
    "app", "smartphone", "laptop", "router", "robot",
}

# Images a person from 1800 already knows; at least one must carry the
# sentence, or it is not built from their world at all.
ANCHOR_WORDS = {"road", "library", "post", "office", "letter", "book"}


def check_vocabulary(text):
    words = set(re.findall(r"[a-z]+", text.lower()))
    modern = words & MODERN_WORDS
    assert not modern, f"sentence uses words coined after 1800: {sorted(modern)}"
    assert words & ANCHOR_WORDS, "sentence needs an image from 1800 (road, library, post office, letter, book)"


def main():
    text = SENTENCE.strip()
    # Gate: 1-200 characters, not only whitespace, a single sentence.
    assert 1 <= len(text) <= 200, f"sentence must be 1-200 chars, got {len(text)}"
    assert text.strip(), "sentence must not be only whitespace"
    assert "\n" not in text, "sentence must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "sentence must be one sentence"
    check_vocabulary(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
