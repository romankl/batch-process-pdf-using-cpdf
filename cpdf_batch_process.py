from pathlib import Path
import os

count = 0

for path in Path('/PATH-TO-FOLDER-WITH-PDFs/pdf').rglob('*.pdf'):
    pfile = path.absolute()
    print("PROCESSING... " + str(pfile))
    os.system("/PATH-TO-CPDF-TOOL/cpdf " + str(pfile) + " -o " + str(pfile))
    print("DONE " + str(pfile) + "\n\n")
    count = count + 1

print(str(count) + " files processed" + "\n\n")
