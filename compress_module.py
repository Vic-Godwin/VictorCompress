import zlib,base64

def compress(file):#,outputfile):
    
    try:
        data = open(file, 'r').read()
    except FileNotFoundError as e:
        print(f"{e}")

    data_bytes = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
    return compressed_data
    #decoded_data = compressed_data.decode('utf-8')
    #compressed_file = open(outputfile,'w')
    #compressed_file.write(decoded_data)

def decompress(file):#,outputfile):
    file_content = open(file,'r').read()
    encode_file_content = file_content.encode('utf-8')
    decompress_file_content = zlib.decompress(base64.b64decode(encode_file_content))
    decode_content = decompress_file_content
    return decode_content
    #new_file = open(outputfile, 'w')
    #new_file.write(decode_content)
    #new_file.close()
