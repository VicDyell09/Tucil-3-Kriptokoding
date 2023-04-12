import hashlib
import filereader
import RSA


def hashText(text):
    hash = hashlib.new("sha3_224", text.encode())
    return hash.hexdigest()

def generateDigitalSigned(filename, privatekey):
    if filereader.fileext(filename) == ".txt":
        text = filereader.readfile(filename) 
    else:
        text = filereader.readfilebin(filename)
    digest = hashText(text)
    key = filereader.readkey(privatekey)
    d = int(key[2])
    N = int(key[1])
    signature = RSA.dekripsihex(d, N, digest) #enkripsi dengan private key
    new_signature = "\n---Begin of Digital Signature---\n"+signature+"\n---End of Digital Signature---" 
    if filereader.fileext(filename) == ".txt":
        filereader.appendfile(new_signature,filename)  
    else:
        filereader.writefile(new_signature,filename)

def validateDigitalSigned(filename, publickey, filesig=""):
    key = filereader.readkey(publickey)
    e = int(key[2])
    N = int(key[1])
    if filereader.fileext(filename) == ".txt":
        text = filereader.readfile(filename)
        isi = text.split("\n---Begin of Digital Signature---\n")
        digest = hashText(isi[0])
        isisig = text.split("---Begin of Digital Signature---\n")
    else:
        text = filereader.readfilebin(filename)
        digest = hashText(text)
        isisig = filereader.readfile(filesig).split("---Begin of Digital Signature---\n")
    plaintext = isisig[1].split("\n---End of Digital Signature---")
    signature = plaintext[0]
    signatureDigest = RSA.enkripsihex(e,N,signature)
    digests = ""
    for c in digest: 
        digests += str(ord(c))
    hexdigest = hex(int(digests))
    if hexdigest == signatureDigest:
        return("Valid")
    else:
        return("Tidak Valid")


# generateDigitalSigned("dea.docx", "del.pri")
# validateDigitalSigned("dea.docx","del.pub","dea.txt")

# generateDigitalSigned("aed.txt", "del.pri")
# validateDigitalSigned("aed.txt","del.pub")