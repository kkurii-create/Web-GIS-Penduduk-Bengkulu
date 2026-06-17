import folium

m = folium.Map(
    location=[-3.83, 102.33],  # Bengkulu
    width="80%",
    height="500px",
    left="10%",
    top="5%",
    zoom_start=12,
    min_zoom=5,
    max_zoom=20,
    control_scale=True,
    prefer_canvas=True,
    zoom_control=True
)

# World Imagery
folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Tiles © Esri',
    name='World Imagery'
).add_to(m)

# Topography Map
folium.TileLayer(
    tiles='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
    attr='Map data © OpenStreetMap contributors',
    name='Topography Map'
).add_to(m)

m.save('mapbengkulu.html')

import folium
from branca.element import Template, MacroElement

# ==========================================
# PETA DASAR
# ==========================================
m = folium.Map(
    location=[-3.83, 102.33],
    zoom_start=8,
    control_scale=True
)

# ==========================================
# BASEMAP
# ==========================================

folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Tiles © Esri',
    name='World Imagery'
).add_to(m)

folium.TileLayer(
    tiles='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
    attr='OpenTopoMap',
    name='Topography Map'
).add_to(m)

# ==========================================
# DATA KABUPATEN/KOTA
# ==========================================

data_bengkulu = [
    ["Bengkulu Selatan", -4.43, 102.90, 155427],
    ["Rejang Lebong", -3.47, 102.53, 258763],
    ["Bengkulu Utara", -3.30, 102.20, 298757],
    ["Kaur", -4.78, 103.37, 118586],
    ["Seluma", -4.03, 102.53, 189874],
    ["Mukomuko", -2.57, 101.12, 185499],
    ["Lebong", -3.20, 102.40, 133042],
    ["Kepahiang", -3.65, 102.58, 134938],
    ["Bengkulu Tengah", -3.74, 102.26, 111318],
    ["Kota Bengkulu", -3.80, 102.27, 368065]
]

# ==========================================
# MARKER DAN POPUP
# ==========================================

for wilayah, lat, lon, penduduk in data_bengkulu:

    popup_text = f"""
    <b>{wilayah}</b><br>
    Jumlah Penduduk : {penduduk:,} Jiwa
    """

    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=wilayah,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# ==========================================
# LEGENDA
# ==========================================

template = """
{% macro html(this, kwargs) %}

<div style="
position: fixed;
bottom: 50px;
right: 50px;
width: 200px;
height: 90px;
background-color: white;
border:2px solid grey;
z-index:9999;
font-size:14px;
padding:10px;
">

<b>Keterangan</b>
<hr>

<span style="color:red;">●</span>
Kabupaten atau Kota

</div>

{% endmacro %}
"""

macro = MacroElement()
macro._template = Template(template)
m.get_root().add_child(macro)

# ==========================================
# KONTROL LAYER
# ==========================================

folium.LayerControl(collapsed=False).add_to(m)

# ==========================================
# SIMPAN
# ==========================================

m.save("mapbengkulu.html")

# ==========================================
# JUDUL PETA
# ==========================================

title_html = '''
<div style="
position: fixed;
top: 10px;
left: 50%;
transform: translateX(-50%);
z-index:9999;
background-color: white;
padding: 10px 20px;
border-radius: 10px;
box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
font-size: 20px;
font-weight: bold;
">

WEBGIS SEBARAN PENDUDUK PROVINSI BENGKULU TAHUN 2017

</div>
'''

m.get_root().html.add_child(
    folium.Element(title_html)
)

# ==========================================
# FOOTER
# ==========================================

footer_html = '''
<div style="
position: fixed;
bottom: 10px;
left: 10px;
z-index:9999;
background-color: white;
padding: 8px;
border-radius: 5px;
font-size: 12px;
box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
">

Sumber Data : BPS Provinsi Bengkulu (2017)

</div>
'''

m.get_root().html.add_child(
    folium.Element(footer_html)
)

# ==========================================
# IDENTITAS PEMBUAT
# ==========================================

creator_html = '''
<div style="
position: fixed;
bottom: 10px;
right: 270px;
z-index:9999;
background-color: white;
padding: 8px;
border-radius: 5px;
font-size: 12px;
box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
">

Dibuat oleh : Muhammad Maskuri

</div>
'''

m.get_root().html.add_child(
    folium.Element(creator_html)
)

m.save("index.html")