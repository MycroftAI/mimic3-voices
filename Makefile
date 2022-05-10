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
.PHONY: all metadata check-configs

SHELL := bash

all:
	python3 scripts/create_samples.py samples
	python3 scripts/create_sample_html.py samples > index.html
	VOICES="$$(python3 scripts/create_readme.py voices)" envsubst < README.md.template > README.md

metadata:
	python3 scripts/create_metadata.py voices > ../mimic3/mimic3_tts/voices.json

check-configs:
	find voices -name 'config.json' -type f -exec jq . {} \;
