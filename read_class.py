from byte_reader import ByteReader


with open("Hello.class", "rb") as f:
    data = f.read()

# v0
# magic = data[:4]
# print(magic)


# v0.1
reader = ByteReader(data)
magic = reader.read_u4()
minor = reader.read_u2()
major = reader.read_u2()

print(f"magic=0x{magic:08x}")
print(f"minor={minor}")
print(f"major={major}")


