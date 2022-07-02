import fontTools.ttLib as ttLib
from fontTools.misc.xmlReader import XMLReader


bold = ttLib.TTFont('DreamHanSerifCN-W19.ttf')
regular = ttLib.TTFont('DreamHanSerifCN-W7.ttf')

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
