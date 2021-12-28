#!/bin/bash

for OUTPUT in $(find . -type d)
do
    if [[ $OUTPUT == *".texpadtmp"* ]] || [[ $OUTPUT == *"out"* ]] || [[ $OUTPUT == "." ]]; then
        :
    else
        mkdir -p out/"${OUTPUT#"./"}"
    fi
done