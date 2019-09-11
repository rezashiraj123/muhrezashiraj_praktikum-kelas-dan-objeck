class kelilingLingkaran (object):
    def __init__ (self, p, r):
        self.jarijari = r
        self.phi = p
        def hitungKeliling (self) :
            return self.phi * self.jarijari
        def cetakData (self) :
            print ("jari-jari\t: ", self.jarijari)
            print ("phi\t: ", self.phi)
            def cetakKeliling (self) :
                print ("Keliling\t=", self.hitungKeliling ())

        def main ():
            Kellingkaran1= kelilingLingkaran (60, 3.14)
            print ("object Lingkaran")
            Kellingkaran1.cetakData ()
            Kellingkaran1.cetakKeliling ()

            Kellingkaran2= kelilingLingkaran (90, 22/7)
            print ("\nObject Lingkaran2")
            Kellingkaran2.cetakData ()
            Kellingkaran2.cetakKeliling ()

            if __name__=="__main__":
                main ()
