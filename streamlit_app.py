# -*- coding: utf-8 -*-
"""
Created on Tue Oct 4 00:09:17 2023

@author: Gabriel Yashim
"""

import numpy as np 
import pickle
import streamlit as st


model = pickle.load(open('Catboost_classifier.pkl', 'rb'))


st.title('Cholera Cases Fatality Rate Prediction System')
html_temp = """
    <h3 style="color:white;text-align:center;"></h3>
    <div style="background-color:;padding:10px;margin-bottom:3rem">
        <p style="text-align:justify;">
            Cholera is an acute diarrhoeal infection caused by ingestion of food or water contaminated with the bacterium Vibrio cholerae. Cholera remains a global threat to public health and an indicator of inequity and lack of social development. This system is able to predict the fatality rate of Cholera Disease in a Country, given the required information.
        </p>  
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)


# Dictionary to map locations to integer values
country_mapping = {
    "":"",
    "Afghanistan":0,
    "Albania":1,
    "Algeria":2,
    "Angola":3,
    "Argentina":4,
    "Armenia":5,
    "Australia":6,
    "Austria":7,
    "Azerbaijan":8,
    "Bahamas":9,
    "Bahrain":10,
    "Bangladesh":11,
    "Belarus":12,
    "Belgium":13,
    "Belize":14,
    "Benin":15,
    "Bhutan":16,
    "Bolivia (Plurinational State of)":17,
    "Botswana":18,
    "Brazil":19,
    "Brunei Darussalam":20,
    "Burkina Faso":21,
    "Burundi":22,
    "Cabo Verde":23,
    "Cambodia":24,
    "Cameroon":25,
    "Canada":26,
    "Central African Republic":27,
    "Chad":28,
    "Chile":29,
    "China":30,
    "Colombia":31,
    "Comoros":32,
    "Congo":33,
    "Costa Rica":34,
    "Cuba":35,
    "Czechia":36,
    "Côte d'Ivoire":37,
    "Democratic People's Republic of Korea":38,
    "Democratic Republic of the Congo":39,
    "Denmark":40,
    "Djibouti":41,
    "Dominican Republic":42,
    "Ecuador":43,
    "El Salvador":44,
    "Equatorial Guinea":45,
    "Eritrea":46,
    "Estonia":47,
    "Eswatini":48,
    "Ethiopia":49,
    "Finland":50,
    "France":51,
    "Gabon":52,
    "Gambia":53,
    "Georgia":54,
    "Germany":55,
    "Ghana":56,
    "Greece":57,
    "Guatemala":58,
    "Guinea":59,
    "Guinea-Bissau":60,
    "Guyana":61,
    "Haiti":62,
    "Honduras":63,
    "Hungary":64,
    "India":65,
    "Indonesia":66,
    "Iran (Islamic Republic of)":67,
    "Iraq":68,
    "Israel":69,
    "Italy":70,
    "Japan":71,
    "Jordan":72,
    "Kazakhstan":73,
    "Kenya":74,
    "Kiribati":75,
    "Kuwait":76,
    "Kyrgyzstan":77,
    "Lao People's Democratic Republic":78,
    "Lebanon":79,
    "Lesotho":80,
    "Liberia":81,
    "Libya":82,
    "Madagascar":83,
    "Malawi":84,
    "Malaysia":85,
    "Maldives":86,
    "Mali":87,
    "Marshall Islands":88,
    "Mauritania":89,
    "Mauritius":90,
    "Mexico":91,
    "Micronesia (Federated States of)":92,
    "Mongolia":93,
    "Morocco":94,
    "Mozambique":95,
    "Myanmar":96,
    "Namibia":97,
    "Nauru":98,
    "Nepal":99,
    "Netherlands":100,
    "New Zealand":101,
    "Nicaragua":102,
    "Niger":103,
    "Nigeria":104,
    "Norway":105,
    "Oman":106,
    "Pakistan":107,
    "Panama":108,
    "Papua New Guinea":109,
    "Paraguay":110,
    "Peru":111,
    "Philippines":112,
    "Poland":113,
    "Portugal":114,
    "Qatar":115,
    "Republic of Korea":116,
    "Republic of Moldova":117,
    "Romania":118,
    "Russian Federation":119,
    "Rwanda":120,
    "Samoa":121,
    "Sao Tome and Principe":122,
    "Saudi Arabia":123,
    "Senegal":124,
    "Seychelles":125,
    "Sierra Leone":126,
    "Singapore":127,
    "Slovenia":128,
    "Somalia":129,
    "South Africa":130,
    "South Sudan":131,
    "Spain":132,
    "Sri Lanka":133,
    "Sudan":134,
    "Suriname":135,
    "Sweden":136,
    "Switzerland":137,
    "Syrian Arab Republic":138,
    "Tajikistan":139,
    "Thailand":140,
    "The former state union Serbia and Montenegro":141,
    "Togo":142,
    "Tonga":143,
    "Tunisia":144,
    "Turkey":145,
    "Turkmenistan":146,
    "Tuvalu":147,
    "Uganda":148,
    "Ukraine":149,
    "United Arab Emirates":150,
    "United Kingdom of Great Britain and Northern Ireland":151,
    "United Republic of Tanzania":152,
    "United States of America":153,
    "Uzbekistan":154,
    "Venezuela (Bolivarian Republic of)":155,
    "Viet Nam":156,
    "Yemen":157,
    "Zambia":158,
    "Zimbabwe":159
}


# Dropdown select box
selected_country = st.selectbox("Select Country:", list(country_mapping.keys()))
year = st.text_input("Enter the Year")
cases = st.text_input("Number of reported cases of cholera:")
death = st.text_input("Number of reported deaths from cholera:")

# storing the selected values in different variables    
country_value = country_mapping[selected_country]



pred = ''

result = ''


if st.button('Submit'):
    pred = model.predict([[country_value, year, cases, death]])
        
    st.write(f"Cholera case fatality rate:  {pred[0]:.2f}")
    




