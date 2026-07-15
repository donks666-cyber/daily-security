PY = venv/bin/python
PELICAN = venv/bin/pelican
PELICANOPTS =

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBCONF = $(BASEDIR)/publishconf.py

PORT = 8000
SERVER = $(BASEDIR)/output

help:
	@echo 'Makefile for 去社会安全                                                '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html        (re)generate the web site                          '
	@echo '   make clean       remove the generated files                         '
	@echo '   make regenerate  regenerate files upon modification                '
	@echo '   make publish     generate using production settings                '
	@echo '   make serve       serve project at http://localhost:8000            '
	@echo '   make devserver   start dev server with auto-reload                 '
	@echo '   make stopserver   stop auto-reload server                          '
	@echo '   make search      build stork search index                          '
	@echo '   make all         build site + search index                         '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

search:
	$(PY) generate_search_index.py

all: html search

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -r

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBCONF) $(PELICANOPTS)
	$(PY) generate_search_index.py

serve:
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)

devserver:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)

stopserver:
	kill `cat $(SERVER)/srv.pid`
	@rm -f $(SERVER)/srv.pid

.PHONY: help html clean regenerate publish serve devserver stopserver search all
