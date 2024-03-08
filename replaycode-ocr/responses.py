import ocr

async def get_response_from_ocr(image) -> [str]:
    image_data = await ocr.load_image_from_discord(image)
    template = ocr.load_template(template_filename="images/template_proc.jpg")
    #location = ocr.template_match(image_data, template)
    response: [str] = ocr.parse_image(image_data, template)

    if response:
        return replaycodes_to_string(response)
    else:
        return "Error."

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