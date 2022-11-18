# Variable Shadowing
# NameSpace에 의해 변수가 가려지게 되는 것

var_shadowing = "global"


def outer_function():
    var_shadowing = "outer"

    def inner_function():
        var_shadowing = "inner1"
        print("inner function scope:%s" % var_shadowing)

    inner_function()
    print("outer_function scope:%s" % var_shadowing)


if __name__ == '__main__':
    outer_function()
    print("global scope %s" % var_shadowing)
