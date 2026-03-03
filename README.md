# variables_plus

A simple Python library to create, clear, read, write and delete variables in multiple sandboxes.

This is my first python library :D

Commands:

vp.vp("create(variable=something)")   # Remove =something to create a blank variable.

vp.vp("clear(variable)")   # Leave clear() empty to clear all variables.

vp.vp("delete(variable)")   # Variable needs to exist.

vp.vp("read(variable)")   # Doesn't print it. Use print(vp.vp("read(variable)")) to print the variables contents.

vp.vp(“write(variable=something)”)   # Variable needs to exist.

vp.vp("SANDBOX()") # Add a number between the brackets for the sandbox ID.

# !NB!

Use: pip install variablesplus

But, to import it: import vp
