import hid
import sys

sys.stdout.reconfigure(encoding='utf-8')

avoid_strings = ['Razer Basilsk X HyperSpeed', 'DualSense Wireless Controller', 'DualShock 4 Wireless Controller', 'Xbox Wireless Controller', 'AMD SR4 lamplight Control', 'AMD SR4 lamplight control', 'AMD SR4 Lamplight Control', 'AMD SR4 Lamplight Control'
                 , 'Blue Snowball', 'Blue Snowball iCE']

for device_dict in hid.enumerate():
    keys = list(device_dict.keys())
    keys.sort()
    for key in keys:
        #look for same vid and pid appearing multiple ttimes but different interface_number
        if key == 'interface_number' and device_dict[key] != -1 and device_dict['product_string'] not in avoid_strings:
            print("device:", device_dict['product_string'])
            print("interface_number:", device_dict[key])
            print("vid:", device_dict['vendor_id'], "pid:", device_dict['product_id'])
    print()


h = hid.device()
h.open(9610, 269)  # VendorID, ProductID

print("using device:", h.get_manufacturer_string(), h.get_product_string(), h.get_serial_number_string())