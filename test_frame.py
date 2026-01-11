from frame import Frame

frame = Frame(4,4)

frame.locals[1] = 2
frame.locals[2] = 3

frame.push(frame.locals[1])
frame.push(frame.locals[2])

a = frame.pop()
b = frame.pop()

frame.push(a+b)

print(frame.stack)