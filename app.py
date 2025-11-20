import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Dashboard Financiero")

# --- INICIO DE LA BARRA LATERAL MEJORADA ---
st.sidebar.header('Configuración')

# 1. Damos opciones predefinidas para facilitar la prueba
opcion = st.sidebar.selectbox(
    'Elige una acción o escribe una:',
    ('Usar Ticker Personalizado', 'Apple (AAPL)', 'Google (GOOGL)', 'Tesla (TSLA)', 'Bitcoin (BTC-USD)', 'Euro/Dolar (EURUSD=X)')
)

# 2. Lógica para seleccionar el símbolo
if opcion == 'Usar Ticker Personalizado':
    ticker_symbol = st.sidebar.text_input("Escribe el símbolo (Ej: NVDA)", value='SPY')
else:
    # Extraemos el código del paréntesis. Ej: "Apple (AAPL)" -> "AAPL"
    ticker_symbol = opcion.split('(')[-1].strip(')')

# 3. Ayuda visual para el usuario
st.sidebar.info(
    """
    💡 **Ayuda:**
    Los símbolos son los códigos de Yahoo Finance.
    - Acciones: `AAPL`, `MSFT`
    - Cripto: `BTC-USD`, `ETH-USD`
    - Divisas: `EURUSD=X`
    
    [Buscar símbolos aquí](https://finance.yahoo.com/lookup)
    """
)

start_date = st.sidebar.date_input("Fecha de inicio", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("Fecha de fin", value=pd.to_datetime("today"))
# --- FIN DE LA BARRA LATERAL MEJORADA ---

st.title(f'📈 Análisis de Acciones: {ticker_symbol}')

# --- MODIFICACIÓN AQUÍ ---
def cargar_datos(ticker):
    # Eliminamos el try/except silencioso para ver el error
    try:
        # Descargamos datos
        data = yf.Ticker(ticker)
        # Usamos 'auto_adjust=True' que suele dar menos problemas
        df = data.history(start=start_date, end=end_date, auto_adjust=True)
        
        if df.empty:
            st.warning(f"Yahoo Finance devolvió una tabla vacía para {ticker}.")
            return None, None
            
        return df, data.info
    except Exception as e:
        # Esto imprimirá el error real en tu web para que sepamos qué pasa
        st.error(f"Ocurrió un error al cargar los datos: {e}")
        return None, None
# -------------------------

st.write("Cargando datos...")
df_acciones, info_empresa = cargar_datos(ticker_symbol)

if df_acciones is not None and not df_acciones.empty:
    st.subheader("Resumen Financiero")
    col1, col2, col3 = st.columns(3)
    
    # Manejo de errores si falta información específica
    precio_actual = df_acciones['Close'].iloc[-1]
    market_cap = info_empresa.get('marketCap', 'No disponible')
    sector = info_empresa.get('sector', 'No disponible')

    col1.metric("Precio Cierre (Último)", f"${precio_actual:.2f}")
    col2.metric("Volumen Mercado", f"{market_cap}")
    col3.metric("Sector", sector)

    st.subheader("Evolución del Precio")
    fig = go.Figure(data=[go.Candlestick(x=df_acciones.index,
                    open=df_acciones['Open'],
                    high=df_acciones['High'],
                    low=df_acciones['Low'],
                    close=df_acciones['Close'])])
    
    fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Ver datos históricos detallados"):
        st.dataframe(df_acciones)

    st.download_button(
        label="Descargar datos en CSV",
        data=df_acciones.to_csv().encode('utf-8'),
        file_name=f'{ticker_symbol}_data.csv',
        mime='text/csv',
    )