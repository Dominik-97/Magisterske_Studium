## Markdown extension (e.g. md, markdown, mdown).
MEXT = md
## All markdown files in the working directory
SRC = $(wildcard *.$(MEXT))


DOCX=$(SRC:.md=.docx)
PDFS=$(SRC:.md=.pdf)


all: $(PDFS)	$(DOCX)
pdf: clean $(PDFS)
docx: clean $(DOCX)

# Separator for these lines need to start with a hard tab, not 4 spaces!
%.pdf: %.md
	if grep -q no_TOC $<; then \
		pandoc --toc --wrap=preserve -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../pdf/$@ $< \
	else \
		pandoc --wrap=preserve -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../pdf/$@ $< \
	fi; \

%.docx: %.md
	pandoc --toc --wrap=preserve -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o ../docx/$@ $<

clean:
	rm -f *.pdf *.docx
