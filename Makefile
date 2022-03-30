.PHONY: all metadata

all:
	python3 scripts/create_samples.py samples
	python3 scripts/create_sample_html.py samples > index.html

metadata:
	python3 scripts/create_metadata.py voices > ../mimic3/mimic3-tts/mimic3_tts/voices.json
