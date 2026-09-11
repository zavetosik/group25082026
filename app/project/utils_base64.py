import base64

string = b'hello - ()*/'

encode = base64.b64encode(string)
print(encode)

decoded = base64.b64decode(encode)
print(decoded)


html_template = """
<img src="data:image/png;base64,{image_base64}">
"""



with open('spring.png', 'rb') as file:
    image_bytes = file.read()
    print(image_bytes)

    image_base64 = base64.b64encode(image_bytes).decode('ascii')
    print(image_base64)

    with open('index.html', 'w', encoding='utf-8') as html_file:
        content = html_template.format(image_base64=image_base64)
        html_file.write(content)