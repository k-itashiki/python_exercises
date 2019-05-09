import re
with open("README.md", "r", encoding="utf-8") as f:
    mach_word = []
    for line in f:
        if re.search("^##",line):
            mach_word.append(line.rstrip("\n"))
    print(mach_word)  ## output line
f.close
