import re
with open("README.md", "r", encoding="utf-8") as f:
    for line in f:
        if re.search("^##",line):
            print(line)  ## output line
f.close
