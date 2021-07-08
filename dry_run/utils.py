import inspect

def get_arg(func, args, arg):
    arg_names = inspect.getfullargspec(func).args
    return args[arg_names.index(arg)]
