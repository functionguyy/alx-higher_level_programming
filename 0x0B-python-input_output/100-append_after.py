#!/usr/bin/python3
"""Module define function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a specific
    string

    args:
        filename(:str): name of file
        search_string(:str): string to search for in file lines
        new_string(:str): string to insert inside the file
    """

    # ensure all arguments are strings
    arg = [filename, search_string, new_string]
    string_status = list(map(lambda x: True if type(x) is str else False, arg))
    condition_status = all(string_status)

    if condition_status is True:
        # create an empty list
        file_content = []

        # open the file and read it line by line
        with open(filename, encoding='utf-8') as f:
            for line in f:
                file_content.append(line)
                # parse the line for a match to search_string
                if search_string in line:
                    # if there is match, append the line to file_content
                    # then append the new_string after it to file_content
                    file_content.append(new_string)

        # exiting the upper `with` block means file_content is populated
        # now open the file again for writing the elements in file_content
        with open(filename, 'w', encoding='utf-8') as f:
            for line in file_content:
                f.write(line)
