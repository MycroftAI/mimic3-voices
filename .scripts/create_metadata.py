#!/usr/bin/env python3
# Copyright 2022 Mycroft AI Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import hashlib
import json
import sys
from pathlib import Path

_BLOCK_SIZE = 4096


def main():
    """Generate JSON output with a summary of all voice files"""
    # {
    #   "<lang>/<voice>": {
    #     "files": {
    #       "relative/path": {
    #         "size_bytes": size in bytes,
    #         "sha256_sum": sha256 hash
    #       }
    #     },
    #     "speakers": [],
    #     "properties": {}
    #   }
    # }
    if len(sys.argv) < 2:
        print("Usage: create_metadata.py <VOICES_DIR>", file=sys.stderr)
        sys.exit(1)

    voices_dir = Path(sys.argv[1])
    voices = {}

    # Directory structure is <language>/<voice name>
    for lang_dir in sorted(voices_dir.iterdir()):
        if not lang_dir.is_dir() or lang_dir.name.startswith("."):
            continue

        lang = lang_dir.name

        for voice_dir in sorted(lang_dir.iterdir()):
            if not voice_dir.is_dir() or voice_dir.name.startswith("."):
                continue

            voice = voice_dir.name
            voice_key = f"{lang}/{voice}"
            voice_files = {}

            # Hash all files for this voice (recursive)
            for voice_file_path in sorted(voice_dir.rglob("*")):
                if not voice_file_path.is_file() or voice_file_path.name.startswith(
                    "."
                ):
                    continue

                num_bytes = voice_file_path.stat().st_size
                rel_path = str(voice_file_path.relative_to(voice_dir))

                current_hash = hashlib.sha256()
                with open(voice_file_path, "rb") as voice_file:
                    # Read in blocks in case file is very large
                    block = voice_file.read(_BLOCK_SIZE)
                    while len(block) > 0:
                        current_hash.update(block)
                        block = voice_file.read(_BLOCK_SIZE)

                # Report number of bytes in the file and its sha256 sum
                voice_files[rel_path] = {
                    "size_bytes": num_bytes,
                    "sha256_sum": current_hash.hexdigest(),
                }

            # Load speaker names (for multi-speaker voices)
            speakers = []
            speakers_path = voice_dir / "speakers.txt"
            if speakers_path.is_file():
                with open(speakers_path, "r", encoding="utf-8") as speakers_file:
                    for line in speakers_file:
                        line = line.strip()
                        if line:
                            speakers.append(line)

            voices[voice_key] = {
                "files": voice_files,
                "speakers": speakers,
                "properties": {},
            }

    json.dump(voices, sys.stdout, indent=4)


if __name__ == "__main__":
    main()
