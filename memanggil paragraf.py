class MyFile (object) :
def __init__ (sef, namafile):
print ("Membuka file %s... \n" %namafile)
self.file = open (namafie)
def __del__ (self):
print (\nMenutup file...")
self.file.close ()
def bacadata (self) :
for baris in self.file :
print (baris, end= "")

def main ():
f= MyFile ("D:/aplikasi/python/paragraf.txt")
f= bacadata()
if __name__ == " __main__ ":
main ()
