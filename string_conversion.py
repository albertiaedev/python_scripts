def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


# The main function converts a PascalCaseString or camelCaseString into a snake_case_string
def main():
    print(convert_to_snake_case('convertToSnakeCase'))

main()