TEXFILE := Strategický_audit # Change name here
BIBFILE := Zdroje/Zdroje.bib # Change bibliography here
TEXENGINE=pdflatex
BIBLATEX=biber
BUILDFLAGS=-output-directory=out
FOLDER=out
BUILDTEX=$(TEXENGINE) $(BUILDFLAGS) $(TEXFILE)

.PHONY: all
.PHONY: prepareBib
.PHONY: clear
.PHONY: clean
.PHONY: prepareOut
.PHONY: buildStandalone

buildStandalone: prepareOut
	$(BUILDTEX)
	$(BIBLATEX) $(FOLDER)/$(TEXFILE)
	$(BUILDTEX)
	$(BUILDTEX)
	cp out/$(TEXFILE).pdf .

build: prepareBib prepareOut
	$(BUILDTEX)
	$(BIBLATEX) $(FOLDER)/$(TEXFILE)
	$(BUILDTEX)
	$(BUILDTEX)
	cp out/$(TEXFILE).pdf .

prepareBib:
	python3 prepare_bib.py $(BIBFILE)

prepareOut:
	./create_subdirectories.sh

clear: clean
	@rm -f $(TEXFILE).pdf; \

clean:
	@rm -rf $(FOLDER);

help:
	@echo "buildStandalone:    Generate pdf file without preparing the bib file."; \
	 echo "build:    	   Generate pdf file."; \
	 echo "clear:    	   Delete all generated files."; \
	 echo "clean:    	   Delete all temporary files."; \
	 echo "help:     	   Print help for Makefile."

all: build clean
