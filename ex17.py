from sys import argv; from os.path import exists; script, from_file, to_file = argv; in_file = open(from_file).read(); out_file = open(to_file, 'w').write(in_file); print(f"Copying from {from_file} to {to_file}\nThe input file is {len(in_file)} bytes long\nAlright, all done.")

# what is os.path? what is exists?
