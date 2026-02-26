# src/asistente.py
# ─────────────────────────────────────────────────────────────────────────────
# Lógica del asistente: construye el prompt y llama a la API de Hugging Face.
# Adaptado para Streamlit (sin prints, devuelve resultados/errores limpios).
# ─────────────────────────────────────────────────────────────────────────────

import time
from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError

from src.config import (
    obtener_token,
    MODELO,
    MAX_TOKENS,
    TEMPERATURA,
    REINTENTOS,
    ESPERA_ENTRE_REINTENTOS,
)


def construir_prompt(ciudad: str) -> list[dict]:
    """
    Construye el prompt con sistema + usuario para el chat del modelo.

    Args:
        ciudad: Nombre de la ciudad objetivo.

    Returns:
        Lista de mensajes en formato chat.
    """
    mensaje_sistema = (
        "Eres un asistente de viajes familiar experto en turismo sostenible y "
        "de bajo coste. Respondes siempre en español, de forma clara, amigable "
        "y bien estructurada. Cada plan que sugieres debe ser apto para niños, "
        "adecuado para toda la familia y gratuito o de muy bajo coste."
    )

    mensaje_usuario = (
        f"Dame exactamente 10 planes recomendados para hacer en {ciudad} "
        f"con niños y en familia, que sean gratuitos o de muy bajo coste.\n\n"
        f"Formato de respuesta obligatorio:\n"
        f"1. **[Nombre del plan]**: [Descripción breve de 1-2 oraciones. "
        f"Indica si es gratuito o el coste aproximado.]\n"
        f"2. ...\n"
        f"...\n"
        f"10. ...\n\n"
        f"No añadas texto introductorio ni conclusión, solo la lista numerada "
        f"del 1 al 10."
    )

    return [
        {"role": "system", "content": mensaje_sistema},
        {"role": "user", "content": mensaje_usuario},
    ]


def obtener_planes(ciudad: str, callback_estado=None) -> str:
    """
    Consulta el LLM en Hugging Face y devuelve 10 planes familiares.

    Args:
        ciudad: Nombre de la ciudad.
        callback_estado: Función opcional para reportar estado (ej. st.status).

    Returns:
        Texto con los 10 planes recomendados.

    Raises:
        ConnectionError: Si falla la API tras los reintentos.
        ValueError: Si la respuesta está vacía.
        EnvironmentError: Si falta el token.
    """
    token = obtener_token()
    cliente = InferenceClient(token=token)
    mensajes = construir_prompt(ciudad)

    for intento in range(1, REINTENTOS + 1):
        try:
            if callback_estado:
                callback_estado(f"Consultando al modelo (intento {intento}/{REINTENTOS})...")

            respuesta = cliente.chat.completions.create(
                model=MODELO,
                messages=mensajes,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURA,
            )

            texto = respuesta.choices[0].message.content.strip()

            if not texto:
                raise ValueError("El modelo devolvió una respuesta vacía.")

            return texto

        except HfHubHTTPError as e:
            if intento < REINTENTOS:
                if callback_estado:
                    callback_estado(
                        f"Error en intento {intento}. Reintentando en "
                        f"{ESPERA_ENTRE_REINTENTOS}s..."
                    )
                time.sleep(ESPERA_ENTRE_REINTENTOS)
            else:
                raise ConnectionError(
                    f"No se pudo conectar con la API de Hugging Face "
                    f"tras {REINTENTOS} intentos. Detalle: {e}"
                ) from e

        except Exception as e:
            if isinstance(e, (ValueError, EnvironmentError)):
                raise
            if intento < REINTENTOS:
                if callback_estado:
                    callback_estado(
                        f"Error inesperado en intento {intento}. "
                        f"Reintentando en {ESPERA_ENTRE_REINTENTOS}s..."
                    )
                time.sleep(ESPERA_ENTRE_REINTENTOS)
            else:
                raise ConnectionError(
                    f"Error inesperado tras {REINTENTOS} intentos: "
                    f"{type(e).__name__}: {e}"
                ) from e
