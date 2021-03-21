var AllStudentsUrl = 'http://127.0.0.1:5000/Students';
var InsertNewStudentUrl= 'http://127.0.0.1:5000/insertStudent';
console.log("This is js test");
var $x=AllStudentsUrl;
var $y=InsertNewStudentUrl;
$.ajax({
url:$x,
type:'GET',
success:function(data){
   var table=''
   console.log(data);
 $.each(data,function(i,d){
  
    table+='<tr data-id="'+d.StudentID+'">'+
    '<td>'+d.StudentID+'</td>'+
    '<td>'+d.StudentName+'</td>'+
    
    '<td>'+d.StudentMobileNo+'</td>'+
   
    '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td></tr>';


    
 });
 $("table").find("tbody").empty().html(table);
 

 
}



});
var logindata={'StudentID':'3','Password':'123','StudentName':'xyz','StudentMobileNo':'6321'};
$("#loginbutton").on("click",function(){
  $.ajax({
    url:$y,
    type:'POST',
    data:{'StudentID':'3','Password':'123','StudentName':'xyz','StudentMobileNo':'6321'},
    success:function(respose){
       console.log(respose);
    }
  });
});
