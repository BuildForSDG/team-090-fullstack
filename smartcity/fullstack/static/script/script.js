var my_latitute = 0;
var my_longitude = 0;
x = document.getElementById('error');
function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else { 
      x.innerHTML = "Geolocation is not supported by this browser.";
    }
  }
  
  
function showPosition(position) {
    my_latitute = position.coords.latitude;
    my_longitude = position.coords.longitude; 
  }
  function showError(error) {
    switch(error.code) {
      case error.PERMISSION_DENIED:
        x.innerHTML = "User denied the request for Geolocation."
        break;
      case error.POSITION_UNAVAILABLE:
        x.innerHTML = "Location information is unavailable."
        break;
      case error.TIMEOUT:
        x.innerHTML = "The request to get user location timed out."
        break;
      case error.UNKNOWN_ERROR:
        x.innerHTML = "An unknown error occurred."
        break;
    }
  }
getLocation();
if(my_latitute == 0 ){
    my_latitute = 11.83537;
    my_longitude = 13.15166;
}
cont = document.getElementById('map');
mapboxgl.accessToken = 'pk.eyJ1IjoiYXJkZXNwIiwiYSI6ImNrYjZsY25pYjBwdXoyeHF2MXJoYzh5Z2YifQ.0l2qyChIYTHzZSTL0umdAg';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center: [my_latitute, my_longitude],
zoom: 13
});
 
map.addControl(
new MapboxGeocoder({
accessToken: mapboxgl.accessToken,
mapboxgl: mapboxgl
})
);

var marker = new mapboxgl.Marker().setLngLat([my_longitude,my_latitute]).addTo(map);
var popup = new mapboxgl.Popup({ closeOnClick: false })
.setLngLat([my_longitude,my_latitute])
.setHTML('User')
.addTo(map);

//Map for service
var map2 = new mapboxgl.Map({
    container: 'servicemap', // container id
    style: 'mapbox://styles/mapbox/streets-v11', // stylesheet location
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9 // starting zoom
    });