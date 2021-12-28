"""File to parse and prepare bib file for the LaTeX compilation."""

# ---
# A Python script to parse bibfile and add online to all misc entries
# Currently only misc is implemented, other types and types to ignore will have to be implemented
# ---

from dataclasses import dataclass, fields
from typing import Union

@dataclass
class misc:
    name: str
    title: str
    url: str
    urldate: str
    file: Union[str, None]
    howpublished: str

def main():

    dict_of_miscs = {}
    name = None
    title = None
    url = None
    urldate = None
    file = None

    with open("Zdroje/Zdroje.bib", "r") as f:
        lines = f.readlines()

    for line in lines:
        if "file =" in line:
            file = str(line.split(" = ")[1])
        if name is not None and title is not None and url is not None and urldate is not None:
            dict_of_miscs[name] = misc(name, title, url, urldate, file, "{online}")
            name = title = url = urldate = None
        if line.startswith("@misc"):
            name = line.split("{")[1].replace(",","").replace("\n", "")
        if "title =" in line:
            title = str(line.split(" = ")[1])
        if "url =" in line:
            url = str(line.split(" = ")[1])
        if "urldate =" in line:
            urldate = str(line.split(" = ")[1])

    with open("Zdroje/Zdroje2.bib", "w") as f:
        for _, misc_value in dict_of_miscs.items():
            for field in fields(misc_value):
                if field.name == "name":
                    f.write("@misc{{{name},\n".format(name=getattr(misc_value, field.name)))
                if field.name == "title":
                    f.write("\t{field_name} = {title}".format(field_name=field.name, title=getattr(misc_value, field.name)))
                if field.name == "url":
                    f.write("\t{field_name} = {url}".format(field_name=field.name, url=getattr(misc_value, field.name)))
                if field.name == "urldate":
                    f.write("\t{field_name} = {urldate}".format(field_name=field.name, urldate=getattr(misc_value, field.name)))
                if field.name == "file":
                    if getattr(misc_value, field.name) is None or getattr(misc_value, field.name) == "None":
                        continue
                    f.write("\t{field_name} = {file}".format(field_name=field.name, file=getattr(misc_value, field.name)))
                if field.name == "howpublished":
                    f.write("\t{field_name} = {howpublished}\n}}\n\n".format(field_name=field.name, howpublished=getattr(misc_value, field.name)))


if __name__ == "__main__":
    main()
