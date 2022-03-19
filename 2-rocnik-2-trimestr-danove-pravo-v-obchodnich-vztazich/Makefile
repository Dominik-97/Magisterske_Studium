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
		pandoc --wrap=preserve -F mermaid-filter -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../pdf/$@ $< ; \
	else \
		pandoc --toc --wrap=preserve -F mermaid-filter -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../pdf/$@ $< ; \
	fi

%.docx: %.md
	if grep -q no_TOC '$<'; then \
		pandoc --wrap=preserve -F mermaid-filter -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../docx/$@ $< ; \
	else \
		pandoc --toc --wrap=preserve -F mermaid-filter -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../docx/$@ $< ; \
	fi

clean:
	rm -f *.pdf *.docx
