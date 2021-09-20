SITE=$(HOME)/Sites/classes 
REMOTE_CONFIG=/tmp/remote_config.yml

all: .all

.all: _data/classes.json
	rm -f $(REMOTE_CONFIG)
	sed -e 's/^remote_theme/#remote_theme/' -e 's/^#theme:/theme:/' _config.yml > $(REMOTE_CONFIG)
	bundle exec jekyll build --config $(REMOTE_CONFIG) --destination $(SITE) --incremental --watch

_data/classes.json: etc/y2021.xlsx etc/y2022.xlsx
	etc/sheet.py
