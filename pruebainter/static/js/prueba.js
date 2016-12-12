$(document).ready(function(){
	var u = gettext("Alerta")
	alert(u)

	$("#enviar").click(function(){
		console.log($('input:radio[name=gender]:checked').val());
	});
	//console.log()
});