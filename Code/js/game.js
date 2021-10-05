var tanya = true;
while (tanya) {
  var p = prompt("Pilih : gajah, semut, orang");

  var comp = Math.random();

  if (comp < 0.34) {
    comp = "gajah";
  } else if (comp >= 0.34 && comp < 0.67) {
    comp = "orang";
  } else {
    comp = "semut";
  }

  var hasil = "";
  if (p == comp) {
    hasil = "Seri!";
  } else if (p == "gajah") {
    hasil = comp == "orang" ? "Menang!" : "Kalah!";
  } else if (p == "orang") {
    hasil = comp == "gajah" ? "Kalah" : "Menang";
  } else if (p == "semut") {
    hasil = comp == "orang" ? "Kalah!" : "Menang!";
  } else {
    hasil = "Kamu Memasukkan pilihan yang tidak ada";
  }

  alert("Kamu memilih : " + p + " dan komputer memilih : " + comp + "\nMaka hasilnya : " + hasil);

  tanya = confirm("Ulangi Lagi? ");
}

alert("Terima Kasih Sudah Bermain");

//
