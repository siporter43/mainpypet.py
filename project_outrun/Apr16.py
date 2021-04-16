
# Goals:
# [ ] Iterate all of the files in your working directory that end in `.py`
# [ ] Get the first line of each file.
# [ ] Extract the docstring, if it exists, from the file:
#     [ ] Iterate through each line of the file
#     [ ] Strip the leading and trailing whitespace from each line by calling `.strip()`
#     [ ] Skip any lines that are empty or begin with `#`
#     [ ] Extract the docstring
#         [ ] If you come across any nonempty line that doesn't start with either `"""` or `#`, there is no docstring for that file, so you can stop.
#         [ ] If the line begins with `"""`,
#             [ ] if the line doesn't end in `"""`
#                 [ ] continue iterating through the remaining lines in the file
#                     [ ] append each line to the docstring text
#                     [ ] until you find one that ends in `"""`
#             [ ] otherwise, that's the end of the docstring
#             [ ] remove the leading and trailing `"""`
# [ ] int the filename followed by the docstring (if any) of each file
