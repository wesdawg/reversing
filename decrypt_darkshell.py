def decrypt_darkshell(cipherbytes, start_idx=0x04, stop_idx=0xA8):
   """     
   De-obfuscates Darkshell comms encoded using the following method:
     cipherbyte = 0xDE - [plainbyte - (plainbyte & 0x10) << 1]
   The obfuscation is reversed as follows:
     intermediate = 0xDE - cipherbyte
     plainbyte = intermediate + (intermediate & 0x10) << 1
   """    
   len_mesg = len(cipherbytes)
   if len_mesg != 260:
       raise RuntimeError("Darkshell bot-to-CnC comms are always 260 bytes")
   plainbytes = []
   for cipherbyte in cipherbytes[start_idx:stop_idx]:
       intermediate= 0xDE - ord(cipherbyte)
       plainbytes += [chr(intermediate + ((intermediate & 0x10) << 1))]
   return cipherbytes[:start_idx] + ''.join(plainbytes) + cipherbytes[stop_idx:]
