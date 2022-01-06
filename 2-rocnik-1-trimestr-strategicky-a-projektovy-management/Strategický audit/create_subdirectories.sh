#!/bin/bash

create_subdirectories () {
    for OUTPUT in $(find . -type d)
    do
        if [[ $OUTPUT == *".texpadtmp"* ]] || [[ $OUTPUT == *"out"* ]] || [[ $OUTPUT == "." ]]; then
            :
        else
            mkdir -p out/"${OUTPUT#"./"}"
        fi
    done
}

copy_folder_structure () {
for OUTPUT in $(find . -type f -name "*.tex" -o -name "*.bib" -o -name "*.png")
    do
        if [[ $OUTPUT == "./out/"* ]]; then
            :
        else
            cp -R "${OUTPUT}" out/"${OUTPUT#"./"}"
        fi
    done
}

create_subdirectories
copy_folder_structure