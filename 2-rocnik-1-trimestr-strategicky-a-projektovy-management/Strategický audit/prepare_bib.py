"""File to parse and prepare bib file for the LaTeX compilation."""

# ---
# A Python script to parse bibfile and add online to all misc entries
# Currently only misc and online types are implemented
# ---

from typing import Iterable, Any, Tuple
import copy
import sys

prefixes: list = ["@misc", "@online"]

def check_if_field_already_exists(it:Iterable[Any], field: str) -> bool:
    return any(field in string for string in it)

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

    for line in lines:
        if line == "\n":
            continue
        temp_list.append(line)
        if line == "}\n" or line == "}":
            list_of_entries.append(copy.deepcopy(temp_list))
            temp_list.clear()

    with open(bib_file_location, "w") as f:
        for entry in list_of_entries:
            #print(entry)
            if not (is_online := check_if_online_entry(entry)):
                for is_last_element, var in is_element_last_in_iterable(entry):
                    if is_last_element:
                        f.write("{}\n".format(var))
                    else:
                        f.write(var)
            if is_online:
                if check_if_field_already_exists(entry, "howpublished"):
                    for is_last_element, var in is_element_last_in_iterable(entry):
                        if is_last_element:
                            f.write("{}\n".format(var))
                        else:
                            f.write(var)
                else:
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
