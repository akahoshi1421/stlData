path = input("path?")

f = open(path[1:len(path) - 1], "r")

result = ""

for line in f.readlines():
    if "solid" in line or "endsolid" in line:
        continue

    if "vertex" in line:
        numData = line.split("vertex  ")[1]

        xyz = numData.split("  ")

        x = xyz[0]
        y = xyz[1]
        z = xyz[2]

        thisLine = "            vertex  "

        if x[0] == "0":
            if "+00" in x:
                thisLine += "${this.x}" + x[1:len(x) - 2] + "01"
            else:
                thisLine += "${this.x}" + x[1:]

        elif x[0] == "1":
            thisLine += "${this.x+1}" + x[1:]

        if y[0] == "0":
            thisLine += "  ${this.y}" + y[1:]

        elif y[0] == "1":
            thisLine += "  ${this.y+1}" + y[1:]

        if z[0] == "0":
            thisLine += "  ${this.z}" + z[1:]

        elif z[0] == "1":
            thisLine += "  ${this.z+1}" + z[1:]

        thisLine += "\n"

        result += thisLine

    else:
        result += line

f.close()

f = open("result.txt", "w")

f.write(result)

f.close()