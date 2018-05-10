from sys import argv
# what is os.path? what is exists?
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file).read()

print(f"The input file is {len(in_file)} bytes long")

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
