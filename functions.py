import folium
import pandas as pd

# def generate_markers():
    
#     df = pd.read_csv(r'projects\tweet2map\data_mmda_traffic_spatial.csv')
    
#     for item in df.iterrows():
#     # url = f'<a href = "{item[1]["Source"]}"> Source URL</a>'
#     url = f'{item[1]["Source"]}'
#     popup_text = """ <font size="4"><b>Date: {}<br></b>\n{}
#                     <br>Source: {}</font>""".format(item[1]['Date'], item[1]['Tweet'], url)
#     iframe = folium.IFrame(
#         popup_text,
#         width=500,
#         height=130
#     )
#     popup = folium.Popup(iframe)
#     mc.add_child(folium.Marker(location=[item[1]['Latitude'], item[1]['Longitude']],
#                                 popup=popup,
#                                 clustered_marker=True)).add_to(m)