import struct 
import os
# 支持文件类型 
# 用16进制字符串的目的是可以知道文件头是多少字节 
# 各种文件头的长度不一样，少半2字符，长则8字符 
def typeList(): 
    return {
        "FFD8FF": 'jpg',
        "2320": 'py'
        } 
  

# 字节码转16进制字符串 
def bytes2hex(bytes): 
    num = len(bytes) 
    hexstr = u""
    for i in range(num): 
        t = u"%x" % bytes[i] 
        if len(t) % 2: 
            hexstr += u"0" 
        hexstr += t 
    return hexstr.upper() 
  
# 获取文件类型 
def filetype(filename): 
    binfile = open(filename, 'rb') # 必需二制字读取 
    tl = typeList() 
    ftype = 'unknown' 
    for hcode in tl.keys(): 
        # print('1',hcode)
        numOfBytes = len(hcode)// 2 # 需要读多少字节 
        binfile.seek(0) # 每次读取都要回到文件头，不然会一直往后读取 
        hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes)) # 一个 "B"表示一个字节 
        # print(hbytes)
        f_hcode = bytes2hex(hbytes) 
        print('3',f_hcode)
        if f_hcode == hcode: 
            ftype = tl[hcode] 
            break
    #不要忘记关闭打开的文件，避免出现异常
    binfile.close() 
    return ftype
  
if __name__ == '__main__': 
    print(filetype('1.jpg'))
    print(filetype('list.py'))
    for i in os.listdir('.'):
        if not os.path.isdir(i):
            print(i,filetype(i))