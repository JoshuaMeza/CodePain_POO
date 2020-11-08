# PEP 8 - Coding standard 

## Naming

- **Variables:** CapWords preferring short names. The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.
- **Classes:** CapWords convention.
- **Functions:** lowercase, with words separated by underscores as necessary to improve readability.
- **Fuctions and Methods Arguments:**  Use ""self"" for the first argument to instance methods. Use ""cls"" for the first argument to class methods.
- **Constants:** Constants are usually defined on a module level and written in all capital letters with underscores separating words.
- **Libraries:** lower_case_with_underscores without any number.
- **Archives:** lower_case_with_underscores without any number.

## Documentation template

- **Language:** English.
- **Initial block:** ...
- **Classes:** ...
- **Functions:** ...
- **Procedure comments:** ...
- **Test comments:** ...

### Identation
- **Use 4 spaces per indentation level.**

Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent [7]. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line:

### Maximum Line Length
- **Limit all lines to a maximum of 79 characters.**

### Blank Lines
- Surround top-level function and class definitions with two blank lines.

- Method definitions inside a class are surrounded by a single blank line.

- Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

- Use blank lines in functions, sparingly, to indicate logical sections.

### Imports
- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
- Absolute imports are recommended, as they are usually more readable and tend to be better behaved 

### Module Level Dunder Names
- Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports. Python mandates that future-imports must appear in the module before any other code except docstrings

### Pet Peeves
**Avoid extraneous whitespace in the following situations:**
- Immediately inside parentheses, brackets or braces
- Between a trailing comma and a following close parenthesis.
- Immediately before a comma, semicolon, or colon.
- Immediately before the open parenthesis that starts the argument list of a function call.
- Immediately before the open parenthesis that starts an indexing or slicing.
- More than one space around an assignment (or other) operator to align it with another.
- However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted

## Documentation tools

...
