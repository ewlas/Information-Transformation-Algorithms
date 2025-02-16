import sys

def rle_encode(data: bytes) -> bytes:
    encoded = bytearray()
    i = 0
    
    while i < len(data):
        run_length = 1
        while i + run_length < len(data) and run_length < 129 and data[i] == data[i + run_length]:
            run_length += 1
        
        if run_length > 1:
            encoded.append(128 + run_length - 2)
            encoded.append(data[i])
            i += run_length
        else:
            start = i
            while i + 1 < len(data) and (i - start) < 127 and data[i] != data[i + 1]:
                i += 1
            encoded.append(i - start)
            encoded.extend(data[start:i + 1])
            i += 1
    
    return bytes(encoded)

def rle_decode(data: bytes) -> bytes:
    decoded = bytearray()
    i = 0
    
    while i < len(data):
        length_byte = data[i]
        i += 1
        
        if length_byte >= 128:
            run_length = length_byte - 128 + 2
            byte_value = data[i]
            i += 1
            decoded.extend([byte_value] * run_length)
        else:
            run_length = length_byte + 1
            decoded.extend(data[i:i + run_length])
            i += run_length
    
    return bytes(decoded)

def main():
    if len(sys.argv) < 3:
        return
    
    mode, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    
    with open(input_file, "rb") as f:
        data = f.read()
    
    if mode == "encode":
        result = rle_encode(data)
    elif mode == "decode":
        result = rle_decode(data)
    else:
        print("invalid. Use 'encode' or 'decode'.")
        return
    
    with open(output_file, "wb") as f:
        f.write(result)
    
    print(f"Operation {mode} completed successfully.")

if __name__ == "__main__":
    main()
