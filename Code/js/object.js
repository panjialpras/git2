// membuat object
// var mhs = {
//   nama: "Panji Al Muqsith", // object
//   umur: 19,
//   //
//   ips: [3.12, 3.33, 3.45], // property
//   alamat: {
//     jalan: "Jl. UKH No. 123",
//     kota: "Bekasi",
//     provinsi: "Jawa Barat",
//   },
// };

// Object Literal
var mhs1 = {
  nama: "Panji Al Muqsith",
  nim: "5200411249",
  email: "panjiallazusa@gmail.com",
  jurusan: "Teknik Informatika",
};
var mhs2 = {
  nama: "Prasetyo",
  nim: "5200411248",
  email: "pras@gmail.com",
  jurusan: "Teknik Informatika",
};

// Function Declaration
function crateObjectMhs(nama, nim, email, jurusan) {
  var mhs = {};
  mhs.nama = nama;
  mhs.nim = nim;
  mhs.email = email;
  mhs.jurusan = jurusan;
  return mhs;
}

var mhs3 = crateObjectMhs("Hendra", "500411222", "hendrakece23@gmail.com", "Teknik Informatika");

// Constructor, function khusus buat object
function Murid(nama, nim, email, jurusan) {
  this.nama = nama;
  this.nim = nim;
  this.email = email;
  this.jurusan = jurusan;
}
var murid = new Murid("Endry", "5200411112", "end12@gmail.com", "Kedokteran");
