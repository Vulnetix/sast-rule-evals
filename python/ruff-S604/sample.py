import my_custom_subprocess

user_input = input("Enter a command: ")
my_custom_subprocess.run(user_input, shell=True)

