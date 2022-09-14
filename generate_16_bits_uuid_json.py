#!/usr/bin/env python3

import sys
import fitz
import json

ROW_FIRST_COLUMN = [
    "16-bit UUID for Members",
    "GATT Characteristic and Object Type",
    "GATT Declarations ",
    "GATT Descriptor",
    "GATT Service",
    "GATT Unit ",
    "Protocol Identifier",
    "SDO GATT Service",
    "Service Classes and Profiles",
]

def main(argc, argv):
    if argc != 2:
        sys.exit("USAGE: ./generate_16_bits_uuid_json.py doc.pdf")

    try:
        doc = fitz.open(argv[1])
    except:
        sys.exit("Error opening file");


    output = {
    }
    for k in ROW_FIRST_COLUMN:
        output[k] = []

    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        text = page.get_text("text").split('\n')
        for i in range(len(text)):
            if text[i] in ROW_FIRST_COLUMN:
                output[text[i]].append({"uuid": text[i+1], "name": text[i+2]})

    with open("ble_16_bits_uuids.json", "w") as outfile:
        json.dump(output, outfile, indent=4)

    print("OK")

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
