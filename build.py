from pathlib import Path
Path("output").mkdir(exist_ok=True)

font = fontforge.open('TF2C.sfdir')
font.generate('output/tf2c.ttf')
font.generate('output/tf2c.woff2')
font = fontforge.open('TF2CSecondary.sfdir')
font.generate('output/tf2c-secondary.ttf')
font.generate('output/tf2c-secondary.woff2')
font = fontforge.open('TF2CBuild.sfdir')
font.generate('output/tf2c-build.ttf')
font.generate('output/tf2c-build.woff2')
font = fontforge.open('TF2CProfessor.sfdir')
font.generate('output/tf2c-professor.ttf')
font.generate('output/tf2c-professor.woff2');