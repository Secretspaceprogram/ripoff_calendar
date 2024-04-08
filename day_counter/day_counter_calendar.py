import re
import subprocess


def update_svg(number):
    change = open("template.svg", "rt")
    data = change.read()
    data = data.replace('id="tspan217791">0', 'id="tspan217791">' + str(number))
    change.close()
    Change = open("temp.svg", "wt")
    Change.write(data)
    Change.close()
    subprocess.run(['/Applications/Inkscape.app/Contents/MacOS/inkscape', "temp.svg", '--export-type=pdf', '--export-filename=' + "output/" + str(number)])
    subprocess.run(['rm', "temp.png"])

for i in range(300,367):
    update_svg(i)


