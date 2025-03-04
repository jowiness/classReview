window.onload = function(){
	var gen = $('#gen')[0];
	var kechen = $('#kechen')[0];
	var keci = $('#keci')[0];
	var content = $('#content')[0];
	var zsd = $('#zsd')[0];
	var banji = $('#banji')[0];
	var num = $('#num')[0];
	var xueyuan = $('#xueyuan')[0];
	var biaoxian = $('#biaoxian')[0];
	gen.onclick = function(){
		var data = {'kechen':kechen.value,'keci':keci.value,'content':content.value,'zsd':zsd.value,'banji':banji.value,'num':num.value,'xueyuan':xueyuan.value,'biaoxian':biaoxian.value};
		$.post('/report',data,function(result){
			alert(result);
		});
	};
};
