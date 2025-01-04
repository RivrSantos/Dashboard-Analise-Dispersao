import pandas as pd
import streamlit as st
import pydeck as pdk
import time


tab_moto= pd.read_csv("cordenadas.csv") # arquivo principal
st.sidebar.image("Black.png")


# funçao para exibir as cordenadas em um dataframe
def lat_lon():
   st.sidebar.dataframe(tab_moto, hide_index= True)
    
# funçao para exibir texto dentro de um container usando formato markdown
def conc():
     st.info("A análise de dispersão geográfica é uma ferramenta poderosa para otimizar campanhas de publicidade, permitindo direcionar recursos, personalizar mensagens e maximizar o retorno sobre o investimento. Ao compreender como nosso público está distribuído no espaço, podemos tomar decisões estratégicas para alcançar melhores resultados.")

# funçao para exibiçao do mapa e suas determinadas cordenadas dentro de um container principal
def maps():
    st.sidebar.metric(label="TOTAL DE ATENDIMENTOS", value=76,
                      delta='2.1%', delta_color='normal')
    df= pd.DataFrame(tab_moto)
    container_map = st.container(border=True, height=700)
    container_map.subheader('RELATORIO - DISPERSAO DEMOGRAFICA', divider=True)
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
                get_color="[120, 30, 75, 300]",
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
         st.sidebar.subheader(". 83,9%")
         st.sidebar.markdown(". Media cc: 250")
         st.sidebar.markdown(". Ticket: R$ 28.042,13")
         st.sidebar.divider()
    elif gen == "Mulheres":
         st.sidebar.subheader(". 16,1%")
         st.sidebar.markdown(". Media cc: 150")
         st.sidebar.markdown(". Ticket: R$ 17.212,24")
         st.sidebar.divider()
    else:
        st.sidebar.divider()

    container_map.info('🌎. Os dados são de fonte local, demonstrando a dispersão geográfica de clientes em Montes Claros e região')

# chamada principal
maps()

texto= st.sidebar.button("Resumo")
if texto == True:
    conc()
  
cord= st.sidebar.button("Cordenadas")
if cord == True:
    lat_lon()

