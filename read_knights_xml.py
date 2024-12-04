import lxml.etree as et

doc = et.parse("knights.xml")

for knight in doc.findall('knight'):
    title = knight.get('title')  # get XML tag attribute
    name = knight.findtext('name')  # get text contained in tag
    print(f"{title} {name}")
print('-' * 60)
for color in doc.findall('color'):
    print(color.text)
