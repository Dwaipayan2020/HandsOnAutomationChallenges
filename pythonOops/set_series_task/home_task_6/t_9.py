class AcceptArguments:
    a = 0

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        AcceptArguments.a += 1


accept_args = AcceptArguments('argument1', 'argument2')
accept_args = AcceptArguments('argument3', 'argument4')
accept_args = AcceptArguments('argument5', 'argument6')
accept_args = AcceptArguments('argument7', 'argument8')
accept_args = AcceptArguments('argument9', 'argument10')
