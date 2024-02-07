import sys, getopt, os
from doc_gen.file_reader import compile_files_in_dir_into_string, read_file,write_to_file
from doc_gen.generator import generate_code_documentation,generate_dir_documentation

def main(argv):
	opts, args = getopt.getopt(argv, "hd:", ["dir="])
	dir = ""

	if len(opts) == 0:
		print("No options provided")
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-d", "--dir"):
			dir = arg
		elif opt == "-h":
			print(f"""Usage: doc-gen [option] [argument]
Options:
  -d --dir <file or directory> : Document a directory or file
				""")
			sys.exit()

	try:
		if os.path.isfile(dir):
			directory = os.path.dirname(dir)
			fileName = os.path.basename(dir)
			write_to_file(directory + "/" + f"README.{fileName}.md",generate_code_documentation(read_file(dir)))
		elif os.path.isdir(dir):
			write_to_file(dir + "/" + "README.md",generate_dir_documentation(compile_files_in_dir_into_string(dir)))

	except FileNotFoundError:
		print("Input not found, are you sure it's a valid file or directory?")

if __name__ == "__main__":
   main(sys.argv[1:])
