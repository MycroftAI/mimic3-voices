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
import sys
from pathlib import Path

LANG_NAMES = {
    "af_ZA": "Afrikaans",
    "de_DE": "German",
    "en_UK": "English",
    "en_US": "English",
    "el_GR": "Greek",
    "es_ES": "Spanish",
    "fa": "Persian",
    "fi_FI": "Finnish",
    "fr_FR": "French",
    "hu_HU": "Hungarian",
    "it_IT": "Italian",
    "ko_KO": "Korean",
    "nl": "Dutch",
    "ru_RU": "Russian",
    "sw": "Kiswahili",
    "te_IN": "Telugu",
    "uk_UK": "Ukrainian",
    "vi_VN": "Vietnamese",
    "yo": "Yoruba",
}


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
<th>Quality</th>
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

            # Load speaker names (for multi-speaker voices)
            speakers = []
            speakers_path = voice_dir / "speakers.txt"
            if speakers_path.is_file():
                with open(speakers_path, "r", encoding="utf-8") as speakers_file:
                    for line in speakers_file:
                        line = line.strip()
                        if line:
                            speakers.append(line)

            print(
                f"""<tr>
<td><tt>{voice_key}</tt></td>
<td>{LANG_NAMES.get(lang, lang)}</td>"""
            )

            if len(voice_sources) == 1:
                print(f'<td><a href="{voice_sources[0]}">View</a></td>')
            else:
                print("<td>")
                for i, source in enumerate(voice_sources):
                    print(f'<a href="{source}">[{i+1}]</a>')
                print("</td>")

            print(
                f"""<td>{max(1, len(speakers))}</td>
    <td>low</td>
    <td><a href="voices/{voice_key}/LICENSE">View</a></td>
</tr>"""
            )

    print(
        """</tbody>
</table>"""
    )


if __name__ == "__main__":
    main()
