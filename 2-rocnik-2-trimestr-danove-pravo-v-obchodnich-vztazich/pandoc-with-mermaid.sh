#!/bin/bash

WHAT_FUNCTION_TO_RUN=$1
FILE_TO_COMPILE=$2
TARGET=$3
CURRENT_WORKING_DIRECTORY=$(pwd)

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

echo $CURRENT_WORKING_DIRECTORY

case ${WHAT_FUNCTION_TO_RUN} in

  run_pdf_without_toc)
    echo "Running function ${WHAT_FUNCTION_TO_RUN} with arguments: ${FILE_TO_COMPILE}, ${TARGET}."
    result=$((pdf_without_toc) 2>&1)
    echo $result
    ;;

  run_pdf_with_toc)
    echo "Running function ${WHAT_FUNCTION_TO_RUN} with arguments: ${FILE_TO_COMPILE}, ${TARGET}."
    result=$((pdf_with_toc) 2>&1)
    echo $result
    ;;

  run_docx_without_toc)
    echo "Running function ${WHAT_FUNCTION_TO_RUN} with arguments: ${FILE_TO_COMPILE}, ${TARGET}."
    result=$((docx_without_toc) 2>&1)
    echo $result
    ;;

  run_docx_with_toc)
    echo "Running function ${WHAT_FUNCTION_TO_RUN} with arguments: ${FILE_TO_COMPILE}, ${TARGET}."
    result=$((docx_with_toc) 2>&1)
    echo $result
    ;;

  *)
    echo "No valid function selected, exiting..." && exit 1
    ;;
esac