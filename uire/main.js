
// 1. Model pencarian/searching yang diinginkan berbentuk kategori
if (centroid[0] == 'A'){
  // Toxonomy
	
  document.getElementById("taxon").hidden = false;
} else if(centroid[0] == 'B'){
  // Keyword

} else if(centroid[0] == 'C'){
  // Image
}

// 2. Adanya fasilitas Spellcheck
if (centroid[1] == 'Y'){
  document.getElementById("spellcheck").hidden = false;
  document.getElementById("input_search").value = "compter";  
} else if(centroid[1] == 'T'){
  document.getElementById("spellcheck").hidden = true;
} 

// 3. Adanya rekomendasi buku yang relevan
if (centroid[2] == 'Y'){

} else if(centroid[2] == 'T'){
	document.getElementById("rekomendasi1").hidden = true;	
} 

// 4. Adanya hasil pencarian yang diranking berdasarkan relevansinya dengan kebutuhan
if (centroid[3] == 'Y'){
	document.getElementById("based").hidden = false;
	document.getElementById("relevan").hidden = false;	
} else if(centroid[3] == 'T'){

} 


// 5. Navigasi penelusuran pencarian/searching yang dinginkan berbentuk
if (centroid[4] == 'L'){
  // Link
  
  document.getElementById("im_1").hidden = true;
  document.getElementById("im_2").hidden = true;
  document.getElementById("im_3").hidden = true;
  document.getElementById("im_rekom").hidden = true;
  
} else if(centroid[4] == 'I'){
  // Icon
} 

// 6. Icon navigasi yang diinginkan berbentuk 
if (centroid[5] == 'C'){
  // Gambar
  document.getElementById("search_icon").hidden = false;

} else if(centroid[5] == 'T'){
  // Teks
  document.getElementById("search_text").hidden = false;
} 

// 7. Ukuran icon navigasi yang diinginkan 
if (centroid[6] == 'K'){
  // Kecil

} else if(centroid[6] == 'G'){
  // Besar
  document.getElementById("search_icon").width = "40";
  document.getElementById("search_icon").height = "40";
  document.getElementById("search_icon").style.padding = "20px 0 0 0";

  document.getElementById("search_text").style.cssText = "border-style:solid; padding:3px; font-size: 18px;";
} 

// 8. Adanya batasan bentuk/tipe  huruf  dalam disain antarmuka OPAC.        
if (centroid[7] == 'Y'){

} else if(centroid[7] == 'T'){
   document.getElementById("subtitle_1").style.cssText = "font-family: arial";	
   document.getElementById("subtitle_2").style.cssText = "font-family: arial";	
   document.getElementById("subtitle_3").style.cssText = "font-family: arial";	

} 


// 9. Adanya batasan ukuran/size huruf dalam disain antarmuka OPAC
if (centroid[8] == 'Y'){

} else if(centroid[8] == 'T'){
   document.getElementById("title_1").style.cssText = "font-size: 18px;";
   document.getElementById("title_2").style.cssText = "font-size: 18px;";
   document.getElementById("title_3").style.cssText = "font-size: 18px;";
} 

// 10. Adanya batasan jumlah warna dalam disain antarmuka OPAC         
if (centroid[9] == 'Y'){
	document.getElementById("spellcheck").style.cssText = "padding-left:5px; color:blue;"
} else if(centroid[9] == 'T'){

} 

// 11. Warna disain antarmuka  yang diinginkan :
if (centroid[10] == 'WL'){
  // lembut

} else if(centroid[10] == 'WM'){
  // mencolok
	document.getElementById("spellcheck").style.cssText = "padding-left:5px; color:red;"

} 


// 12. Adanya batasan jumlah warna  background dalam disain antarmuka OPAC  
if (centroid[11] == 'Y'){

} else if(centroid[11] == 'T'){
	document.getElementById("bg1").style.cssText = "background-color:white;"
	document.getElementById("bg2").style.cssText = "background-color:white;"
	document.getElementById("bg3").style.cssText = "background-color:white;"
} 

document.getElementById("secondbox").style.cssText = "padding:10px";
// 13. Warna background antarmuka yang diinginkan 
if (centroid[12] == 'WL'){
  // lembut
  document.getElementById("mybox").style.cssText = "background-color: #F0F8FF;";
} else if(centroid[12] == 'WM'){
  // mencolok
  document.getElementById("mybox").style.cssText = "background-color: blue;";
} 

// 14. Desain antarmuka pencarian/searching dengan bentuk sederhana  (Y/T)
if (centroid[13] == 'Y'){
  document.getElementById("not_simple").hidden = true
} else if(centroid[13] == 'T'){

} 

// 15. Hasil pencarian/searching  yang diinginkan Menampilkan:
if (centroid[14] == 'P'){
  // semua informasi obyek
  document.getElementById("lengkap_1").hidden = false
  document.getElementById("lengkap_2").hidden = false
  document.getElementById("lengkap_3").hidden = false

} else if(centroid[14] == 'Q'){
  // informasi hanya obyek yang diminta

} else if(centroid[14] == 'R'){
  // informasi dengan menambahkan referensi sumber lain yang relevan
	document.getElementById("rekomendasi1").hidden = false;	

} else if(centroid[14] == 'S'){
  // Menampilkan Informasi diurutkan berdasarkan popularitas
	document.getElementById("based").hidden = false;
	document.getElementById("popular").hidden = false;

}
	</script>
</window>

