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
from collections import defaultdict
from pathlib import Path


def main():
    """Generates an HTML page with voice samples (for github.io page)"""
    if len(sys.argv) < 2:
        print("Usage: create_sample_html.py <SAMPLES_DIR>", file=sys.stderr)
        sys.exit(1)

    print('<html lang="en">')
    print("<head>")
    print('<meta charset="utf-8"><title>Mimic 3 Voice Samples</title>')
    print(
        """<style>
h2 {
    background-color: #22A7F0;
    color: #FFF;
    padding: 5px;
}
table {
    border-collapse: collapse;
    font-family: sans-serif;
}

table thead tr {
    background-color: #8CE0FE;
    text-align: left;
}
table th,
table td {
    padding: 12px 15px;
}
table tbody tr {
    border: 1px solid #eee;
}
table tbody tr:nth-of-type(even) {
    background-color: #F1F3F4;
}


</style>"""
    )
    print("</head>")

    print("<body>")
    print("<h1>Mimic 3 Voice Samples</h1>")
    print(
        '<p>Voices samples trained with <a href="https://github.com/MycroftAI/mimic3">Mimic 3</a> for use on the <a href="https://mycroft.ai/product/mark-ii/">Mark II</a>.</p>'
    )
    print(
        """<p>
        These voices were trained in a low quality mode to run faster than realtime on a Raspberry Pi 4.
        On a 64-bit Raspberry Pi OS, a realtime factor (RTF) of 0.5 is average.
        </p>"""
    )
    print("<hr>")

    local_dir = Path(sys.argv[1])

    # language -> voice name -> samples dir
    voices = defaultdict(dict)

    # local/<LANGUAGE>/<VOICE>
    for lang_dir in sorted(Path(local_dir).iterdir()):
        if (not lang_dir.is_dir()) or lang_dir.name.startswith("."):
            continue

        language = lang_dir.name

        for voice_dir in sorted(lang_dir.iterdir()):
            if (not voice_dir.is_dir()) or voice_dir.name.startswith("."):
                continue

            test_sentences = voice_dir / "sample.txt"
            if not test_sentences.is_file():
                print("Missing", test_sentences, file=sys.stderr)
                continue

            voices[language][voice_dir.name] = voice_dir

    # Print table of contents
    print("<ul>")
    for language, lang_voices in voices.items():
        print("<li>", f'<a href="#{language}">', language, "</a>")

        print("<ul>")
        for voice_name in lang_voices:
            print(
                "<li>",
                f'<a href="#{language}_{voice_name}">',
                voice_name,
                "</a>",
                "</li>",
            )
        print("</ul>")

        print("</li>")

    print("</ul>")
    print("<hr>")

    # Print samples
    for language, lang_voices in voices.items():
        print(f'<h2 id="{language}">', language, "</h2>")

        for voice_name, samples_dir in lang_voices.items():
            sample_text_path = samples_dir / "sample.txt"
            with open(sample_text_path, "r", encoding="utf-8") as sample_text_file:
                text = sample_text_file.read().strip()

            print(f'<h3 id="{language}_{voice_name}">', voice_name, "</h3>")
            print("<p>", text, "</p>")

            speakers_path = samples_dir / "speakers.txt"
            speakers = []
            if speakers_path.is_file():
                with open(speakers_path, "r", encoding="utf-8") as speakers_file:
                    for line in speakers_file:
                        line = line.strip()
                        if line:
                            speakers.append(line)

            if not speakers:
                # Single speaker
                sample_path = samples_dir / "sample.wav"
                print(
                    f'<audio preload="none" controls src="{sample_path}"></audio>',
                )
            else:
                # Multi speaker
                print("<table>")
                print("<thead><tr><th>Id</th><th>Speaker</th><th>Sample</th></tr></thead>")

                for speaker_idx, speaker in enumerate(speakers):
                    sample_path = samples_dir / f"sample_{speaker}.wav"
                    assert sample_path.is_file(), sample_path

                    print("<tr>")
                    print("<td>", speaker_idx, "</td>")
                    print("<td>", speaker, "</td>")
                    print(
                        "<td>",
                        f'<audio preload="none" controls src="{sample_path}"></audio>',
                        "</td>",
                    )
                    print("</tr>")

                print("<table>")

            print("<br>")

        # ---------------------------------------------------------------------

        print("<br>")
        print("<hr>")

    print("</body>")
    print("</html>")


if __name__ == "__main__":
    main()
