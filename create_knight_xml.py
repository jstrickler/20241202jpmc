import lxml.etree as et

knight_root = et.Element("knights")

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_tag = et.SubElement(knight_root, "knight", title=title)
        et.SubElement(knight_tag, "name").text = name
        color_tag = et.SubElement(knight_tag, "color")
        color_tag.text = color
        et.SubElement(knight_tag, 'quest').text = quest
        et.SubElement(knight_tag, "comment").text = comment


knight_xml = et.tostring(knight_root, pretty_print=True, xml_declaration=True).decode()
print(knight_xml)

knight_doc = et.ElementTree(knight_root)
knight_doc.write('knights.xml', pretty_print=True, xml_declaration=True)
# print(dir(knight_doc))


