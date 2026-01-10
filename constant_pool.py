'''
Why constant pool is indexed from 1
    This is not a programming accident.
    The JVM designers wanted:
    Index 0 = invalid
    So any zero index means “not present”
    That’s why:
    constant_pool_count = N
    valid entries = 1 … N-1
'''
# v0.2 -> constant pool

from byte_reader import ByteReader


TAG_UTF8 = 1
TAG_CLASS = 7
TAG_STRING = 8
TAG_FIELDREF = 9
TAG_METHODREF = 10
TAG_NAMEANDTYPE = 12


def read_constant_pool(reader: ByteReader,cp_count):
    cp = [None]*cp_count #index 0 unused -> index 0 is not found in JVM
    i=1
    while i < cp_count:
        tag = reader.read_u1();
        if tag == TAG_UTF8:
            length = reader.read_u2();
            bytes_data = reader.data[reader.pos:reader.pos+length]
            reader.pos += length
            value = bytes_data.decode("utf-8"); # bytes to String in UTF-8
            cp[i] = ("utf-8",value)
        
        elif tag == TAG_CLASS:
            name_index = reader.read_u2()
            cp[i] = ("Class",name_index)
        
        elif tag == TAG_STRING:
            string_index = reader.read_u2()
            cp[i] = ("String",string_index)
        
        elif tag == TAG_FIELDREF:
            class_index = reader.read_u2()
            name_type_index = reader.read_u2()
            cp[i] = ("Fieldref",class_index,name_type_index)
        
        elif tag == TAG_METHODREF:
            name_index = reader.read_u2()
            desc_index = reader.read_u2()
            cp[i] = ("Methodref",name_index,desc_index)
            
        elif tag == TAG_NAMEANDTYPE:
            name_index = reader.read_u2()
            desc_index = reader.read_u2()
            cp[i] = ("NameAndType",name_index,desc_index)
        
        else:
            raise Exception("Unsupported constant pool tag: "+ str(tag))
        
        i+=1
    return cp