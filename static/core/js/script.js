 /*

	autor: Lário Diniz
	descrição: Filtra a listadefilmes
	
 */
window.onload = function(){
	var form = document.getElementById("ordenar");
	form.onchange=function(){
		if(form.selectedIndex==1){sortUnorderedList("ul");}
		else{sortUnorderedList("ul", true);}
	
	
	}
}
function sortUnorderedList(ul, sortDescending) {
  if(typeof ul == "string")
    ul = document.getElementsByTagName(ul)[0];

  // Idiot-proof, remove if you want
  if(!ul) {
    alert("The UL object is null!");
    return;
  }

  // Get the list items and setup an array for sorting
  var lis = ul.getElementsByTagName("LI");
  var vals = [];

  // Populate the array
  for(var i = 0, l = lis.length; i < l; i++)
    vals.push(lis[i].innerHTML);

  // Sort it
  vals.sort();

  // Sometimes you gotta DESC
  if(sortDescending)
    vals.reverse();

  // Change the list on the page
  for(var i = 0, l = lis.length; i < l; i++)
    lis[i].innerHTML = vals[i];
}