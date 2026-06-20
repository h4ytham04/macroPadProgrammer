import hid
import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

PATH = b'\\\\?\\HID#VID_258A&PID_010D&MI_01&Col03#b&17ceb4e7&0&0002#{4d1e55b2-f16f-11cf-88cb-001111000030}'

h = hid.device()
h.open_path(PATH)
print('[OK] opened Col03')

# 1. Try reading back with report ID 5
print('\n-- get_feature_report with ID 5, various lengths --')
for length in (8, 16, 32, 64, 65):
    try:
        data = h.get_feature_report(5, length)
        print(f'  get(5, {length}) -> {bytes(data).hex()}')
    except Exception as e:
        print(f'  get(5, {length}) -> FAIL: {repr(e)}')

# 2. Try send with report ID 5 and different lengths
print('\n-- send_feature_report ID 5, various lengths --')
for length in (8, 16, 32, 64, 65):
    try:
        ret = h.send_feature_report([5] + [0] * (length - 1))
        print(f'  send(5, {length} total) -> {ret}')
    except Exception as e:
        print(f'  send(5, {length} total) -> FAIL: {repr(e)}')

# 3. Try adjacent report IDs with 65 bytes total
print('\n-- send_feature_report IDs 0-16, 65 bytes total --')
for rid in range(0, 17):
    try:
        ret = h.send_feature_report([rid] + [0] * 64)
        print(f'  send({rid}, 65) -> {ret}')
    except Exception as e:
        print(f'  send({rid}, 65) -> FAIL: {repr(e)}')

# 4. After successful send, try reading back
print('\n-- send ID 5 then immediately read back --')
try:
    sent = h.send_feature_report([5] + [0] * 64)
    print(f'  sent -> {sent}')
    time.sleep(0.05)
    data = h.get_feature_report(5, 65)
    print(f'  read -> {bytes(data).hex()}')
except Exception as e:
    print(f'  FAIL: {repr(e)}')

h.close()
