class LuasLingkaran (object):
    def __init__ (self, p, r):
        self.jarijari = r
        self.phi = p
        def hitungLuas (self) :
            return self.phi * self.jarijari * self.jarijari
        def cetakData (self) :
            print ("jari-jari\t: ", self.jarijari)
            print ("phi\t: ", self.phi)
            def cetakKeliling (self) :
                print ("Luas\t=", self.hitungLuas ())

        def main ():
            Llingkaran1= Luaslingkaran (24, 3.14)
            print ("object Lingkaran")
            Llingkaran.cetakData ()
            Llingkaran.cetakLuas ()

            Llingkaran2= LuasLingkaran (48, 22/7)
            print ("\nObject Lingkaran2")
            Llingkaran2.cetakData ()
            Llingkaran2.cetakLuas ()

            if __name__=="__main__":
                main ()
