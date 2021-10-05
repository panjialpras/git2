// function volumeDuakubus(a, b) {
//   var volumeA;
//   var volumeB;
//   var total;

//   volumeA = a * a * a * a;
//   volumeB = b * b * b * b;

//   total = volumeA + volumeB;
//   return total;
// }
// alert(volumeDuakubus(9, 8));

// function tambah() {
//   dipake kalo lebih dari 1 inputan user tanpa repot
//   var hasil = 0;
//   for (var i = 0; i < arguments.length; i++) {
//     hasil += arguments[i];
//   }
//   return hasil;
// }
// var total = tambah(1, 2, 3, 5);
// console.log(total);

// var a = parseInt(prompt("masukkan nilai 1"));
// var b = parseInt(prompt("masukkan nilai 2"));
// // var hasil = tambah(a, b);
// var hasil = tambah(3, 6);

// alert(hasil);

// function angka(n) {
//   if (n === 0) {
//     return;
//   }
//   console.log(n);
//   return angka(n - 1);
// }

// angka(10);

// function pesan(nama) {
//   alert("Halo " + nama);
// }
// pesan("Panji");
var pesan = function (nama) {
  alert("Halo " + nama);
};
pesan("Nji");
