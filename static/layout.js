$(document).ready(function(){
    document.getElementById("ButtonToClick").onclick = function () {
        var searchitem = $("#item").val() + ""; 
        var link = "/search/" + searchitem; 
        location.href = link;
    };

}); 

function funonclick() { 
    location.href = "/";

}