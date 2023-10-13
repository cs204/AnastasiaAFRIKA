def get_file_mime_type(file_name):
    if file_name.endswith('.gif'):
        return 'image/gif'
    elif file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        return 'image/jpeg'
    elif file_name.endswith('.png'):
        return 'image/png'
    elif file_name.endswith('.pdf'):
        return 'application/pdf'
    elif file_name.endswith('.txt'):
        return 'text/plain'
    elif file_name.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'

file_name = input("File name: ")
mime_type = get_file_mime_type(file_name)
print(f"{mime_type}")