$(document).ready(function(){
  function update_states(data){ 
    // function to update select element with list of state
    $("#state, #id_region").html('');
    for(var i = 0; i < data.regions.length; i++){
        $("#state, #id_region").append('<option id="selected-state" value="'+ data.regions[i]['id'] +'">'+ data.regions[i]['name'] +'</option>');
    }
  }
  // get states for the selected country 
  $("#country, #id_country").change(function(){
      var country = $(this).val();
      $.ajax(
        {
          url:"/ajax/states/",
          data:{
            "country":country,
          },
          dataType: 'json',
          success:function(data){
            $("#state, #id_region").html('');
            for(var i = 0; i < data.regions.length; i++){
              $("#state, #id_region").append('<option id="selected-state" value="'+ data.regions[i]['id'] +'">'+ data.regions[i]['name'] +'</option>');
            }
          }
        }
      );
  });

// get cities for the selected state
$("#state, #id_region").change(function(){
  var state = $(this).val();
  $.ajax(
    {
      url:"/ajax/cities/",
      data:{
        "state":state,
      },
      dataType:"json",
      success:function(data){
        $("#city, #id_city").html("");
        for(var i = 0; i < data.cities.length; i++){
          $("#city, #id_city").append('<option id="selected-city" value="'+ data.cities[i]['id'] +'">'+ data.cities[i]['city'] +'</option>');
        }
      },
      error: function(){
        alert('erro');
      }
    }
  );
});
function myLocation(){
      $.get("https://api.ipdata.co?api-key=test", function(response) {
      $("#mycity").append(response.city);
      $("#myregion").append(response.region);
      $("#mycountry").append(response.country_name);
      //send ajax request
       
        $.ajax(
          {
            url:"/ajax/states/name/",
            data:{
              "country":response.country_name,
              "state":response.region,
              "city":response.city,
            },
            dataType: "json",
            success: function(data){
              $("#country").html("");
              for(var i = 0; i < data.countries.length; i++){
                if(data.countries[i]["name"] === response.country_name){
                  $("#country").append('<option id="selected-country" value="'+ data.countries[i]['id'] +'" disabled selected hidden>'+ data.countries[i]['name'] +'</option>');
                }
                $("#country").append('<option id="selected-country" value="'+ data.countries[i]['id'] +'">'+ data.countries[i]['name'] +'</option>');
              }
              // update state list
              $("#state").html("");
              for(var i = 0; i < data.regions.length; i++){
                if(data.regions[i]["name"] === response.region){
                  $("#state").append('<option id="selected-state" value="'+ data.regions[i]['id'] +'" disabled selected hidden>'+ data.regions[i]['name'] +'</option>');
                }
                $("#state").append('<option id="selected-state" value="'+ data.regions[i]['id'] +'">'+ data.regions[i]['name'] +'</option>');
              }
              //update city list
              $("#city").html("");
              for(var i = 0; i < data.cities.length; i++){
                if(data.cities[i]["city"] === response.city){
                  $("#city").append('<option id="selected-city" value="'+ data.cities[i]['id'] +'" disabled selected hidden>'+ data.cities[i]['city'] +'</option>');
                }
                $("#city").append('<option id="selected-city" value="'+ data.cities[i]['id'] +'">'+ data.cities[i]['city'] +'</option>');
              }
            }, 
          }
        );

      var country = $("#mycountry").text();
      var errorPanel = $("#error-panel");
      /*if(country === ''){
        $("#error-panel").append("Select country");
      }
      else{
        $("#error-panel").append("Select manually");
      }
      */

    }, "jsonp");
  }
 myLocation();
  var myLatitude = 0;
  var myLongitude = 0;
  function showPosition(position) {
    myLatitude = position.coords.latitude;
    myLongitude = position.coords.longitude; 
  }
  //var x = document.getElementById("error");
  var x = $("#error");
  function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
      } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
      }
    }
    
    function showError(error) {
      switch(error.code) {
        case error.PERMISSION_DENIED:
          x.innerHTML = "User denied the request for Geolocation.";
          break;
        case error.POSITION_UNAVAILABLE:
          x.innerHTML = "Location information is unavailable.";
          break;
        case error.TIMEOUT:
          x.innerHTML = "The request to get user location timed out.";
          break;
        case error.UNKNOWN_ERROR:
          x.innerHTML = "An unknown error occurred.";
          break;
      default:
          x.innerHTML = " ";
      }
    }
  getLocation();
  /*
  if(myLatitude === 0 ){
      myLatitude = 11.83537;
      myLongitude = 13.15166;
  }
  */
  /*mapboxgl.accessToken = "pk.eyJ1IjoiYXJkZXNwIiwiYSI6ImNrYjZsY25pYjBwdXoyeHF2MXJoYzh5Z2YifQ.0l2qyChIYTHzZSTL0umdAg";
  var map = new mapboxgl.Map({
  container: "smap",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [myLongitude, myLatitude],
  zoom: 4
  });
   
  map.addControl(
  new MapboxGeocoder({
  accessToken: mapboxgl.accessToken,
  mapboxgl: mapboxgl
  })
  );

  var marker = new mapboxgl.Marker().setLngLat([10,8]).addTo(map);

  //Map for service
  var map2 = new mapboxgl.Map({
      container: "smap", // container id
      style: "mapbox://styles/mapbox/streets-v11", // stylesheet location
      center: [8, 10], // starting position [lng, lat]
      zoom: 4 // starting zoom
      });

  map2.addControl(
      new MapboxGeocoder({
      accessToken: mapboxgl.accessToken,
      mapboxgl: mapboxgl
      })
  );
  var marker2 = new mapboxgl.Marker().setLngLat([8, 10]).addTo(map2);
  */

});