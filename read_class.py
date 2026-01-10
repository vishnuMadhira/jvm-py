from byte_reader import ByteReader
from constant_pool import read_constant_pool
# from cp_resolver import resolve_methodref,resolve_class,resolve_name_and_type,resolve_string,resolve_utf8,resolve_fieldref
from cp_resolver import *


with open("Hello.class", "rb") as f:
    data = f.read()

# v0 -> magic
magic = data[:4]
print(magic)


# v0.1 -> major,minor
reader = ByteReader(data)
magic = reader.read_u4()
minor = reader.read_u2()
major = reader.read_u2()

print(f"magic=0x{magic:08x}")
print(f"minor={minor}")
print(f"major={major}")



# v0.2 -> constant pool
cp_count = reader.read_u2()
print("constant_pool_count =", cp_count)

cp = read_constant_pool(reader, cp_count)

for i in range(1, cp_count):
    print(i, cp[i])
    
# v0.3 -> resolve meaning

print("\Resolved Constant Pool:")

for i in range(1,cp_count):
    entry = cp[i]
    
    if entry[0] == "Methodref":
        print(i,resolve_methodref(cp,i))
    
    elif entry[0] == "Class":
        print(i,resolve_class(cp,i))
    
    elif entry[0] == "NameAndType":
        name, desc = resolve_name_and_type(cp, i)
        print(i, "NameAndType =", name, desc)
    
    elif entry[0] == "Utf-8":
        print(i,resolve_utf8(cp,i))
    
    elif entry[0] == "String":
        print(i,resolve_string(cp,i))
    
    elif entry[0]=="Fieldref":
        print(i,resolve_fieldref(cp,i))
        
"""
from cp_resolver import *

print("\nResolved Methodrefs:")

for i in range(1, cp_count):
    entry = cp[i]
    if entry[0] == "Methodref":
        print(i, resolve_methodref(cp, i))

"""
    

