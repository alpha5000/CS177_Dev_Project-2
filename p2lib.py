import wave

def write(name,file1,size,output_list):
    output_file = wave.open(name, 'wb')
    output_file.setnchannels(file1.getnchannels())
    output_file.setsampwidth(file1.getsampwidth())
    output_file.setframerate(file1.getframerate())
    output_file.setnframes(size)
    output_file.setcomptype('NONE','not compressed')
    
    output_list = bytearray(output_list)
    output_list = bytes(output_list)
    output_file.writeframes(output_list)
    
    output_file.close()
