# v0.1 -> read bytes from java class file and print minor,major and magic

class ByteReader:
    def __init__(self,data: bytes):
        self.data = data
        self.pos = 0
    
    # Bitwise OR (|) : This works on individual bits.
    # read input at pos form data in bytes and used by others for processing
    # read one unsigned byte at the current position and advance the cursor
    def read_u1(self) -> int:
        value = self.data[self.pos]
        self.pos = self.pos+1
        return value
    

    # extra topic to learn:

    # Two worldviews exist :
    # 1. Big-endian (most significant byte first) : value = (first_byte << 8) | second_byte
        # Used by:
        # Network protocols (TCP/IP)
        # File format
        # JVM class files

    # Humans, conceptually
    # 2. Little-endian (least significant byte first) : value = (second_byte << 8) | first_byte
        # Used by:
        # x86 CPUs internally
        # Some binary blobs
        # Certain file formats (rarely)
    
    # Bytes in file (hex):
    # CA FE

    # CA = 11001010
    # FE = 11111110

    # Each byte occupies 8 bits.
    # We want to assemble them into one integer represented by 16 bits
    # 11001010 11111110

    # b1 << 8
    # b2
    
    def read_u2(self) -> int:
        b1 = self.read_u1()
        b2 = self.read_u1()
        return (b1 << 8) | b2
    
    # Bytes in file (hex):
    # CA FE BA BE

    # CA = 11001010
    # FE = 11111110
    # BA = 10111010
    # BE = 10111110

    # Each byte occupies 8 bits.
    # We want to assemble them into one 32-bit number:
    # 11001010 11111110 10111010 10111110

    # b1 << 24
    # b2 << 16
    # b3 << 8
    # b4


    
    def read_u4(self) -> int:
        b1 = self.read_u1()
        b2 = self.read_u1()
        b3 = self.read_u1()
        b4 = self.read_u1()
        return (b1 << 24) | (b2 << 16) | (b3 << 8) | b4