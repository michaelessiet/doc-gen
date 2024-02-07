from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def generate_code_documentation(code, model="gpt-4-turbo-preview"):
		print("Generating documentation for code, please wait...")
		response = client.chat.completions.create(
			model=model,
			messages=[
				{
					"role": "system",
					"content": "You are a software engineer and you are writing documentation for the following code"
				},
				{
					"role": "user",
					"content": code
				},
				{
					"role": "system",
					"content": "Write the documentation for the code. And remember to include the purpose of the code, how it works, and how to use it."
				}
			],
		)
		return response.choices[0].message.content

def generate_dir_documentation(code, model="gpt-4-turbo-preview"):
	print("Generating documentation for directory, this may take a while so go touch grass or something...")
	response = client.chat.completions.create(
		model=model,
		messages=[
			{
				"role": "system",
				"content": "You're a software engineer, here is all the code within all the files in the directory. Write the documentation for the directory."
			},
			{
				"role": "user",
				"content": code
			},
			{
				"role": "system",
				"content": "Write the documentation for the directory"
			},
		]
	)
	return response.choices[0].message.content
