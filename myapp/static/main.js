

const map = L.map("map", {
    minZoom: -2 ,
    crs: L.CRS.Simple,
    maxBounds: [
    [0, 0],
    [5144, 7260]
    ]
});
//límites de la imágen(resolución en pixeles, alto x ancho)
//formato "y,x" para todo en leaflet
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

var marcador_vidrio = new MarkerIcon({ iconUrl: '/static/images/marker_icon_green.png' }), 
    marcador_normal = new MarkerIcon({iconUrl: '/static/images/marker_icon_red.png'}),
    marcador_papel = new MarkerIcon({iconUrl: '/static/images/marker_icon_blue.png'}),
    marcador_plastico = new MarkerIcon({iconUrl: '/static/images/marker_icon_yellow.png'}),
    marcador_latas = new MarkerIcon({iconUrl: '/static/images/marker_icon_black.png'});
    


    const vidrio1 = L.marker([3670, 4385], {icon: marcador_vidrio}).bindPopup("vidrio")
    const normal1 = L.marker([3670, 4360], {icon: marcador_normal}).bindPopup("normal")
    const papel1 = L.marker([3670, 4335], {icon: marcador_papel}).bindPopup("papel y cartón")
    const lata1 = L.marker([3670, 4310], {icon: marcador_latas}).bindPopup("latas")
    const plastico1 = L.marker([3670, 4285], {icon: marcador_plastico}).bindPopup("plásticos")



var all_markers=[vidrio1, normal1, papel1, lata1, plastico1];



var vidrios = L.layerGroup([vidrio1]);
var normales = L.layerGroup([normal1]);
var papeles = L.layerGroup([papel1]);
var latas = L.layerGroup([lata1]);
var plasticos = L.layerGroup([plastico1]);



//para el filtro
var filtro = {
    "Normal": normales,
    "Papel y cartón": papeles,
    "Vidrio": vidrios,
    "Botellas plásticas": plasticos,
    "Latas": latas
}


var layerControl = L.control.layers(null, filtro).addTo(map);


//popup para solicitar marcadores
var popup = L.popup();

function onMapClick(e) {
    var container = document.createElement('div');
    container.innerHTML = "Deseas solicitar un marcador en " + e.latlng.toString() + '?'+
        '<br><br>Elegir tipo de marcador: ' +
        '<select id="markerType">' +
        '   <option value="normal">Normal</option>' +
        '   <option value="Papel y cartón">Papel y cartón</option>' +
        '   <option value="Vidrio">Vidrio</option>' +
        '   <option value="Botellas plásticas">Botellas plásticas</option>' +
        '   <option value="Latas">Latas</option>' +
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
            mapa:'1',
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
