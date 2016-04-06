usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
            'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
            'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_to_check = str(input("Enter your username"))
if username_to_check in usernames:
    print("Access granted")
else:
    print("Access denied")
