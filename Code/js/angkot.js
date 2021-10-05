var penumpang = [];
var tambahPenumpang = function (namaPenumpang, penumpang) {
  if (penumpang.length == 0) {
    penumpang.push(namaPenumpang);
    return penumpang;
  } else {
    for (var a = 0; a < penumpang.length; a++) {
      if (penumpang[a] == undefined) {
        penumpang[a] = namaPenumpang;
        return penumpang;
      } else if (penumpang[a] == namaPenumpang) {
        console.log(namaPenumpang) + "sudah ada di dalam angkot";
        return penumpang;
      } else if (a == penumpang.length - 1) {
        penumpang.push(namaPenumpang);
        return penumpang;
      }
    }
  }
};
var hapusPenumpang = function (namaPenumpang, penumpang) {
  if (penumpang.length == 0) {
    console.log("Angkot masih kosong!");
  } else {
    for (var a = 0; a < penumpang.length; a++) {
      if (penumpang[a] == namaPenumpang) {
        penumpang[a] = undefined;
        return penumpang;
      } else if (a == penumpang.length - 1) {
        console.log(namaPenumpang + "penumpang tersebut tidak ada di dalam angkot");
        return penumpang;
      }
    }
  }
  return penumpang;
};
