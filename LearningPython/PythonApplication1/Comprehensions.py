import os
print(os.path.expanduser('~'))

print(os.getcwd())
metadata = os.stat('Comprehensions.py')
print(metadata.st_mtime)

import time
print(time.localtime(metadata.st_mtime))

print(metadata.st_size)

import NativeDatatypes
print(NativeDatatypes.approximate_size(metadata.st_size))


a_list = [1, 9, 8 ,4]
a_list = [elem * 2 for elem in a_list]
# Python constructs the new list in memory, and when the list comprehension is complete,
# it assigns the result to the original variable
print(a_list)

import glob
pyFiles = glob.glob('*.py');
print(pyFiles)

print([os.path.realpath(f) for f in pyFiles])

files = [f for f in glob.glob('*.py') if os.stat(f).st_size > 1000]
print(files)

#list comprehensions
print('\n\nlist comprehension')
print([(NativeDatatypes.approximate_size(os.stat(f).st_size), os.path.basename(f)) for f in glob.glob('*.py')])

#dictionary comprehensions
print('\n\ndictionary comprehension')
metadata_dict = {f:os.stat(f) for f in glob.glob('*.py')}
print(metadata_dict)
print(metadata_dict['Comprehensions.py'].st_size)

#set comprehensions
a_set = set(range(10))
print(a_set)
print({x * 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
print({2**x for x in range(10)})