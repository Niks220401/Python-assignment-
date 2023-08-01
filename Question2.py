def create_file_extension_dict(file_list):
    file_extension_dict = {}
    for file_name in file_list:
        # Split the file name into name and extension parts
        name, extension = file_name.split('.')
        # If the file has multiple extensions, consider only the last one
        extension = '.' + extension.split('.')[-1]
        
        # If the extension is .ppt.txt, consider it as .txt
        if extension == '.ppt.txt':
            extension = '.txt'
        
        # Add the file name to the corresponding extension key in the dictionary
        if extension in file_extension_dict:
            file_extension_dict[extension].append(file_name)
        else:
            file_extension_dict[extension] = [file_name]
    
    return file_extension_dict

file_list = ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]

result_dict = create_file_extension_dict(file_list)
print(result_dict)