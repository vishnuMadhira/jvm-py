from byte_reader import ByteReader
from constant_pool import read_constant_pool


with open("Hello.class", "rb") as f:
    data = f.read()

# v0 -> magic
# magic = data[:4]
# print(magic)


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


