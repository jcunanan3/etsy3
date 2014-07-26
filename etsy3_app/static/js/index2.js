/**
 * Created by joaquincunanan on 7/25/14.
 */
var map;
function initialize() {
    var mapOptions = {
        zoom: 16,
        center: new google.maps.LatLng(37.7833, 122.4167)
    };
    map = new google.maps.Map(document.getElementById('map-canvas'),
         mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);

