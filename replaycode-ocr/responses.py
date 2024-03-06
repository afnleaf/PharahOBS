import ocr



async def get_response(image) -> str:
    image_data = await ocr.load_image_from_url(image)
    template = "images/template_proc.jpg"
    ocr.parse_image(image_data, template)
    return 



'''
async def get_response1(image_url: str) -> str:
    image_data = await ocr.load_image_from_url(image_url)
    template = "images/template_proc.jpg"
    parse_image(image_data, template)
    return 
'''

'''
from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "well you're awfully silent..."
    elif "hello" in lowered:
        return "Hello there!"
    elif "how are you" in lowered:
        return "Good, thanks!"
    elif "bye" in lowered:
        return "Cya"
    elif "roll dice" in lowered:
        return f"You rolled: {randint(1,6)}"
    else:
        return choice(["test1", "test2", "test3"])
'''

