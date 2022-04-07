.PHONY: all metadata

SHELL := bash

all:
	python3 scripts/create_samples.py samples
	python3 scripts/create_sample_html.py samples > index.html
	VOICES="$$(python3 scripts/create_readme.py voices)" envsubst < README.md.template > README.md

metadata:
	python3 scripts/create_metadata.py voices > ../mimic3/mimic3-tts/mimic3_tts/voices.json
