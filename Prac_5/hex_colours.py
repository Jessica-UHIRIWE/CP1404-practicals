COLOR_CODES = {"aliceblue": '#f0f8ff', "antiquewhite": "#faebd7", "aqua": '#00ffff', "aquamarine": '#7fffd4',
               "azure": '#f0ffff', "beige": "#f5f5dc", "bisque": '#ffe4c4', "black": '#000000',
               "blanchedalmond": '#ffebcd', "blue": '#0000ff'}


def get_color_code(color_name):
    color_name = color_name.lower()
    return COLOR_CODES.get(color_name)


def main():
    while True:
        color_name = input("Enter a color name (or press Enter to stop): ").strip()
        if color_name == "":
            break
        color_code = get_color_code(color_name)
        if color_code:
            print(f"The code for {color_name} is {color_code}.")
        else:
            print("Invalid color name. Please try again.")


main()
