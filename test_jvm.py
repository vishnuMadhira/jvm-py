from jvm import JVM
from frame import Frame

jvm = JVM()

f1 = Frame(2,2)
f2 = Frame(2,2)

jvm.push_frame(f1)
jvm.push_frame(f2)

print(jvm.current_frame() == f2)