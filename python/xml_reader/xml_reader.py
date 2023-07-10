from xml.dom import minidom

def xml_to_dialogue(xml_file_path, target_file_path):

    NEW_LINE = "\n\n"
    SEPARATOR = ": "

    # Open XML and target file
    xml_object = minidom.parse(xml_file_path)
    target_file = open(target_file_path, 'w', encoding='utf-8')

    not_empty = False

    utterances = xml_object.getElementsByTagName('S')
    for utt in utterances:
        dialogue = utt.getElementsByTagName('FORM')[0].firstChild.data
        speaker = utt.attributes['who'].value
        target_file.writable

        if not_empty:
            target_file.write('\n\n')
        else:
            not_empty = True
        
        target_file.write(speaker + SEPARATOR + dialogue)

xml_to_dialogue('../../resource/archive/xml_pfc_example.xml', 'output/dialogue_test.txt')