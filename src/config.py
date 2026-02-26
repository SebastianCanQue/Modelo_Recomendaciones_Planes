# src/config.py
# ─────────────────────────────────────────────────────────────────────────────
# Módulo de configuración: lee variables de entorno de forma segura.
# Compatible con Streamlit (st.secrets) y con ejecución local (.env).
# ─────────────────────────────────────────────────────────────────────────────

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Constantes del modelo ────────────────────────────────────────────────────
MODELO = "meta-llama/Llama-3.2-3B-Instruct"
MAX_TOKENS = 1024
TEMPERATURA = 0.7
REINTENTOS = 3
ESPERA_ENTRE_REINTENTOS = 5


def obtener_token() -> str:
    """
    Obtiene el token de Hugging Face priorizando:
      1. st.secrets (para Streamlit Cloud)
      2. Variable de entorno HF_TOKEN (.env o sistema)

    Returns:
        str: Token de la API de Hugging Face.

    Raises:
        EnvironmentError: Si no se encuentra el token en ninguna fuente.
    """
    # 1. Intentar desde Streamlit secrets (deploy en Streamlit Cloud)
    try:
        token = st.secrets.get("HF_TOKEN")
        if token:
            return token
    except FileNotFoundError:
        pass

    # 2. Intentar desde variable de entorno
    token = os.getenv("HF_TOKEN")
    if token:
        return token

    raise EnvironmentError(
        "No se encontró el token HF_TOKEN. "
        "Configúralo en el archivo .env o en Streamlit secrets."
    )
