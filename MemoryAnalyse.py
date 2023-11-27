from Constants import REDUSE_MEMINFO_PRINT, DETAIL_MEMINFO_PRINT

MEMORY_JAVA_HEAP = "Java Heap:"
MEMORY_NATIVE_HEAP = "Native Heap:"
MEMORY_CODE = "Code:"
MEMORY_STACK = "Stack:"
MEMORY_GRAPHICS = "Graphics:"
MEMORY_PRIVATE_OTHER = "Private Other:"
MEMORY_SYSTEM = "System:"
MEMORY_TOTAL_PSS = "TOTAL PSS:"


class MemoryAnalyse:
    fileName = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def readMemoryFile(self):
        with open(self.fileName, "r", encoding="latin-1") as fd:
            return fd.read()

    def memoryAnalyse(self, optionName, recordTime, printType):
        dumpInfo = self.readMemoryFile()
        if printType == DETAIL_MEMINFO_PRINT:
            print(dumpInfo)
        lines = dumpInfo.split("\n")
        meminfoList = [None] * 10
        meminfoList[0] = recordTime
        meminfoList[1] = optionName
        index = 0
        replace = ""
        for line in lines:
            index = 1
            if MEMORY_JAVA_HEAP in line:
                index = 2
                replace = MEMORY_JAVA_HEAP
            elif MEMORY_NATIVE_HEAP in line:
                index = 3
                replace = MEMORY_NATIVE_HEAP
            elif MEMORY_CODE in line:
                index = 4
                replace = MEMORY_CODE
            elif MEMORY_STACK in line:
                index = 5
                replace = MEMORY_STACK
            elif MEMORY_GRAPHICS in line:
                index = 6
                replace = MEMORY_GRAPHICS
            elif MEMORY_PRIVATE_OTHER in line:
                index = 7
                replace = MEMORY_PRIVATE_OTHER
            elif MEMORY_SYSTEM in line:
                index = 8
                replace = MEMORY_SYSTEM
            elif MEMORY_TOTAL_PSS in line:
                index = 9
                if printType == REDUSE_MEMINFO_PRINT:
                    print(line)
                replace = MEMORY_TOTAL_PSS
            if index > 1:
                line = line.replace(replace, "")
                line_split = line.split()
                meminfoList[index] = line_split[0]
        return dumpInfo, meminfoList
