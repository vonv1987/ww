calculator = {}
calculator["add"] = lambda x, y: x + y
calculator["sub"] = lambda x, y: x - y
calculator["mul"] = lambda x, y: x * y
calculator["div"] = lambda x, y: 1.0 * x / y

print calculator["add"](4, 6)
print calculator["sub"](4, 6)
print calculator["mul"](4, 6)
print calculator["div"](4, 6)

a=lambda x,y:x+y
print a(2,5)