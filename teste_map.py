import pandas as pd
import streamlit as st
import pydeck as pdk

st.logo("inmotors.png")
tab_moto= pd.read_csv("cordenadas.csv")
tabg= pd.read_csv("genero.csv")
tot= tabg.median()
def maps():
    df= pd.DataFrame(tab_moto)
    container_map = st.container(border=True, height=720)
    container_map.subheader('RELATÓRIO - DISPERSÃO ', divider=True)
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

    container_map.info('🌎 . Os dados são de fonte local, demonstrando a dispersão geográfica de clientes em Montes Claros e região')

with st.popover("ANÁLISE - GEOGRÁFICA"):
    st.markdown("A análise de dispersão geográfica é uma ferramenta poderosa para otimizar campanhas de publicidade, permitindo direcionar recursos, personalizar mensagens e maximizar o retorno sobre o investimento. Ao compreender como o nosso público está distribuído no espaço, podemos tomar decisões mais estratégicas para alcançar melhores resultados.")
st.sidebar.metric(label="TOTAL DE ATENDIMENTOS", value=76,
                  delta='2.1%', delta_color='normal')

maps()
gen= st.sidebar.radio(
    "GENERO",
    ["Homens", "Mulheres"],
    index= None
)
if gen == "Homens":
    st.sidebar.write("83,9%")
elif gen == "Mulheres":
    st.sidebar.write("16,1%")

st.sidebar.subheader("CORDENADAS")
st.sidebar.dataframe(tab_moto, hide_index= True)
