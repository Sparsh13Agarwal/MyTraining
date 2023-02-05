import test

def monkey_patch_fun(self):
    print("monkey patching func is called")


test.Test.func = monkey_patch_fun # changing behaviour of func()

ob = test.Test()
ob.func()
