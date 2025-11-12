# Write Python code to replace all the : 
# characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

new_info ='+'.join(info.split(':')) 
 # Python first evaluates info.split(':')
 # This call returns a new list of strings: 
 # ['xyz', '*', '42', '42', 'Lee Kim', '/home/xyz', '/bin/zsh']
 # Then, the .join() method is called on the '+' string, and the 
 # list that was just created is passed as an argument to join. 
print(new_info)