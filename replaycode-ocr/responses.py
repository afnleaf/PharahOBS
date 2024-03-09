import ocr


async def get_response_from_ocr(image, list_of_templates) -> [str]:
    image_data = await ocr.load_image_from_discord(image)
    crops = ocr.template_match(image_data, list_of_templates)
    replaycodes = ocr.process_codes(crops)
    
    #response: [str] = ocr.parse_image(image_data, template)

    if replaycodes:
        return replaycodes_to_string(replaycodes)
    else:
        return "Error."


def load_templates():
    template_filename="images/template_large.png"
    template = ocr.load_template(template_filename)
    # should be created outside
    list_of_templates = ocr.create_templates(template)
    return list_of_templates


def replaycodes_to_string(replaycodes: [str]) -> str:
    text: str = ""
    for code in replaycodes:
        text += code + "\n"
    return text

'''
def validate_image(image):
    image_data = await ocr.load_image_from_discord(image)
    template = ocr.load_template(template_filename="images/template_proc.jpg")
    return True
'''