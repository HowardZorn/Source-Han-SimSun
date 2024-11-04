import fontTools.ttLib as ttLib
from fontTools.misc.xmlReader import XMLReader


bold = ttLib.TTFont('DreamHanSerifCN-W20.ttf')
regular = ttLib.TTFont('DreamHanSerifCN-W7.ttf')
light = ttLib.TTFont('DreamHanSerifCN-W3.ttf')

# Use typography metrics for line spacing.
# To enable USE_TYPO_METRICS flag in OS/2, set the 8-th bit as 1.
# Reference: https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection
bold["OS/2"].fsSelection |= (1 << 7)
regular["OS/2"].fsSelection |= (1 << 7)
light["OS/2"].fsSelection |= (1 << 7)

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
    regular['name'] = nsimsun['name']

regular.save('nsimsun.ttf')

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
    bold['name'] = nsimsunbd['name']

bold.save('nsimsunbd.ttf')

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
    light['name'] = nsimsunl['name']

light.save('nsimsunl.ttf')
