import hid
import sys

sys.stdout.reconfigure(encoding='utf-8')

avoid_strings = ['Razer Basilsk X HyperSpeed', 'DualSense Wireless Controller', 'DualShock 4 Wireless Controller', 'Xbox Wireless Controller', 'AMD SR4 lamplight Control', 'AMD SR4 lamplight control', 'AMD SR4 Lamplight Control', 'AMD SR4 Lamplight Control'
                 , 'Blue Snowball', 'Blue Snowball iCE']

#find all devices with 9610 vid and 269 pid
for device in hid.enumerate():
    if device['vendor_id'] == 9610 and device['product_id'] == 269:
        print("Path:", device["path"])
        print("device:", device['product_string'])
        print("interface_number:", device['interface_number'])
        print('usage_page', device['usage_page'])
        print('usage', device['usage'])
        print("vid:", device['vendor_id'], "pid:", device['product_id'])
        print()

h1 = hid.device()
h1.open_path(
    b'\\\\?\\HID#VID_258A&PID_010D&MI_01&Col03#b&17ceb4e7&0&0002#{4d1e55b2-f16f-11cf-88cb-001111000030}'
)
print("opened h1")
print("h1 open:", h1)

#try zero-filled report to see if interface accepts output reports
h1.write(bytes([0] * 64))

#try feature report to see if interface accepts feature reports
h1.send_feature_report(bytes([0] * 65))

#try receiving a report to see if interface sends input reports

h1.get_feature_report(2, 65)
    


h1.close()

h2 = hid.device()
h2.open_path(
    b'\\\\?\\HID#VID_258A&PID_010D&MI_01&Col05#b&17ceb4e7&0&0004#{4d1e55b2-f16f-11cf-88cb-001111000030}'
)
print("opened h2")
print("h2 open:", h2)

#try zero-filled report to see if interface accepts output reports
h2.write(bytes([0] * 64))

#try feature report to see if interface accepts feature reports
h2.send_feature_report(bytes([0] * 65))

#try receiving a report to see if interface sends input reports
h2.get_feature_report(2, 65)

h2.close()