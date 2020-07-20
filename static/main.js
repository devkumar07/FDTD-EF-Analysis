function createCards(data){
  $("#totalcases").html('<b>Total Cases: </b>'+ data.latest.confirmed);
  $("#totaldeaths").html('<b>Total Death: </b>'+ data.latest.deaths);
}


$(document).ready(function(){
    $.get("/",'index.html')
    $(document).ready(function () {
        $('#cases').DataTable({
          "ajax": {
          "url": "/globalcases",
          "dataType": "json",
          "dataSrc": "locations",
          "contentType":"application/json"
          },
          "columns": [
            {'data': 'country'},
            {'data': 'latest.confirmed'},
            {'data': 'latest.deaths'},
            {'data': 'last_updated'}
          ],
          "order": [[ 1, "desc" ]]
        });
    });
    $('#news').DataTable({
        "ajax": {
        "url": "/news", 
        "dataType": "json",
        "dataSrc": "articles",
        "contentType":"application/json"
        },
        "columns": [
            {'data': 'title'},
            {'data': 'description'},
            {'data': 'source.name'}
        ]
      });
      $.get("/init",{},function(response){
        var data = JSON.parse(response);
        createCards(data);
    });
});