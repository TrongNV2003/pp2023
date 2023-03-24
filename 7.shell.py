import os

while True:
# read command from user
    command = input('$ ')
    
# check for I/O redirection
    if '>' in command:
        # output to file
        command, filename = command.split('>')
        filename = filename.strip()
        os.system(f'{command.strip()} > {filename}')
    
    elif '<' in command:
        # input from file
        command, filename = command.split('<')
        filename = filename.strip()
        os.system(f'{command.strip()} < {filename}')
    
    elif '|' in command:
        # pipe command
        command1, command2 = command.split('|')
        os.system(f'{command1.strip()} | {command2.strip()}')
    
    else:
        # simple command
        os.system(command)
