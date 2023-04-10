import sys
import hashlib
import filereader
import RSA


def hashText(text):
    hash = hashlib.new("sha3_224", text.encode())
    # print("\nSHA3-512 Hash: ", hash_sha3_512.hexdigest())
    return hash.hexdigest()

def generateDigitalSigned(filename, privatekey):
    text = filereader.readfile(filename)
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
    text = filereader.readfile(filename)
    isi = text.split("\n---Begin of Digital Signature---\n")
    digest = hashText(isi[0])
    key = filereader.readkey(publickey)
    e = int(key[2])
    N = int(key[1])
    if filereader.fileext(filename) == ".txt":
        isi = text.split("---Begin of Digital Signature---\n")
        plaintext = isi[1].split("\n---End of Digital Signature---")
        signature = plaintext[0] 
    else:
        isi = filereader.readfile(filesig).split("---Begin of Digital Signature---\n")
        plaintext = isi[1].split("\n---End of Digital Signature---")
        signature = RSA.dekripsi(e, N, plaintext[0]) 
    signatureDigest = RSA.enkripsihex(e,N,signature)
    digests = ""
    for c in digest: 
        digests += str(ord(c))
    hexdigest = hex(int(digests))
    if hexdigest == signatureDigest:
        print("Valid")
    else:
        print("Tidak Valid")


# generateDigitalSigned("test.txt", "del.pri")
validateDigitalSigned("test.txt","del.pub")