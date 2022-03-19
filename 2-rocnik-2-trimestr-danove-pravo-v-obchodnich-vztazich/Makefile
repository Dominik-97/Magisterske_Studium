## Markdown extension (e.g. md, markdown, mdown).
MEXT = md
## All markdown files in the working directory
SRC := $(wildcard *.$(MEXT))
SRC := $(filter-out README.md, $(SRC))


DOCX=$(SRC:.md=.docx)
PDFS=$(SRC:.md=.pdf)


all: $(PDFS)	$(DOCX)
pdf: clean $(PDFS)
docx: clean $(DOCX)

# Separator for these lines need to start with a hard tab, not 4 spaces!
%.pdf: %.md
	if grep -q no_TOC '$<'; then \
		./pandoc-with-mermaid.sh run_pdf_without_toc pdf/$@ 2-rocnik-2-trimestr-danove-pravo-v-obchodnich-vztazich/$< ; \
	else \
		./pandoc-with-mermaid.sh run_pdf_with_toc pdf/$@ 2-rocnik-2-trimestr-danove-pravo-v-obchodnich-vztazich/$< ; \
	fi

%.docx: %.md
	if grep -q no_TOC '$<'; then \
		./pandoc-with-mermaid.sh run_docx_without_toc docx/$@ 2-rocnik-2-trimestr-danove-pravo-v-obchodnich-vztazich/$< ; \
	else \
		./pandoc-with-mermaid.sh run_docx_with_toc docx/$@ 2-rocnik-2-trimestr-danove-pravo-v-obchodnich-vztazich/$< ; \
	fi

clean:
	rm -f *.pdf *.docx
