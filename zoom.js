// Change this array to test.

// var points = [
//     { lat: 50.170603, lng: -114.577065 },
//     { lat: 35.144478, lng: -115.33516959999997 }
// ];

// var $mapDiv = $('#mapDiv');

// var mapDim = {
//     height: $mapDiv.height(),
//     width: $mapDiv.width()
// }

function calculateZoom(points, mapDim, $mapDiv) {

    function getBoundsZoomLevel(bounds, mapDim) {
        var WORLD_DIM = { height: 256, width: 256 };
        var ZOOM_MAX = 21;

        function latRad(lat) {
            var sin = Math.sin(lat * Math.PI / 180);
            var radX2 = Math.log((1 + sin) / (1 - sin)) / 2;
            return Math.max(Math.min(radX2, Math.PI), -Math.PI) / 2;
        }

        function zoom(mapPx, worldPx, fraction) {
            return Math.floor(Math.log(mapPx / worldPx / fraction) / Math.LN2);
        }

        var ne = bounds.getNorthEast();
        var sw = bounds.getSouthWest();

        var latFraction = (latRad(ne.lat()) - latRad(sw.lat())) / Math.PI;

        var lngDiff = ne.lng() - sw.lng();
        var lngFraction = ((lngDiff < 0) ? (lngDiff + 360) : lngDiff) / 360;

        var latZoom = zoom(mapDim.height, WORLD_DIM.height, latFraction);
        var lngZoom = zoom(mapDim.width, WORLD_DIM.width, lngFraction);

        return Math.min(latZoom, lngZoom, ZOOM_MAX);
    }

    function createMarkerForPoint(point) {
        return new google.maps.Marker({
            position: new google.maps.LatLng(point.lat, point.lng)
        });
    }

    function createBoundsForMarkers(markers) {
        var bounds = new google.maps.LatLngBounds();
        $.each(markers, function () {
            bounds.extend(this.getPosition());
        });
        return bounds;
    }

    var markers = [];
    $.each(points, function () { markers.push(createMarkerForPoint(this)); });

    var bounds = (markers.length > 0) ? createBoundsForMarkers(markers) : null;

    return (bounds) ? getBoundsZoomLevel(bounds, mapDim) : 0

    $.each(markers, function () { this.setMap(map); });
}