import sys, getopt, os
import click
from doc_gen.file_reader import compile_files_in_dir_into_string, read_file,write_to_file
from doc_gen.generator import generate_code_documentation,generate_dir_documentation

@click.command()
@click.argument('dir', nargs=1, type=click.Path(exists=True))
@click.option('-d', '--depth', default=1, help='The depth of the directory to search for files')
def main(dir, depth):
	try:
		if os.path.isfile(dir):
			directory = os.path.dirname(dir)
			fileName = os.path.basename(dir)
			write_to_file(directory + "/" + f"README.{fileName}.md",generate_code_documentation(read_file(dir)))
		elif os.path.isdir(dir):
			write_to_file(dir + "/" + "README.md",generate_dir_documentation(compile_files_in_dir_into_string(dir, depth)))

	except FileNotFoundError:
		print("Input not found, are you sure it's a valid file or directory?")

if __name__ == "__main__":
   main()
