from fontTools.ttLib import TTFont, TTCollection

import copy
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def open_ttc(ttc_file_path: str) -> TTCollection:
    # Open the TTC file
    ttc = TTCollection(ttc_file_path)
    font_count = len(ttc.fonts)
    logger.info(f"There are {font_count} font(s) in the ttc collection {ttc_file_path}. ")
    return ttc

def fonts_in_ttc(ttc : TTCollection) -> dict:
    ret = {}
    for font_number, font in enumerate(ttc.fonts):
        name_table = font["name"]
        # Get the font's full name (nameID 4, platformID 3, encodingID 1, languageID 0x409 for Windows and English)
        full_name_record = name_table.getName(4, 3, 1, 0x409)
        full_name = full_name_record.toUnicode() if full_name_record else "Unknown Font Name"
        ret[full_name] = font
        logger.info(f"Font {font_number}: {full_name}")
    return ret

def apply_gsub_substitution(font: TTFont) -> TTFont:
    # Load the font file
    output_font = copy.deepcopy(font)
    replace = {}
    # Access the GSUB table
    if 'GSUB' not in font:
        logger.info("This font does not have a GSUB table.")
        return
    
    gsub_table = font['GSUB']
    
    # Check the available features in the GSUB table
    hwid_feature = None
    for feature in gsub_table.table.FeatureList.FeatureRecord:
        if feature.FeatureTag == 'hwid':
            hwid_feature = feature
            break

    if hwid_feature is None:
        logger.info("The 'hwid' feature is not available in this font.")
        return

    # 'hwid' feature found, now check its lookups
    logger.info(f"Found 'hwid' feature with {len(hwid_feature.Feature.LookupListIndex)} lookups.")
    
    # Let's look at each lookup in the 'hwid' feature and inspect the substitutions
    lookups = gsub_table.table.LookupList.Lookup
    for lookup_index in hwid_feature.Feature.LookupListIndex:
        lookup = lookups[lookup_index]
        logger.info(f"Processing lookup {lookup_index} of type {lookup.LookupType}")

        # The type of lookup (e.g., single substitution, multiple substitution, etc.)
        if lookup.LookupType == 1:  # Single substitution lookup
            for sub_table in lookup.SubTable:
                if hasattr(sub_table, 'mapping'):  # SingleSubstFormat
                    for glyph, substitute in sub_table.mapping.items():
                        if glyph not in replace:
                            logger.info(f"Add substitution glyph '{glyph}' -> '{substitute}'")
                            replace[glyph] = substitute
                        else:
                            logger.info("Substitutions conflict!")
                            replace[glyph] = substitute
        else:
            logger.warning("Unsupported lookup type.")
    
    
    for t in output_font["cmap"].tables:
        for unicode, name in t.cmap.items():
            if name in replace:
                logger.info(f"Updated cmap: U+{unicode:04X}, substitute glyph '{name}' with '{replace[name]}'")
                t.cmap[unicode] = replace[name]

    return output_font

if __name__ == "__main__":
    light = TTFont("SourceHanSerifSC-Light.otf")
    regular = TTFont("SourceHanSerifSC-Regular.otf")
    bold = TTFont("SourceHanSerifSC-Bold.otf")
    apply_gsub_substitution(light).save("SourceHanSerifSCHW-Light.otf")
    apply_gsub_substitution(regular).save("SourceHanSerifSCHW-Regular.otf")
    apply_gsub_substitution(bold).save("SourceHanSerifSCHW-Bold.otf")
