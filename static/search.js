var displayResults = function(searchTerm,data){
    //empty old data
    $.ajax({
        type: "POST",
        url: "search_results_link",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(searchTerm),
        success: function(result){
            var all_data = result["searchResults"]
            indices = result["indices"]
            searchResults = all_data
            displaySearchResults()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

    //insert all new data
}
var displaySearchResults = function(){
    $("#searchResultsDiv").empty()
    if (searchResults === undefined || searchResults.length == 0) {
        var numberOfSearchResults = searchResults.length;
        $("#searchResultsDiv").append("<p>" + numberOfSearchResults + "</p>")    }
    else{
        

        var numberOfSearchResults = searchResults.length;
        $("#searchResultsDiv").append("<p>" + numberOfSearchResults + "</p>")
        

$.each(searchResults, function(i,datum){
    
    var javaScriptToGoTo = " <div class='card' style='width: 18rem;'>" +  
"<a href='/view/" + datum["id"] + "'  >" + 
"<img alt = 'alternative text' src= '" + datum["url"] + "' class='card-img-top'>" + "</a>" + 
" <div class='card-body'>" + 
"<h5 class='card-title' id = 'name-" + i + "'>" + datum["name"] + "</h5>"  + "<p class='card-text' id = 'stars-" + i + "'>"

var middle = ""

$.each(datum["stars"], function(i,datumm){
middle = middle + datumm + "<br>" ; 
})


var endOfJavaScriptogoto  = "</p>" 
+  "</div>" + "  </div>"; 
$("#searchResultsDiv").append(javaScriptToGoTo + middle + endOfJavaScriptogoto)
    

   
       
})
   var i;  
for(i = 0; i < indices.length; i++){
    if(indices[i]["type"] == "stars"){
    var hashtag = "stars-"; 
    hashtag+= i.toString(); 
    var elm = document.getElementById(hashtag);
    var html = elm.innerHTML;
    var matchingindex = html.toLowerCase().indexOf(indices[i]["searchTerm"].toLowerCase())
    elm.innerHTML = html.substring(0, matchingindex) + '<span style="background-color: #FFFF00">' + html.substring(matchingindex, matchingindex + indices[i]["lengthOfSubstring"]) + '</span>' + html.substring(matchingindex + indices[i]["lengthOfSubstring"]);
}
    else{
        var hashtag = "name-"; 
        hashtag+= i.toString(); 
        
        var elm = document.getElementById(hashtag);
        var html = elm.innerHTML;

        elm.innerHTML = html.substring(0, indices[i]["index"]) + '<span style="background-color: #FFFF00">' + html.substring(indices[i]["index"], indices[i]["index"] + indices[i]["lengthOfSubstring"]) + '</span>' + html.substring(indices[i]["index"] + indices[i]["lengthOfSubstring"]);
    }
}
    

}
}

function test(elem,array) {

  }

function convertStarsToCode(element){

}




$(document).ready(function(){
    displaySearchResults() 


}); 