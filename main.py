import funcs

while True: 
    string = input("Enter pseudo-code : ")
    if string == 'quit':
        exit()
    else:
        fun_args = string.split(',', 1)
        func = getattr(funcs, fun_args[0])
        print(func(fun_args[1]))