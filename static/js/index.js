window.onload = function(){
	console.log(555);
	var name = $('#name')[0];
	var mood = $('.mood');
	var bigEvent = $('#bigEvent')[0];
	var speak = $('#speak')[0];
	var d1 = $('#d1')[0];
	var d2 = $('#d2')[0];
	var d3 = $('#d3')[0];
	var d4 = $('#d4')[0];
	var d5 = $('#d5')[0];
	var sub1 = $('#sub1')[0];
	var sub2 = $('#sub2')[0];
	var sub3 = $('#sub3')[0];
	var sub4 = $('#sub4')[0];
	var chatDiv = $('#chatDiv')[0];
	var x = 'x';
	var gen = $('#gen')[0];
	var kechen = $('#kechen')[0];
	var keci = $('#keci')[0];
	var content = $('#content')[0];
	var banji = $('#banji')[0];
	var xueyuan = $('#xueyuan')[0];
	var biaoxian = $('#biaoxian')[0];
	sub1.onclick = function(){
		for(var i=0;i<mood.length;i++){
			if(mood[i].checked){
				x=i;
			}
		}
		$.get('/mood?name='+name.value+'&mood='+x,function(result){
			alert(result);
		});
	};
	sub2.onclick = function(){
		$.get('/week?name='+name.value+'&week='+bigEvent.value,function(result){
			alert(result);
		});
	};
	sub3.onclick = function(){
		$.get('/chat?name='+name.value+'&chat='+speak.value,function(result){
			alert(result);
			speak.value = '';
		});
	};
	sub4.onclick = function(){
		console.log(123);
		var data = {'name':name.value,'d1':d1.value,'d2':d2.value,'d3':d3.value,'d4':d4.value,'d5':d5.value};
		$.post('/know',data,function(result){
			alert(result);
		});
	};
	setInterval(function(){
		$.get('/showmsg',function(result){
			chatDiv.innerHTML = result;
		});
	},1000);
	gen.onclick = function(){
		var data = {'kechen':kechen.value,'keci':keci.value,'content':content.value,'banji':banji.value,'xueyuan':xueyuan.value,'biaoxian':biaoxian.value};
		$.post('/report',data,function(result){
			alert(result);
		});
	};
};
