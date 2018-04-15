import os, sys

print('This script searches and moves all files from a directory with a certain extension to one specific folder\n')

print('Search directory (e.g C:\\dir): ', end='')
search_dir = input()

print('Target folder (e.g C:\\target): ', end='')
target_dir = input()

print('File extension (e.g .mp3): ', end='')
file_ext = input()

if not(os.path.isdir(search_dir)):
	sys.exit("The directory " + search_dir + " was not found")
elif not(os.path.isdir(target_dir)):
	sys.exit("The folder " + target_dir + " was not found")

n_files=0
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(file_ext):
        	n_files+=1
	       	os.rename(os.path.join(root, file),str(target_dir+'\\'+file))

print(str(n_files) + " files were moved!")