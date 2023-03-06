class Dimas:
  def _init_(self, nama, NIM, kelasPBO, SKS):
    self.nama = nama
    self.NIM = NIM
    self.kelasPBO = kelasPBO
    self.SKS = SKS

  def info(self):
    print("Nama : " + self.nama )
    print("NIM : " + self.NIM )
    print("Kelas PBO Siakad : " + self.kelasPBO )
    print("SKS : " + self.SKS )

Objek = Dimas("Dimas Faturrohim", "121140224", "RD", "21")

Objek.info()