$(document).ready(function(){ 
var myLatitude = 0;
var myLongitude = 0;
//get address
var gotten = false;
function getLongitudeLatitude(){
    if(gotten===false){
        var city = $(".fa-city").text();
        $.ajax(
            {
                url: '/ajax/service_address/',
                dataType: "json",
                data:{
                    "city":city,
                },
                success: function(data){
                    myLongitude = data.longitude;
                    myLongitude = data.latitude;
                    gotten = true;
                }
              
            }
        );
    }
}
getLongitudeLatitude();
function showPosition(position) {
  myLatitude = position.coords.latitude;
  myLongitude = position.coords.longitude; 
}
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
mapboxgl.accessToken = "pk.eyJ1IjoiYXJkZXNwIiwiYSI6ImNrYjZsY25pYjBwdXoyeHF2MXJoYzh5Z2YifQ.0l2qyChIYTHzZSTL0umdAg";
var map = new mapboxgl.Map({
container: "map",
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

var marker = new mapboxgl.Marker().setLngLat([myLongitude,myLatitude]).addTo(map);
});