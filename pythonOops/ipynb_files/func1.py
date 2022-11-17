# syntax:
# def <function_name>(<arg1>,<arg2>,...<argn>):
#    <statement1>
#    <statement2>
#    .
#    .
#    return <any out put that user wants to return>
#            # This is optional, if not used then
#            # By default "None" will be returned
#            # This acts as a exit gate, 
#            # after return, none of the statement 
#            # will be executed
#            
# def Add(a,b):
#    c = a+b
#    print(c)

def Add(a, b):
    c = a + b
    return (c)


c = Add(2, 5)
# Add(2,)
# Add(2, 5, 5)
# Add(10,20)
Add(10, 20)
print(Add(10, 20))
d = Add(10, 20)
# print(d)
