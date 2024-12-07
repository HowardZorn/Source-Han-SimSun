import fontTools.ttLib as ttLib
from fontTools.misc.xmlReader import XMLReader


bold = ttLib.TTFont('SourceHanSerifSC-Bold.ttf')
regular = ttLib.TTFont('SourceHanSerifSC-Regular.ttf')
light = ttLib.TTFont('SourceHanSerifSC-Light.ttf')
bold_hw = ttLib.TTFont('SourceHanSerifHWSC-Bold.ttf')
regular_hw = ttLib.TTFont('SourceHanSerifHWSC-Regular.ttf')
light_hw = ttLib.TTFont('SourceHanSerifHWSC-Light.ttf')

# Use typography metrics for line spacing.
# To enable USE_TYPO_METRICS flag in OS/2, set the 8-th bit as 1.
# Reference: https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection

bold["OS/2"].version = 4
regular["OS/2"].version = 4
light["OS/2"].version = 4
bold_hw["OS/2"].version = 4
regular_hw["OS/2"].version = 4
light_hw["OS/2"].version = 4

bold["OS/2"].fsSelection |= (1 << 7)
regular["OS/2"].fsSelection |= (1 << 7)
light["OS/2"].fsSelection |= (1 << 7)

bold_hw["OS/2"].fsSelection |= (1 << 7)
regular_hw["OS/2"].fsSelection |= (1 << 7)
light_hw["OS/2"].fsSelection |= (1 << 7)

bold_hw["OS/2"].panose.bProportion = 9
regular_hw["OS/2"].panose.bProportion = 9
light_hw["OS/2"].panose.bProportion = 9

bold_hw["OS/2"].xAvgCharWidth = 500
regular_hw["OS/2"].xAvgCharWidth = 500
light_hw["OS/2"].xAvgCharWidth = 500

simsun = ttLib.TTFont()

with open('simsun_regular.xml', "rb") as f:
    reader = XMLReader(f, simsun)
    reader.read()
    reader.close()
    regular['name'] = simsun['name']

regular.save('simsun.ttf')

nsimsun = ttLib.TTFont()

with open('nsimsun_regular.xml', "rb") as f:
    reader = XMLReader(f, nsimsun)
    reader.read()
    reader.close()
    regular_hw['name'] = nsimsun['name']

regular_hw.save('nsimsun.ttf')

simsunbd = ttLib.TTFont()

with open('simsun_bold.xml', "rb") as f:
    reader = XMLReader(f, simsunbd)
    reader.read()
    reader.close()
    bold['name'] = simsunbd['name']

bold.save('simsunbd.ttf')

nsimsunbd = ttLib.TTFont()

with open('nsimsun_bold.xml', "rb") as f:
    reader = XMLReader(f, nsimsunbd)
    reader.read()
    reader.close()
    bold_hw['name'] = nsimsunbd['name']

bold_hw.save('nsimsunbd.ttf')

simsunl = ttLib.TTFont()

with open('simsun_light.xml', "rb") as f:
    reader = XMLReader(f, simsunl)
    reader.read()
    reader.close()
    light['name'] = simsunl['name']

light.save('simsunl.ttf')

nsimsunl = ttLib.TTFont()

with open('nsimsun_light.xml', "rb") as f:
    reader = XMLReader(f, nsimsunl)
    reader.read()
    reader.close()
    light_hw['name'] = nsimsunl['name']

light_hw.save('nsimsunl.ttf')
