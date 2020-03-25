var displaySearchResults = function(element){
    $("#searchResultsDiv").html(""); 
    var searchResultDivTerm= $("<br> </br> <p> New Item Created Succesfully:    " + "<a href='" + element + "'>Click Here to View it</a> </p>"
    + "<br> </br>")
    $("#searchResultsDiv").append(searchResultDivTerm)
    $("#title").val(""); 
    $("#description").val(""); 
    $("#Rating").val(""); 
    $("#URL").val(""); 
    $("#stars").val(""); 
    $("#userreview").val(""); 
    $("#title").focus(); 

    
    }

$(document).ready(function(){
    $("#submit_name").click(function(){
        


        if(!(document.getElementById('title').value &&
        document.getElementById('description').value && 
        document.getElementById('Rating').value &&
        document.getElementById('URL').value &&
        document.getElementById('stars').value &&
        document.getElementById('userreview').value)){
            $("#0").remove()
            $("#1").remove()
            $("#2").remove()
            $("#3").remove()
            $("#4").remove()
            $("#5").remove()

            if(!(document.getElementById('title').value)){
                var toappend = "<span class='error text-danger' id = '0'>" + "Please enter some input</span>"; 
                $("#TitleGroup").append(toappend)
            }

            else if(!(document.getElementById('description').value)){
                var toappend = "<span class='error text-danger' id = '1'>" + "Please enter some input</span>"; 
                $("#DescriptionGroup").append(toappend)
            }
            else if(!(document.getElementById('Rating').value)){
                var toappend = "<span class='error text-danger' id = '2'>" + "Please enter some input</span>"; 
                $("#RatingGroup").append(toappend)

            }
            else if(!(document.getElementById('URL').value)){
                var toappend = "<span class='error text-danger' id = '3'>" + "Please enter some input</span>"; 
                $("#URLGroup").append(toappend)
            }
            else if(!(document.getElementById('stars').value)){
                var toappend = "<span class='error text-danger' id = '4'>" + "Please enter some input</span>"; 
                $("#StarsGroup").append(toappend)
            }
            else if(!(document.getElementById('userreview').value)){
                var toappend = "<span class='error text-danger' id = '5'>" + "Please enter some input</span>"; 
                $("#ReviewGroup").append(toappend)
            }
        }


        else {
            $("#0").html("")
            $("#1").html("")
            $("#2").html("")
            $("#3").html("")
            $("#4").html("")
            $("#5").html("")

        var stars = document.getElementById('stars').value;
        var starsList = stars.split(",");    
        
        var newelement = {
            "id": currentid,
            "name": document.getElementById('title').value,
            "description": document.getElementById('description').value,
            "rating": document.getElementById('Rating').value,
            "url": document.getElementById('URL').value,
            "stars": starsList, 
            "user review": document.getElementById('userreview').value,
            "mark_as_deleted": "false", 
            "starsWithMarkedAsDeleted": [{"stars": "Mark Hamill", "mark_as_deleted": "false"}]
            }
            var j; 
             newelement["starsWithMarkedAsDeleted"] = []
             for(j = 0; j < newelement["stars"].length; j++){
             newelement["starsWithMarkedAsDeleted"].push({"stars":newelement["stars"][j], "mark_as_deleted": "false"})
             }
            $.ajax({
                type: "POST",
                url: "creating",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify(newelement),
                success: function(result){
                    currentid++; 
                    var all_data = result; 
                    displaySearchResults(all_data)
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        }
    })



}); 