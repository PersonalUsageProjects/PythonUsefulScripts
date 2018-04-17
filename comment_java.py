import os, sys

comment = "/* Aluno: Raul Formiga Mansur\n Matrícula: 635382\n Ciência da Computação Tarde\n*/"

print("This script comment all .java files inside an directory")

print('Search directory (e.g C:\\dir): ', end='')
search_dir = input()

n_files=0
for root, dirs, files in os.walk(search_dir):
	for file in files:
		if file.endswith(".java"):
			n_files+=1

			f = open(os.path.join(root, file), 'r+')
			file_data = f.read()
			f.seek(0, 0)
			f.write(comment.rstrip('\r\n') + '\n' + file_data)

print(str(n_files) + " files were commented!")
