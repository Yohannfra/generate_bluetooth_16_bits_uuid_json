# generate_bluetooth_16_bits_uuid_json

A little script to generate a json file from the content of [this pdf](https://btprodspecificationrefs.blob.core.windows.net/assigned-values/16-bit%20UUID%20Numbers%20Document.pdf) that describes all ble 16-bits identifiers.

I made this script to easily generate a dictionary to get identifier name from 16 bit raw bytes (for [this program](https://github.com/Yohannfra/ble_repl))

## Access fields

The [generated json](./ble_16_bits_uuids.json) is composed of these arrays:

```json
    "16-bit UUID for Members": [],
    "GATT Characteristic and Object Type": [],
    "GATT Declarations ": [],
    "GATT Descriptor": [],
    "GATT Service": [],
    "GATT Unit ": [],
    "Protocol Identifier": [],
    "SDO GATT Service": [],
    "Service Classes and Profiles": [],
```

And all identifiers are objects with the 16 bits identifier as key and a string value.

eg.
```json
{
    "0xFCE8 ": "ITT Industries"
},
```
