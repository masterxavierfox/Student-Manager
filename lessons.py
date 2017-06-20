add_students(name = "Mark", student_id = 15)


#Variable arguments
def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"], kwargs["salutation"], kwargs["subscriber"])


#Variable arguments
print("Variable Arguments:")
var_args("Mark", "Loves Python", None, "Hello", True)


#key word variable arguments
print("key Word Variable Arguments:")
var_kwargs("Mark", description="Loves Python", feedback=None, salutation="Hello", subscriber=True)

