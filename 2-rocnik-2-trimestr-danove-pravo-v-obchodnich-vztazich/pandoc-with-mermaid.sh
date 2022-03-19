#!/bin/bash

WHAT_FUNCTION_TO_RUN=$1
FILE_TO_COMPILE=$2
TARGET=$3

pdf_without_toc () {
    pandoc --wrap=preserve \
    -F mermaid-filter \
    -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks \
    -o ${TARGET} \
    ${FILE_TO_COMPILE}
}

pdf_with_toc () {
    pandoc --toc --wrap=preserve \
    -F mermaid-filter \
    -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks \
    -o ${TARGET} \
    ${FILE_TO_COMPILE}
}

docx_without_toc () {
    pandoc --wrap=preserve \
    -F mermaid-filter \
    -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks \
    -o ${TARGET} \
    ${FILE_TO_COMPILE}
}

docx_with_toc () {
    pandoc --toc --wrap=preserve \
    -F mermaid-filter \
    -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks \
    -o ${TARGET} \
    ${FILE_TO_COMPILE}
}

case ${WHAT_FUNCTION_TO_RUN} in

  run_pdf_without_toc)
    pdf_without_toc
    ;;

  run_pdf_with_toc)
    pdf_with_toc
    ;;

  run_docx_without_toc)
    docx_without_toc
    ;;

  run_docx_with_toc)
    docx_with_toc
    ;;

  *)
    echo "No valid function selected, exiting..." && exit 1
    ;;
esac