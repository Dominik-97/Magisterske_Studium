"""File to parse and prepare bib file for the LaTeX compilation."""

# ---
# A Python script to parse bibfile and add online to all misc entries
# Currently only misc is implemented, other types and types to ignore will have to be implemented
# ---

from typing import Iterable, Any, Tuple
import copy
import sys

prefixes: list = ["@misc", "@online"]

def check_if_online_entry(it:Iterable[Any]) -> bool:
    return it[0].startswith(tuple(prefixes))

def is_element_last_in_iterable(it:Iterable[Any]) -> Iterable[Tuple[bool, Any]]:
    iterable = iter(it)
    ret_var = next(iterable)
    for val in iterable:
        yield False, ret_var
        ret_var = val
    yield True, ret_var

def main(bib_file_location: str) -> None:

    list_of_entries = []
    temp_list = []

    try:
        with open(bib_file_location, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Provided file was not found.")
        exit(1)

    for is_last_element, var in is_element_last_in_iterable(lines):
        if is_last_element:
            if var == "\n":
                continue
            temp_list.append(var)
            if var == "}":
                list_of_entries.append(copy.deepcopy(temp_list))
                temp_list.clear()
        else:
            if var == "\n":
                continue
            temp_list.append(var)
            if var == "}\n":
                list_of_entries.append(copy.deepcopy(temp_list))
                temp_list.clear()

    with open(bib_file_location, "w") as f:
        for entry in list_of_entries:
            if not (is_online := check_if_online_entry(entry)):
                for is_last_element, var in is_element_last_in_iterable(entry):
                    if is_last_element:
                        f.write("{}\n".format(var))
                    else:
                        f.write(var)
            if is_online:
                for is_last_element, var in is_element_last_in_iterable(entry):
                    if is_last_element:
                        f.write("\thowpublished = {{online}},\n{}\n".format(var))
                    else:
                        f.write(var)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide the bib file location.")
        exit(1)
