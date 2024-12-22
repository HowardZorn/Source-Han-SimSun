import fontTools.ttLib as ttLib
from utils import apply_gsub_substitution, remove_ligatures
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

ignored_glyphs = {'uniFF12', 'uniFF0A', 'uniFF0B', 'uniFF17', 'uni301C', 'uniFF45', 
                  'uniFF48', 'uniFF35', 'uniFF4A', 'uniFF14', 'uniFF3A', 'uniFF24', 
                  'uniFF2A', 'uniFF2D', 'uniFF41', 'uniFF16', 'uniFF06', 'uniFF1D', 
                  'uniFF53', 'uniFF54', 'uniFF38', 'uniFF55', 'uniFF2C', 'uniFF19', 
                  'uniFF27', 'uniFF32', 'uniFF42', 'uniFF1C', 'uniFF3B', 'uniFF4B', 
                  'uniFF4D', 'uniFF2F', 'uniFF3E', 'uniFF26', 'uniFF25', 'uni2215', 
                  'uniFF18', 'uniFF1E', 'uniFF04', 'uniFF46', 'uniFF5B', 'uniFF58', 
                  'uniFF50', 'uniFF21', 'uniFF47', 'uniFF31', 'uni2003', 'uniFF0D', 
                  'uniFF02', 'uniFF4F', 'uniFF11', 'uniFF23', 'uniFF57', 'uniFF34', 
                  'uniFF3F', 'uniFF56', 'uniFF59', 'uniFF09', 'uniFF0C', 'uniFF08', 
                  'uniFF43', 'uniFF0E', 'uniFF2E', 'uniFF29', 'uniFF51', 'uniFF07', 
                  'uniFF30', 'uniFFE6', 'uniFF36', 'uniFF5C', 'uniFF10', 'uniFF44', 
                  'uniFF15', 'uniFF39', 'uniFF2B', 'uniFF03', 'uniFF52', 'uniFF5D', 
                  'uniFF05', 'uniFF13', 'uniFF37', 'uniFF33', 'uniFF28', 'uni2035', 
                  'uniFF22', 'uniFF5A', 'uniFF3D', 'uniFFE5', 'uniFF49', 'uniFF4C', 
                  'uniFF3C', 'uniFF4E', 'uniFF20'}
bold_hw = apply_gsub_substitution(bold, ignored_glyphs)
bold_hw = remove_ligatures(bold_hw)
regular_hw = apply_gsub_substitution(regular, ignored_glyphs)
regular_hw = remove_ligatures(regular_hw)
light_hw = apply_gsub_substitution(light, ignored_glyphs)
light_hw = remove_ligatures(light_hw)

bold_hw["OS/2"].panose.bProportion = 9
regular_hw["OS/2"].panose.bProportion = 9
light_hw["OS/2"].panose.bProportion = 9

bold_hw["OS/2"].xAvgCharWidth = 1024
regular_hw["OS/2"].xAvgCharWidth = 1024
light_hw["OS/2"].xAvgCharWidth = 1024

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
