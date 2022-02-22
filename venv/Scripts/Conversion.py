import struct

class conversion:
    try:
        def temp_conversion(self, temp_value):
            hex_aa90 = temp_value
            bytes_aa90 = bytes.fromhex(hex_aa90)
            timestamp_aa90, value_aa90 = struct.unpack('< q d', bytes_aa90)
            return timestamp_aa90, value_aa90

        def rssi_conversion(self, rssi_value):
            hex_rssi = rssi_value
            bytes_rssi = bytes.fromhex(hex_rssi)
            timestamp_rssi, value_rssi = struct.unpack('< q b', bytes_rssi)
            return timestamp_rssi, value_rssi

        def vibration_conversion(self, vib_value):
            hex_xvibration = vib_value
            bytes_vibrations = bytes.fromhex(hex_xvibration)
            timestamp, value_count = struct.unpack('< q i', bytes_vibrations[:12])
            values = list(struct.unpack(f'< {value_count}h', bytes_vibrations[12:]))
            #g_values = [value / 32767 * 16 for value in values]
            #x_p2p = max(g_values) - min(g_values)
            return value_count, timestamp, values


    except Exception as f:
        print("Conversion Error:", f)


