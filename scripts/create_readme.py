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
import json
import sys
from pathlib import Path

from shared import LANG_NAMES


def main():
    """Generate voices table for README"""
    if len(sys.argv) < 2:
        print("Usage: create_readme.py <VOICES_DIR>", file=sys.stderr)
        sys.exit(1)

    print(
        """<table>
<thead>
<tr>
<th>Key</th>
<th>Language</th>
<th>Dataset</th>
<th>Speakers</th>
<th>Version</th>
<th>Phonemizer</th>
<th>License</th>
</tr>
<tbody>"""
    )

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
            voice_sources = list(
                filter(
                    None,
                    (voice_dir / "SOURCE").read_text(encoding="utf-8").splitlines(),
                )
            )

            assert voice_sources, voice_key

            # Update README for voice
            with open(
                voice_dir / "README.md.in", "r", encoding="utf-8"
            ) as readme_in_file, open(
                voice_dir / "README.md", "w", encoding="utf-8"
            ) as readme_out_file:
                # Copy contents
                for line in readme_in_file:
                    line = line.strip()
                    print(line, file=readme_out_file)

                # Add phonemes
                print("", file=readme_out_file)
                print("", file=readme_out_file)
                print("## Phonemes", file=readme_out_file)
                print("", file=readme_out_file)

                print(
                    "<table><thead><th>&nbsp;</th><th>Phoneme</th><th>Description</th></thead>",
                    file=readme_out_file,
                )
                with open(
                    voice_dir / "phonemes.txt", "r", encoding="utf-8"
                ) as phonemes_file:
                    for line in phonemes_file:
                        line = line.strip("\r\n")
                        if not line:
                            continue

                        phoneme_num, phoneme = line.split(maxsplit=1)
                        description = ""

                        if phoneme_num == "0":
                            description = "padding"
                        elif phoneme == "^":
                            description = "start utterance"
                        elif phoneme == "$":
                            description = "end utterance"
                        elif phoneme in {"|", ","}:
                            description = "short pause (minor break)"
                        elif phoneme in {"‖", "."}:
                            description = "long pause (major break)"
                        elif phoneme in {"#", " "}:
                            description = "word break"
                        elif phoneme == "ˈ":
                            description = "primary stress"
                        elif phoneme == "ˌ":
                            description = "secondary stress"
                        elif phoneme == "ː":
                            description = "elongation"
                        elif phoneme == "·":
                            description = "silence"

                        print("<tr>", file=readme_out_file)
                        print("<td>", phoneme_num, "</td>", file=readme_out_file)
                        print("<td>", phoneme, "</td>", file=readme_out_file)
                        print("<td>", description, "</td>", file=readme_out_file)
                        print("</tr>", file=readme_out_file)

                print("</table>", file=readme_out_file)

            # Phonemizer
            with open(voice_dir / "config.json", "r", encoding="utf-8") as config_file:
                voice_config = json.load(config_file)

            phonemizer = voice_config.get("phonemizer", "")
            phonemizer_link = "#"

            if phonemizer == "gruut":
                phonemizer_link = "https://github.com/rhasspy/gruut/"
            elif phonemizer == "espeak":
                phonemizer_link = "https://github.com/espeak-ng/espeak-ng/"
            elif phonemizer == "epitran":
                phonemizer_link = "https://github.com/dmort27/epitran/"
            elif phonemizer == "symbols":
                phonemizer_link = "voices/{voice_key}/README.md#phonemes"

            # Load speaker names (for multi-speaker voices)
            speakers = []
            speakers_path = voice_dir / "speakers.txt"
            if speakers_path.is_file():
                with open(speakers_path, "r", encoding="utf-8") as speakers_file:
                    for line in speakers_file:
                        line = line.strip()
                        if line:
                            speakers.append(line)

            lang_name = LANG_NAMES.get(lang, lang)
            if isinstance(lang_name, tuple):
                lang_name = f"{lang_name[0]} ({lang_name[1]})"

            print(
                f"""<tr>
<td><a href="voices/{voice_key}"><tt>{voice_key}</tt></a></td>
<td>{lang_name}</td>"""
            )

            if len(voice_sources) == 1:
                print(f'<td><a href="{voice_sources[0]}">View</a></td>')
            else:
                print("<td>")
                for i, source in enumerate(voice_sources):
                    print(f'<a href="{source}">[{i+1}]</a>')
                print("</td>")

            voice_version = (voice_dir / "VERSION").read_text(encoding="utf-8").strip()

            print(
                f"""<td>{max(1, len(speakers))}</td>
    <td>{voice_version}</td>
    <td><a href="{phonemizer_link}">{phonemizer}</a></td>
    <td><a href="voices/{voice_key}/LICENSE">View</a></td>
</tr>"""
            )

    print(
        """</tbody>
</table>"""
    )


if __name__ == "__main__":
    main()
