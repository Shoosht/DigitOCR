from util import *
from PIL import ImageOps


def display_digits(digits):
    if digits == "":
        return False
    centered_text(digits)
    return True


centered_title("Digital Number Recognition")

image_info = st.file_uploader("", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=False)

if image_info is not None:
    image_file = load_image(image_info)

    if image_file is not None:
        show_image(image_file)

        if not display_digits(read_digits(image_file, False, True)):
            if not display_digits(read_digits(ImageOps.invert(image_file), False, True)):
                if not display_digits(read_digits(image_file, True, True)):
                    if not display_digits(read_digits(ImageOps.invert(image_file), True, True)):
                        centered_text("NO DIGITS FOUND")
