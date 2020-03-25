var displaySearchResults = function(element){
    $("#Name").html("")
    $("#Description").html("")
    $("#Rating").html("")
    $("#URL").html("")
    $("#stars").html("")
    $("#reviews").html("")
    $("#editLink").html("")
    $("#viewArea").html("")
    $("#viewArea2").html("")
    $("#viewItem").html("")
    $("#last").html("")




   
    var nameAppendEditIcon = "<input type='image' src= '" +"https://cdn3.iconfinder.com/data/icons/user-interface-web-1/550/web-circle-circular-round_58-512.png'" +
    "id = 'nameEditButton' height = '24' width = '24' onclick = 'funonclick()' />"

        var javaScriptToGoTo = " <div class='card' style='width: 18rem;'>" +  
//    "<a href='/view/" + element["id"] + "'  >" + 
 //   "<img src= '" + element["url"] + "' class='card-img-top'>" + "</a>" +
    " <div class='card-body'>" +   
    "<h5 class='card-title' id = 'name-" + "0" + "'>" + element["name"] + nameAppendEditIcon +  
    "</h5>"  + "<p class='card-text' id = 'stars-" + "0" + "'>"
    
    var middle = ""
    
    $.each(element["stars"], function(i,datumm){
    middle = middle + datumm + "<br>" ; 
    })
    
    
    var endOfJavaScriptogoto  = "</p>" + "<p class='card-text whitedOut'>" +  element["description"] + "</p>" + 
      "</div>" + "</div>"; 
    $("#viewArea").append(javaScriptToGoTo + middle + endOfJavaScriptogoto)
        
    var reviewAppendEditIcon = "<input type='image' src= '" +"https://cdn3.iconfinder.com/data/icons/user-interface-web-1/550/web-circle-circular-round_58-512.png'" +
    "id = 'nameEditButton' height = '24' width = '24' onclick = 'funonclick2()' />"; 

    var javaScriptToGoTo2 = " <div class='card' style='width: 18rem;'>" +  
      "<a href='/view/" + element["id"] + "'  >" + 
        "<img alt = 'alternativeText' src= '" + element["url"] + "' class='card-img-top'>" + "</a>" +
        " <div class='card-body'>" +   
         "<p class='card-text' id = 'reviews-" + "0" + "'>" + element["user review"] + reviewAppendEditIcon +"</p>" +"</div>" + "</div>"; 

         

    $("#viewArea2").append(javaScriptToGoTo2)

           
  



    $("#Name").append(element["name"])
    var nameAppendEditIcon = "<input type='image' src= '" +"https://cdn3.iconfinder.com/data/icons/user-interface-web-1/550/web-circle-circular-round_58-512.png'" +
    "id = 'nameEditButton' height = '24' width = '24' onclick = 'funonclick()' />";  
    $("#Name").append(nameAppendEditIcon)
    $("#Description").append(element["description"])
    $("#Rating").append(element["rating"])
    $("#URL").append("<img alt = 'alternativetext' src = '" + element["url"] + "'> </img>")
    var whatToAppendToStars = ""; 
    var i; 
    $("#stars-0").html("");
    for(i = element["starsWithMarkedAsDeleted"].length-1; i > -1; i--){
        if(element["starsWithMarkedAsDeleted"][i]["mark_as_deleted"] == "false"){

        
        var toprepend = $("<div class = 'row'>" + "<div class = 'col-md-6'> "  + element["starsWithMarkedAsDeleted"][i]["stars"] + "</div>" 
        + "<div class = 'col-md-3'> " + "<button type = 'button' class = 'btn btn-primary' id = '" + i + "'>" + "Delete"
         + "</button>" + "</div>" + "</div>"); 


         $("#stars-0").prepend(toprepend); 
         var hashtag = "#"; 
         hashtag+= i.toString(); 
             $(hashtag).on("click", function(){
                var idOfStar = this.id; 
                var id = movieResult["id"]
    
                var infoToSend = 
     
                    {
                   "id": id, 
                   "idOfStar": idOfStar
                   }; 
                $.ajax({
                    type: "POST",
                    url: "/deletestars",                
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data : JSON.stringify(infoToSend),
                    success: function(result){
                    var all_data = result; 
                    movieResult = all_data; 
                    displaySearchResults(movieResult); 
                    },
                    error: function(request, status, error){
                        console.log("Error");
                        console.log(request)
                        console.log(status)
                        console.log(error)
                    }
                });
            });  
        }
        else{
            var toprepend = $("<div class = 'row'>"  
            + "<div class = 'col-md-3'> " + "<button type = 'button' class = 'btn btn-danger' id = '" + i + "'>"
             + "Undo delete" + "</button>" + "</div>" + "</div>"); 
             $("#stars-0").prepend(toprepend); 
             var hashtag = "#"; 
         hashtag+= i.toString(); 
             $(hashtag).on("click", function(){
                var idOfStar = this.id; 
                var id = movieResult["id"]
    
                var infoToSend = 
     
                    {
                   "id": id, 
                   "idOfStar": idOfStar
                   }; 
                $.ajax({
                    type: "POST",
                    url: "/deletestars",                
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data : JSON.stringify(infoToSend),
                    success: function(result){
                    var all_data = result; 
                    movieResult = all_data; 
                    displaySearchResults(movieResult); 
                    },
                    error: function(request, status, error){
                        console.log("Error");
                        console.log(request)
                        console.log(status)
                        console.log(error)
                    }
                });
                // ajay to make mark as deleted false
                // you're going to want to return the array and rerender the page               
            }); 
        }
    }
    


    $("#reviews").append(element["user review"])
    var reviewAppendEditIcon = "<input type='image' src= '" +"https://cdn3.iconfinder.com/data/icons/user-interface-web-1/550/web-circle-circular-round_58-512.png'" +
    "id = 'nameEditButton' height = '24' width = '24' onclick = 'funonclick2()' />"; 
    $("#reviews").append(reviewAppendEditIcon)
    $("#editLink").append("<a href='/edit/" + id + "'>Click Here to Edit Review</a>"); 
    
    
    }
    
    function funonclick() { 
        $("#Name").html("")


     
        var newNameHtml = "<input id = 'newName'></input><br></br><button id='submit_name'>Submit</button><button id='discard_name'>Discard Changes</button>"
        $("#name-0").append(newNameHtml)
        $("#newName").focus(); 
        $("#submit_name").click(function(){
            var nameSubmitted = $("#newName").val()
            var id = movieResult["id"]

            var infoToSend = 
 
                {
               "id": id, 
               "nameSubmitted": nameSubmitted
               }; 
            $.ajax({
                type: "POST",
                url: "/editName",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify(infoToSend),
                success: function(result){
                    var all_data = result; 
                    movieResult = all_data
                    displaySearchResults(movieResult)
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        }); 

        $("#discard_name").click(function(){
            displaySearchResults(movieResult)
        }); 

    } 

    function funonclick2() { 
        $("#reviews").html("")

     
        var newNameHtml = "<input id = 'newName2'></input><br></br><button id='submit_name'>Submit</button><button id='discard_name'>Discard Changes</button>"
        $("#reviews-0").append(newNameHtml)
        $("#newName2").focus()

        $("#submit_name").click(function(){
            var nameSubmitted = $("#newName2").val()
            var id = movieResult["id"]

            var infoToSend = 
 
                {
               "id": id, 
               "review": nameSubmitted
               }; 
            $.ajax({
                type: "POST",
                url: "/addReview",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify(infoToSend),
                success: function(result){
                    var all_data = result; 
                    movieResult = all_data
                    displaySearchResults(movieResult)
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        }); 

        $("#discard_name").click(function(){
            displaySearchResults(movieResult)
        }); 

    } 
    
    $(document).ready(function(){
        displaySearchResults(movieResult) 
        
    
    }); 

    