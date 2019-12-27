# script.py

# Runs the script to create new python projects
# Automates the task 


import os,sys

def execute_command(command):
    os.system(command)

def make_directory(path):
    os.mkdir(path)
    os.chdir(path)

def git_init(git_link):
    execute_command("git init")
    execute_command("git remote add origin {:}".format(git_link))

def git_first_commit():
    execute_command("echo.>README.MD")
    execute_command("git add *")
    execute_command('git commit -m "initial commit" ')
    execute_command("git push origin master")

# def instantiate_pip():
#     execute_command("pipenv shell")
#     execute_command("exit")


if __name__ == "__main__":
    directory = input("Enter your specified path: ")
    git_link = input("Enter your git link: ")
    make_directory(directory)
    # instantiate_pip()
    git_init(git_link)
    git_first_commit()

