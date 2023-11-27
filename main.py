import os
import sys

from Constants import REDUSE_MEMINFO_PRINT
from ExcelUtils import writeExcel
from MemoryAnalyse import MemoryAnalyse

if __name__ == '__main__':
    analyseDir = sys.argv[1]
    outFile = analyseDir + "/out.xlsx"
    result = []
    excelTitle = ['Time', '文件名', 'Java heap', 'Native heap', 'Code', 'Stack', 'Graphics', 'Private Other',
                  'System',
                  'PSS TOTAL']
    result.append(excelTitle)
    for fileName in os.listdir(analyseDir):
        filePath = os.path.join(analyseDir, fileName)
        memoryAnalyse = MemoryAnalyse(filePath)
        creationTime = os.path.getctime(filePath)
        dumpInfo, meminfoList = memoryAnalyse.memoryAnalyse(fileName, creationTime, REDUSE_MEMINFO_PRINT)
        result.append(meminfoList)
    writeExcel(outFile, result)
