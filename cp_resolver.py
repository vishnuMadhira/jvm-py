# v0.3 resolve meaning.
'''
We stop printing raw indexes and start printing human-readable JVM symbols.

'''

def resolve_utf8(cp,index):
    tag,value = cp[index]
    return value

def resolve_class(cp,index):
    tag,name_index = cp[index]
    return resolve_utf8(cp,name_index)

def resolve_string(cp,index):
    tag,string_index=cp[index]
    return resolve_utf8(cp,string_index)

def resolve_name_and_type(cp,index):
    tag,name_index,desc_index=cp[index]
    name=resolve_utf8(cp,name_index)
    desc=resolve_utf8(cp,desc_index)
    return name,desc

def resolve_methodref(cp,index):
    tag,class_index,name_type_index = cp[index]
    class_name=resolve_class(cp,class_index)
    name,desc=resolve_name_and_type(cp,name_type_index)
    return f"{class_name}.{name}{desc}"

def resolve_fieldref(cp,index):
    tag,class_index,name_type_index=cp[index]
    class_name=resolve_class(cp,class_index)
    name,desc=resolve_name_and_type(cp,name_type_index)
    return f"{class_name}.{name}:{desc}"
    