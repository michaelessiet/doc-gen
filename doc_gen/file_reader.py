import os

excluded_dirs = [".git", ".idea", "__pycache__", "node_modules", ".vscode", "venv", "env", "build", "dist", "target", "out", "output", "bin", "obj", ".output", ".nuxt", ".vercel"]

def read_directory(directory:str):
	files = os.listdir(directory)
	# exlude dirs
	files = [file for file in files if file not in excluded_dirs]
	return files

def read_file(file:str):
	try:
		with open(file, 'r') as f:
			return f.read()
	except UnicodeDecodeError:
		print("File is unreadable: " + file)
		return ""

def read_files_in_directory(directory:str, depth:int, curr_depth = 0):
	files = read_directory(directory)
	fileMap = {}
	for file in files:
		if os.path.isfile(directory + "/" + file):
			fileMap[file] = read_file(directory + "/" + file)
		elif os.path.isdir(directory + "/" + file) and curr_depth < depth:
			fileMap[file] = read_files_in_directory(directory + "/" + file, depth, curr_depth + 1)
		else:
			print("Unknown file type: " + file)
	return fileMap

def compile_files_in_dir_into_string(directory:str, depth:int):
	files = read_files_in_directory(directory, depth)
	string = ""
	for (file, content) in files.items():
		if type(content) is dict:
			string += compile_files_in_dir_into_string(directory + "/" + file, depth)
		else:
			string += file + ":\n" + content + "\n------------------------------------------------------------\n"
	return string

def write_to_file(file:str, content:str | None):
	with open(file, 'w') as f:
		f.write(content if content else "")
	return
