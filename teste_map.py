import pandas as pd
import streamlit as st
import pydeck as pdk
import time

st.sidebar.image("Black.png")
tab_moto= pd.read_csv("C:/Users/user/Desktop/WORKING_SQL/Relatorios/cordenadas.csv")
tabg= pd.read_csv("C:/Users/user/Desktop/WORKING_SQL/genero.csv")

def conc():
    cont= st.container(border= True, height= 100)
    cont.markdown("")
    
def maps():
    st.sidebar.metric(label="TOTAL DE ATENDIMENTOS", value=76,
                      delta='2.1%', delta_color='normal')
    df= pd.DataFrame(tab_moto)
    container_map = st.container(border=True, height=680)
    container_map.subheader('ANALISE - DISPERSAO DEMOGRAFICA', divider=True)
    container_map.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=-16.71824512937061,
            longitude=-43.85249956265636,
            zoom=14,
            pitch=40,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=20,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
                pickable=True,
                coverage=3,
                auto_highlight=True,
                get_color="[20, 30, 75, 100]",
            ),
        ],
    ))
    st.sidebar.subheader("GENERO", divider= True)
    gen= st.sidebar.radio(
        "",
        ["Homens", "Mulheres"],
        index= None
    )

    if gen == "Homens":
        with st.spinner('carregando'):
            time.sleep(2)
            st.sidebar.subheader(". 83,9%")
            st.sidebar.markdown(". Media cc: 250")
            st.sidebar.markdown(". Ticket: R$ 28.042,13")
            st.sidebar.divider()
    elif gen == "Mulheres":
        with st.spinner('carregando'):
            time.sleep(2)
            st.sidebar.subheader(". 16,1%")
            st.sidebar.markdown(". Media cc: 150")
            st.sidebar.markdown(". Ticket: R$ 17.212,24")
            st.sidebar.divider()
    else:
        st.sidebar.divider()

    container_map.info('🌎. Os dados são de fonte local, demonstrando a dispersão geográfica de clientes em Montes Claros e região')
    
maps()

texto= st.sidebar.button("A análise de dispersão geográfica é uma ferramenta poderosa para otimizar campanhas de publicidade, permitindo direcionar recursos, personalizar mensagens e maximizar o retorno sobre o investimento. Ao compreender como nosso público está distribuído no espaço, podemos tomar decisões estratégicas para alcançar melhores resultados.")
if texto == True:
    conc()
elif texto == False:
    pass
# st.sidebar.subheader("CORDENADAS")
# st.sidebar.dataframe(tab_moto, hide_index= True)
