const map = L.map("map", {
    minZoom: -2.5 ,
    maxZoom: 4,
    crs: L.CRS.Simple,
    maxBounds: [
    [0, 0],
    [5144, 7260]
    ]
});

var image = L.imageOverlay(mapa_link, bounds).addTo(map);

var MarkerIcon = L.Icon.extend({
    options:{
        iconSize:     [38, 40],
        shadowSize:   [50, 64],
        iconAnchor:   [22, 70],
        shadowAnchor: [4, 62],
        popupAnchor:  [-3, -100]   
    } 
});

map.fitBounds(bounds);

var iconMapping = {
    'vidrio': new MarkerIcon({ iconUrl: '/static/marker_icon_green.png' }),
    'normal': new MarkerIcon({ iconUrl: '/static/marker_icon_red.png' }),
    'papel': new MarkerIcon({ iconUrl: '/static/marker_icon_blue.png' }),
    'plastico': new MarkerIcon({ iconUrl: '/static/marker_icon_yellow.png' }),
    'latas': new MarkerIcon({ iconUrl: '/static/marker_icon_black.png' })
};
    
var layerGroups = {};
for (var type in iconMapping) {
    layerGroups[type] = L.layerGroup().addTo(map);
}

var layerControl = L.control.layers(null, layerGroups).addTo(map);

//popup para solicitar marcadores
var popup = L.popup({
    minWidth: 280, // Cambia el ancho mínimo del popup
    maxHeight: 150, // Cambia la altura máxima del popup
});

function onMapClick(e) {
    var container = document.createElement('div');
    var a = e.latlng.lat;
    var b = e.latlng.lng;

    container.style.lineHeight= "0.4"
    container.style.display = 'flex'; // Usar flexbox para distribuir el contenido
    container.style.flexDirection = 'column'; // Alinear elementos en columna
    container.style.justifyContent = 'space-between'; // Espacio uniforme entre los elementos
    container.style.textAlign="center"

    var title = document.createElement('h3');
    title.textContent = 'Agregar marcador en:';
    container.appendChild(title);

    var coordinates = document.createElement('p');
    coordinates.textContent = `${a.toFixed().toString()}, ${b.toFixed().toString()}`;
    container.appendChild(coordinates);

    var select = document.createElement('select');
    select.className = 'marker-select'; // Agregar clase al select
    select.id = 'markerType';
    select.innerHTML = `
        <option value="normal">Normal</option>
        <option value="papel">Papel y cartón</option>
        <option value="vidrio">Vidrio</option>
        <option value="plastico">Botellas plásticas</option>
        <option value="latas">Latas</option>
    `;
    container.appendChild(select);

    var button = document.createElement('button');
    button.className = 'confirm-button'; // Agregar clase al botón
    button.id = 'confirmButton';
    button.textContent = 'Solicitar';
    button.addEventListener('click', function() {
        var marker_type = container.querySelector('#markerType').value;
        var latlng = e.latlng;
        sendDataToServer(latlng, marker_type);
        
        alert('Tipo de marcador: ' + marker_type + '\nCoordenadas: ' + a.toFixed() + ', ' + b.toFixed() + '\n¡Tu solicitud se ha enviado con éxito!');
        map.closePopup();
        location.reload();
    });
    container.appendChild(button);

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
            mapa: mapa_id,
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



var markers = []



//Para cargar desde la base de datos apenas cargue la imagen
for (var i = 0; i < markersData.length; i++) {
    var markerData = markersData[i];
    var markerType = markerData.fields.tipo;
    var icono = iconMapping[markerType]
    var marker = L.marker([markerData.fields.x_coordinate, markerData.fields.y_coordinate], {
        icon: icono,
        draggable: true
     });
    layerGroups[markerType].addLayer(marker);
    var popupContent = `
        <div class="custom-popup-content">
            <strong>${markerType}</strong><br/>
            <button class="delete-marker-btn" onclick="handleButtonClick('${markerData.pk}')">Eliminar Marcador</button>
        </div>
    `;
    marker.bindPopup(popupContent);
    markers.push(marker);
}




