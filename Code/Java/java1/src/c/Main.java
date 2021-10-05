public class Main {
    public static void main(String[] args) {
        
        // membuat objek bangun datar
        bangunDatar bangunDatar = new bangunDatar();
        
        // membuat objek persegi dan mengisi nilai properti
        persegi persegi = new persegi();
        persegi.sisi = 2;
        
        // membuat objek Lingkaran dan mengisi nilai properti
        lingkaran lingkaran = new lingkaran();
        lingkaran.r = 22;
        
        // membuat objek Persegi Panjang dan mengisi nilai properti
        persegiPanjang persegiPanjang = new persegiPanjang();
        persegiPanjang.panjang = 8;
        persegiPanjang.lebar = 4;
        
        // membuat objek Segitiga dan mengisi nilai properti
        segitiga mSegitiga = new segitiga();
        mSegitiga.alas = 12;
        mSegitiga.tinggi = 8;
        
        
        // memanggil method luas dan keliling
        bangunDatar.luas();
        bangunDatar.keliling();
        
        persegi.keliling();
        persegi.luas();
        
        lingkaran.luas();
        lingkaran.keliling();
        
        persegiPanjang.luas();
        persegiPanjang.keliling();
        
        mSegitiga.luas();
        mSegitiga.keliling();
    }
}
