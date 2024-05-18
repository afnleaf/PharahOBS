# local module
import ocr

# manage input image being processed by the ocr
async def get_response_from_ocr(message_id, image, list_of_templates) -> [str]:
    try:
        image_data = await ocr.load_image_from_discord(image)
        crops, map_crops = ocr.template_match(image_data, list_of_templates)        
        # ocr on crops
        replaycodes = ocr.process_codes(crops)
        # image processing on maps
        list_of_maps = ocr.process_maps(map_crops)
        
        if replaycodes:
            return replaycodes_to_string(message_id, replaycodes, list_of_maps)
        else:
            return None
    except Exception as e:
        print(e)
        return None
    #response: [str] = ocr.parse_image(image_data, template)


# load templates into memory early
def load_templates(template_filename):
    try:
        template = ocr.load_template(template_filename)
    except Exception as e:
        print(e)
        return None
    # should be created outside
    list_of_templates = ocr.create_templates(template)
    return list_of_templates


# turns replaycode list into message to be posted by the bot, add message_id
def replaycodes_to_string(message_id: str, replaycodes: [str], maps: [str]) -> str:
    text: str = ""
    text += f"{message_id}\n\n"
    for i, code in enumerate(replaycodes):
        text += maps[i] + ":\t\t" + code + "\n"
    return text
