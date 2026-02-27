# Hash Table is a data structure designed to be fast to work with.
#
# The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for,
# adding, and deleting data can be done really quickly, even for large amounts of data.

# list with empty buckets and handling collisions for hashtable
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

# hash function
def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

# insert element in hashtable using hash function
def add(name):
  index = hash_function(name)
  my_list[index].append(name)

# implementation
print("'Bob' has hash code:", hash_function('Bob'))

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)
