#requires yasm to be at /usr/local/bin
from subprocess import call

asmFile = "/tmp/tmp.s"
binFile = "/tmp/tmp.o"
doc = Document.getCurrentDocument()
seg = doc.getCurrentSegment()
addr = doc.getCurrentAddress()

asm = Document.ask("Enter instruction:")

if asm != None:
    f = open(asmFile, "w")
    f.write("[BITS 64]\n")
    f.write(asm)
    f.close()
    res = call(["/usr/local/bin/yasm", "-o", binFile, asmFile])
    if res == 0:
        bytes = bytearray(open(binFile, "rb").read())
        for i in range(len(bytes)):
            byte = bytes[i]
            seg.writeByte(addr, byte)
            addr = addr + 1

seg.markAsCode(doc.getCurrentAddress())
