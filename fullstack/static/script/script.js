var myLatitude = 0;
var myLongitude = 0;
function showPosition(position) {
  myLatitude = position.coords.latitude;
  myLongitude = position.coords.longitude; 
}
var x = document.getElementById("error");
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
if(myLatitude === 0 ){
    myLatitude = 11.83537;
    myLongitude = 13.15166;
}
mapboxgl.accessToken = "pk.eyJ1IjoiYXJkZXNwIiwiYSI6ImNrYjZsY25pYjBwdXoyeHF2MXJoYzh5Z2YifQ.0l2qyChIYTHzZSTL0umdAg";
var map = new mapboxgl.Map({
container: "map",
style: "mapbox://styles/mapbox/streets-v11",
center: [myLatitude, myLongitude],
zoom: 4
});
 
map.addControl(
new MapboxGeocoder({
accessToken: mapboxgl.accessToken,
mapboxgl: mapboxgl
})
);

var marker = new mapboxgl.Marker().setLngLat([myLongitude,myLatitude]).addTo(map);
//var popup = new mapboxgl.Popup({ closeOnClick: false })
//.setLngLat([myLongitude,myLatitude])
//.setHTML('User')
//.addTo(map);

//Map for service
var map2 = new mapboxgl.Map({
    container: "smap", // container id
    style: "mapbox://styles/mapbox/streets-v11", // stylesheet location
    center: [myLongitude, myLatitude], // starting position [lng, lat]
    zoom: 4 // starting zoom
    });

map2.addControl(
    new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl
    })
);
var marker2 = new mapboxgl.Marker().setLngLat([-74.5,40]).addTo(map2);