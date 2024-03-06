import ocr

async def get_response(image) -> [str]:
    image_data = await ocr.load_image_from_discord(image)
    template = "images/template_proc.jpg"
    response: [str] = ocr.parse_image(image_data, template)
    return response

def replaycodes_to_string(replaycodes: [str]) -> str:
    text: str = ""
    for code in replaycodes:
        text += code + "\n"
    return text