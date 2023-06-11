

function select_record(record)
{ 
    document.getElementById("id0").value  = record[0];
    document.getElementById("id1").value  = record[1];
    document.getElementById("id2").value  = record[2];
    document.getElementById("id3").value  = record[3];
    document.getElementById("id4").value  = record[4];
    document.getElementById("id5").value  = record[5];
    document.getElementById("id6").value  = record[6];
    document.getElementById("id7").value  = record[7];
    document.getElementById("id8").value  = record[8];
    document.getElementById("id9").value  = record[9];
    document.getElementById("id10").value  = record[10];
    document.getElementById("id11").value  = record[11];
    document.getElementById("id12").value  = record[12];
    document.getElementById("id13").value  = record[13];
    document.getElementById("id14").value  = record[14];
    document.getElementById("id15").value  = record[15];
    document.getElementById("id16").value  = record[16];
    document.getElementById("id17").value  = record[17];
    document.getElementById("id18").value  = record[18];
    document.getElementById("id19").value  = record[19];
    document.getElementById("id20").value  = record[20];
    alert("Bạn đã chọn dữ liệu - Xem dữ liệu ở các trường dữ liệu");
 
   
  }

  function mouseoverRecord(element)
  {
  var cellcolor = element.style.backgroundColor;
  if(!(cellcolor == 'red')){
      element.style.backgroundColor = "red"; 
  }
  else{
      element.style.backgroundColor= "";
  }
  }


  function mouseoutRecord(element)
  {
  var cellcolor = element.style.backgroundColor;
  if(!(cellcolor == 'red')){
      element.style.backgroundColor = "white"; 
  }
  else{
      element.style.backgroundColor= "";
  }
  }


  function clearContentField()
  {
    document.getElementById("id0").value  = '';
    document.getElementById("id1").value  = '';
    document.getElementById("id2").value  = '';
    document.getElementById("id3").value  = '';
    document.getElementById("id4").value  = '';
    document.getElementById("id5").value  = '';
    document.getElementById("id6").value  = '';
    document.getElementById("id7").value  = '';
    document.getElementById("id8").value  = '';
    document.getElementById("id9").value  = '';
    document.getElementById("id10").value  = '';
    document.getElementById("id11").value  = '';
    document.getElementById("id12").value  = '';
    document.getElementById("id13").value  = '';
    document.getElementById("id14").value  = '';
    document.getElementById("id15").value  = '';
    document.getElementById("id16").value  = '';
    document.getElementById("id17").value  = '';
    document.getElementById("id18").value  = '';
    document.getElementById("id19").value  = '';
    document.getElementById("id20").value  = '';
    

  }






