import sys, getopt, os
from doc_gen.file_reader import compile_files_in_dir_into_string, read_file,write_to_file
from doc_gen.generator import generate_code_documentation,generate_dir_documentation

def main(argv):
	opts, args = getopt.getopt(argv, "h")

	if "-h" in opts or len(args) == 0:
		print(f"""Usage: doc-gen [directory]""")
		sys.exit()

	if len(args) == 0:
		print("No directory provided")
		sys.exit(2)

	if len(args) > 1:
		print("Too many arguments")
		sys.exit(2)

	dir = args[0]

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
