def encryption(codes):
    infile = open('info_security.txt', 'r')
    infile_read = infile.read()

    encrypted_file = open('encrypted.txt', 'w')

    for i in infile_read:
        if i in codes:
            encrypted_file.write(codes[i])
        else:
            encrypted_file.write(i)
    encrypted_file.close()

def decryption(codes):
    encrypted_file = open('info_security.txt', 'r')
    encrypted_file_read = encrypted_file.read()

    for i in encrypted_file_read:
        if not i in codes.values() or i == '.' or i == ' ':
            print(i, end='')
        else:
            for k, v in codes.items():
                if i == v:
                    print(k, end='')
def main():
    codes = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', 
             'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'a', 'H':'b', 'h':'c', 'I':'d', 'i':'e', 
             'J':'f', 'j':'g', 'K':'h', 'k':'i', 'L':'j', 'l':'k', 'M':'l', 'm':'n', 'N':'m', 
             'n':'o', 'O':'p', 'o':'q', 'Q':'r', 'q':'s', 'R':'t', 'r':'u', 'S':'v', 
             's':'w','T':'x', 't':'y', 'U':'z', 'u':'A', 'V':'B', 'v':'C', 'W':'D', 'w':'E', 
             'X':'F', 'x':'G', 'Y':'H', 'y':'I', 'Z':'J', 'z':'K'}
    encryption(codes)
    decryption(codes)

main()