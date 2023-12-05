const map = L.map("map", {
    minZoom: -2 ,
    crs: L.CRS.Simple,
    maxBounds: [
    [0, 0],
    [5144, 7260]
    ]
});



var bounds = [[0,0], [5144,7260]];



var MarkerIcon = L.Icon.extend({
    options:{
        iconSize:     [38, 65],
        shadowSize:   [50, 64],
        iconAnchor:   [22, 94],
        shadowAnchor: [4, 62],
        popupAnchor:  [-3, -100]   
    } 
});



var image = L.imageOverlay('/static/san_joaquin_v2.webp', bounds).addTo(map);
map.fitBounds(bounds);



var iconMapping = {
    'vidrio': new MarkerIcon({ iconUrl: '/static/images/marker_icon_green.png' }),
    'normal': new MarkerIcon({ iconUrl: '/static/images/marker_icon_red.png' }),
    'papel': new MarkerIcon({ iconUrl: '/static/images/marker_icon_blue.png' }),
    'plastico': new MarkerIcon({ iconUrl: '/static/images/marker_icon_yellow.png' }),
    'latas': new MarkerIcon({ iconUrl: '/static/images/marker_icon_black.png' })
};
    


var layerGroups = {};
for (var type in iconMapping) {
    layerGroups[type] = L.layerGroup().addTo(map);
}



var layerControl = L.control.layers(null, layerGroups).addTo(map);



//popup para solicitar marcadores
var popup = L.popup();

function onMapClick(e) {
    var container = document.createElement('div');
    container.innerHTML = "Deseas solicitar un marcador en " + e.latlng.toString() + '?'+
        '<br><br>Elegir tipo de marcador: ' +
        '<select id="markerType">' +
        '   <option value="normal">Normal</option>' +
        '   <option value="papel">Papel y cartón</option>' +
        '   <option value="vidrio">Vidrio</option>' +
        '   <option value="plastico">Botellas plásticas</option>' +
        '   <option value="latas">Latas</option>' +
        '</select>' +
        '<br><br>' +
        '<button id="confirmButton">Solicitar</button>';

    container.querySelector('#confirmButton').addEventListener('click', function() {
        var marker_type = container.querySelector('#markerType').value;
        var latlng = e.latlng;
        sendDataToServer(latlng, marker_type);
        alert('Tipo de marcador: ' + marker_type + '\nCoordenadas: ' + e.latlng.toString()) + '\n¡Tu solicitud se ha enviado con éxito!';
        map.closePopup();
    });
    popup
        .setLatLng(e.latlng)
        .setContent(container)
        .openOn(map);
}


map.on('click', onMapClick);



//se explica solito
function sendDataToServer(latlng, marker_type) {
    fetch('/save_request/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mapa:'mapa6',
            x_coordinate: latlng.lat,
            y_coordinate: latlng.lng,
            tipo: marker_type
         }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



for (var i = 0; i < markersData.length; i++) {
    var markerData = markersData[i];
    var markerType = markerData.fields.tipo;
    var icono = iconMapping[markerType]
    var marker = L.marker([markerData.fields.x_coordinate, markerData.fields.y_coordinate], { icon: icono });
    layerGroups[markerType].addLayer(marker);
    marker.bindPopup('<strong>' + markerType + '</strong><br/>');
}

//const vidrio1 = L.marker([3670, 4385], {icon: marcador_vidrio}).bindPopup("vidrio")