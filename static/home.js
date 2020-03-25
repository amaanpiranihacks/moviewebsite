

var displaySearchResults = function(element){
    $("#bootstrapCards").html("")
    var i = 0;
    var indexAt = movieResults.length-1; 
    // make sure it doesn't go out of ounds
while(i < 10 && indexAt > -1){

    if(true){
    var javaScriptToGoTo = " <div class='card' style='width: 18rem;'>" + 
"<a href='/view/" + movieResults[indexAt]["id"] + "'  >" + 
    "<img alt = 'alternativetext' src= '" + movieResults[indexAt]["url"] + "' class='card-img-top'>" + "</a>" + 
    " <div class='card-body'>" + 
    "<h5 class='card-title'>" + movieResults[indexAt]["name"] + "</h5>"  + 
    "  </div>" + "  </div>"
    $("#bootstrapCards").append(javaScriptToGoTo)
    i++; 
    indexAt--;
    }
    else{
        indexAt--; 
    }



}
    
    
    }

$(document).ready(function(){
    displaySearchResults(movieResults) 
   

}); 