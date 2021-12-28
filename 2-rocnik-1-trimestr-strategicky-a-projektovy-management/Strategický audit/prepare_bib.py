"""File to parse and prepare bib file for the LaTeX compilation."""

# ---
# A Python script to parse bibfile and add online to all misc entries
# Currently only misc is implemented, other types and types to ignore will have to be implemented
# ---

from dataclasses import dataclass, fields
from typing import Union, Iterable, Any, Tuple
import copy

prefixes = ["@misc", "@online"]

def check_if_online_entry(it:Iterable[Any]) -> bool:
    return it[0].startswith(tuple(prefixes))

def signal_last(it:Iterable[Any]) -> Iterable[Tuple[bool, Any]]:
    iterable = iter(it)
    ret_var = next(iterable)
    for val in iterable:
        yield False, ret_var
        ret_var = val
    yield True, ret_var

@dataclass
class misc:
    name: str
    title: str
    url: str
    urldate: str
    file: Union[str, None]
    howpublished: str

def main():

    list_of_entries = []
    temp_list = []
    name = None
    title = None
    url = None
    urldate = None
    file = None

    # loop throu list until line contains only }
    # add to list except spaces of list pop from original lists
    # recursively start looping trhou the list again

    with open("Zdroje/Zdroje.bib", "r") as f:
        lines = f.readlines()

    for is_last_element, var in signal_last(lines):
        if is_last_element:
            print(var)
            if var == "\n":
                continue
            temp_list.append(var)
            if var == "}":
                list_of_entries.append(copy.deepcopy(temp_list))
                temp_list.clear()
        else:
            print(var)
            if var == "\n":
                continue
            temp_list.append(var)
            if var == "}\n":
                list_of_entries.append(copy.deepcopy(temp_list))
                temp_list.clear()

    #for line in lines:
    #    print(line)
    #    if line == "\n":
    #        continue
    #    temp_list.append(line)
    #    if line == "}\n":
    #        list_of_entries.append(copy.deepcopy(temp_list))
    #        temp_list.clear()

    print(list_of_entries)

    with open("Zdroje/Zdroje2.bib", "w") as f:
        for entry in list_of_entries:
            if not (is_online := check_if_online_entry(entry)):
                for is_last_element, var in signal_last(entry):
                    if is_last_element:
                        f.write("{}\n".format(var))
                    else:
                        f.write(var)
            if is_online:
                for is_last_element, var in signal_last(entry):
                    if is_last_element:
                        f.write("\thowpublished = {{online}},\n{}\n".format(var))
                    else:
                        f.write(var)
            # pass to function that will tell if prefixes
            # if not, just loop over entry and write line (pass to signal_last), if last append \n\n to write line function call
            # if yes, just loop over entry and write line (pass to signal_last), if last append howpublished = {online}\n\n to write line function call
            #for line in entry:
            #    if not line.startswith(tuple(prefixes)):
            #        f.write(line)
            #    f.write(line)
                

    #print(list_of_entries)

    #for line in lines:
    #    if line.startswith("@misc"):
        #    name = line.split("{")[1].replace(",","").replace("\n", "")
        #if "file =" in line:
        #    file = str(line.split(" = ")[1])
        #if name is not None and title is not None and url is not None and urldate is not None:
        #    dict_of_miscs[name] = misc(name, title, url, urldate, file, "{online}")
        #    name = title = url = urldate = None
        #if line.startswith("@misc"):
        #    name = line.split("{")[1].replace(",","").replace("\n", "")
        #if "title =" in line:
        #    title = str(line.split(" = ")[1])
        #if "url =" in line:
        #    url = str(line.split(" = ")[1])
        #if "urldate =" in line:
        #    urldate = str(line.split(" = ")[1])

    #with open("Zdroje/Zdroje2.bib", "w") as f:
    #    for _, misc_value in dict_of_miscs.items():
    #        for field in fields(misc_value):
    #            if field.name == "name":
    #                f.write("@misc{{{name},\n".format(name=getattr(misc_value, field.name)))
    #            if field.name == "title":
    #                f.write("\t{field_name} = {title}".format(field_name=field.name, title=getattr(misc_value, field.name)))
    #            if field.name == "url":
    #                f.write("\t{field_name} = {url}".format(field_name=field.name, url=getattr(misc_value, field.name)))
    #            if field.name == "urldate":
    #                f.write("\t{field_name} = {urldate}".format(field_name=field.name, urldate=getattr(misc_value, field.name)))
    #            if field.name == "file":
    #                if getattr(misc_value, field.name) is None or getattr(misc_value, field.name) == "None":
    #                    continue
    #                f.write("\t{field_name} = {file}".format(field_name=field.name, file=getattr(misc_value, field.name)))
    #            if field.name == "howpublished":
    #                f.write("\t{field_name} = {howpublished}\n}}\n\n".format(field_name=field.name, howpublished=getattr(misc_value, field.name)))


if __name__ == "__main__":
    main()
