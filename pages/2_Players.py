import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="running",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jagador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

cal1, cal2, cal3, cal4 =st.columns(4)
cal1.markdown(f"**Idade:** {player_stats['Age']}")
cal2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
cal3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

ccal1, cal2, cal3, cal4 =st.columns(4)
cal1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
cal1.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
cal1.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")


