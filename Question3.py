import re

def extract_common_format(strings_list):
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"
    common_formats = [re.search(pattern, string).group() for string in strings_list if re.search(pattern, string)]
    return common_formats

strings_list = [
    "random_2020-05-04 18:08_string",
    "random_string_2019-02-12 12:00",
    "string_random_2019-02-15 16:00",
    # Add more strings with the same format here if needed
]

result = extract_common_format(strings_list)
print(result)