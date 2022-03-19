#!/bin/bash

pandoc --wrap=preserve -F mermaid-filter -f markdown-implicit_figures+hard_line_breaks+escaped_line_breaks -o pdf/mermaid-test.pdf 2-rocnik-2-trimestr-danove-pravo-v-obchodnich-vztazich/Danove\ pravo\ v\ obchodnich\ vztahu\ zapisky.md