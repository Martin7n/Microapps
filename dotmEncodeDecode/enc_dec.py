import zipfile
import os
import shutil
import re
import xml.etree.ElementTree as ET
from tempfile import mkdtemp

def bookmarks_to_placeholders(input_path, output_path):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    temp_dir = mkdtemp()

    # Extract all contents
    with zipfile.ZipFile(input_path, 'r') as zip_in:
        zip_in.extractall(temp_dir)

    doc_path = os.path.join(temp_dir, 'word', 'document.xml')
    tree = ET.parse(doc_path)
    root = tree.getroot()

    bookmark_names = {}
    open_bookmarks = {}

    for bm in root.iter('{%s}bookmarkStart' % ns['w']):
        bm_id = bm.attrib.get('{%s}id' % ns['w'])
        bm_name = bm.attrib.get('{%s}name' % ns['w'])
        print(f"bookmark_found: {bm_name}, {bm_id}")
        if not bm_name.startswith('_'):
            bookmark_names[bm_id] = bm_name


    def inject_placeholder(elem, text, pos):
        r = ET.Element('{%s}r' % ns['w'])
        t = ET.Element('{%s}t' % ns['w'])
        t.text = text
        r.append(t)
        elem.insert(pos, r)

    def process_elem(elem):
        for i, child in enumerate(list(elem)):
            if child.tag.endswith('}bookmarkStart'):
                bm_id = child.attrib.get('{%s}id' % ns['w'])
                bm_name = bookmark_names.get(bm_id)
                if bm_name:
                    inject_placeholder(elem, f"{{{{{bm_name}}}}}", i)
                    open_bookmarks[bm_id] = bm_name

            elif child.tag.endswith('}bookmarkEnd'):
                bm_id = child.attrib.get('{%s}id' % ns['w'])
                if bm_id in open_bookmarks:
                    del open_bookmarks[bm_id]
            else:
                process_elem(child)

    process_elem(root.find('w:body', ns))
    tree.write(doc_path, xml_declaration=True, encoding='utf-8', method='xml')


    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_out:
        for foldername, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                abs_path = os.path.join(foldername, filename)
                rel_path = os.path.relpath(abs_path, temp_dir)
                zip_out.write(abs_path, rel_path)

    print(f"✅ Bookmarks converted to placeholders: {output_path}")

#test2encode
# bookmarks_to_placeholders("c:/drob/Template1.dotm", "c:/drob/Template2 .dotm")



def placeholders_to_bookmarks(input_path, output_path):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    temp_dir = mkdtemp()
    bookmark_id = 0

    with zipfile.ZipFile(input_path, 'r') as zip_in:
        zip_in.extractall(temp_dir)

    doc_path = os.path.join(temp_dir, 'word', 'document.xml')
    tree = ET.parse(doc_path)
    root = tree.getroot()

    # Regex to match placeholders like {{ClientName}}
    pattern = re.compile(r'\{\{([a-zA-Z0-9_]+)\}\}')

    def create_bookmark(name, bm_id):
        bm_start = ET.Element('{%s}bookmarkStart' % ns['w'], {
            '{%s}id' % ns['w']: str(bm_id),
            '{%s}name' % ns['w']: name
        })
        bm_end = ET.Element('{%s}bookmarkEnd' % ns['w'], {
            '{%s}id' % ns['w']: str(bm_id)
        })
        return bm_start, bm_end

    def process_elem(elem):
        nonlocal bookmark_id
        for i, child in enumerate(list(elem)):
            if child.tag.endswith('}t') and child.text:
                matches = list(pattern.finditer(child.text))
                if matches:
                    parent = elem
                    pos = list(parent).index(child)
                    new_elems = []

                    text = child.text
                    last_index = 0

                    for match in matches:
                        # Add preceding text
                        if match.start() > last_index:
                            t = ET.Element('{%s}t' % ns['w'])
                            t.text = text[last_index:match.start()]
                            r = ET.Element('{%s}r' % ns['w'])
                            r.append(t)
                            new_elems.append(r)

                        name = match.group(1)
                        bm_start, bm_end = create_bookmark(name, bookmark_id)
                        bookmark_id += 1

                        t = ET.Element('{%s}t' % ns['w'])
                        t.text = name
                        print(f"{t.text}:{bookmark_id} bookmark detect")
                        r = ET.Element('{%s}r' % ns['w'])
                        r.append(t)

                        new_elems.extend([bm_start, r, bm_end])
                        last_index = match.end()

                    # Add trailing text
                    if last_index < len(text):
                        t = ET.Element('{%s}t' % ns['w'])
                        t.text = text[last_index:]
                        r = ET.Element('{%s}r' % ns['w'])
                        r.append(t)
                        new_elems.append(r)

                    # Replace the original <w:t> node
                    del parent[pos]
                    for j, ne in enumerate(new_elems):
                        parent.insert(pos + j, ne)

            else:
                process_elem(child)

    process_elem(root.find('w:body', ns))

    tree.write(doc_path, xml_declaration=True, encoding='utf-8', method='xml')

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_out:
        for foldername, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                abs_path = os.path.join(foldername, filename)
                rel_path = os.path.relpath(abs_path, temp_dir)
                zip_out.write(abs_path, rel_path)

    print(f"✅ Placeholders converted to bookmarks: {output_path}")

#test2decode
placeholders_to_bookmarks("c:/drob/Template2 .dotm", "c:/drob/Template2rebuild .dotm")
