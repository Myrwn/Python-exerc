#What will the following code print?

print('abc-def'.isalpha()) # False, because '-' is not an alphabetical character.
print('abc_def'.isalpha()) # False, because '_' is not an alphabetical character.
print('abc def'.isalpha()) # False, because '' (blank space) is not an alphabetical character.
print('abc def'.isalpha() and #False, because the 'and' operator checks if both statements are true
      'abc def'.isspace())    # First method outputs False, second one False as well. False as well, because the string contains non-whitespace characters (the letters.
print('abc def'.isalpha() or # False, because the 'or' operator checks if either one method is true.
      'abc def'.isspace())   # both methods return false (for the second one, is space returns true only when '   ' or '/h').
print('abcdef'.isalpha()) # True, because the string contains only aplhabtical characters.
print('31415'.isdigit()) # True, because the string contains only digits.
print('-31415'.isdigit()) # False, because '-' is not a digit.
print('31_415'.isdigit()) # False, because '_' is not a digit.
print('3.1415'.isdigit()) # False, because '.' is not a digit.
print(''.isspace())       # False, returns True only if there’s at least one character and all of them are spaces or whitespace.