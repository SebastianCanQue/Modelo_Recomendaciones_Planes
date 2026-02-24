# asistente.py
# ─────────────────────────────────────────────────────────────────────────────
# Módulo principal del asistente: construye el prompt y llama a la API de
# Hugging Face usando InferenceClient (sin descargar el modelo en tu PC).
# ─────────────────────────────────────────────────────────────────────────────

import time
from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError
from config import obtener_token

# ── Modelo a utilizar ────────────────────────────────────────────────────────
# Mistral-7B-Instruct sigue instrucciones en español con muy buenos resultados.
# Si prefieres, puedes cambiarlo por: "meta-llama/Meta-Llama-3-8B-Instruct"
MODELO = "meta-llama/Llama-3.2-3B-Instruct"

# ── Parámetros de generación ─────────────────────────────────────────────────
MAX_TOKENS = 1024       # Suficiente para 10 planes detallados
TEMPERATURA = 0.7       # Equilibrio entre creatividad y coherencia
REINTENTOS = 3          # Número de intentos ante fallos de red
ESPERA_ENTRE_REINTENTOS = 5  # Segundos entre reintento y reintento


def construir_prompt(ciudad: str) -> str:
    """
    Construye el mensaje de sistema y el mensaje de usuario que se enviarán
    al modelo de lenguaje.

    Args:
        ciudad (str): Nombre de la ciudad para la que se piden planes.

    Returns:
        list[dict]: Lista de mensajes en formato chat (system + user).
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
        f"1. [Nombre del plan]: [Descripción breve de 1-2 oraciones. "
        f"Indica si es gratuito o el coste aproximado.]\n"
        f"2. ...\n"
        f"...\n"
        f"10. ...\n\n"
        f"No añadas texto introductorio ni conclusión, solo la lista numerada "
        f"del 1 al 10."
    )

    return [
        {"role": "system", "content": mensaje_sistema},
        {"role": "user",   "content": mensaje_usuario},
    ]


def obtener_planes(ciudad: str) -> str:
    """
    Consulta el LLM en Hugging Face y devuelve 10 planes familiares
    para la ciudad indicada.

    Args:
        ciudad (str): Nombre de la ciudad.

    Returns:
        str: Texto con los 10 planes recomendados.

    Raises:
        ConnectionError: Si no se puede conectar con la API tras varios intentos.
        ValueError: Si la respuesta del modelo está vacía o es inválida.
    """
    # Obtenemos el token de forma segura desde la variable de entorno
    token = obtener_token()

    # Instanciamos el cliente — la inferencia ocurre en los servidores de HF,
    # NO en tu PC, por lo que el consumo de recursos local es mínimo.
    cliente = InferenceClient(token=token)

    mensajes = construir_prompt(ciudad)

    # ── Bucle de reintentos ──────────────────────────────────────────────────
    for intento in range(1, REINTENTOS + 1):
        try:
            print(f"   🔄 Consultando al modelo (intento {intento}/{REINTENTOS})...")

            respuesta = cliente.chat.completions.create(
                model=MODELO,
                messages=mensajes,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURA,
            )

            # Extraemos el texto generado de la respuesta
            texto = respuesta.choices[0].message.content.strip()

            if not texto:
                raise ValueError("El modelo devolvió una respuesta vacía.")

            return texto

        except HfHubHTTPError as e:
            # Errores HTTP de la API de Hugging Face (ej. 429 rate limit, 503)
            print(f"   ⚠️  Error HTTP de la API (intento {intento}): {e}")
            if intento < REINTENTOS:
                print(f"   ⏳ Esperando {ESPERA_ENTRE_REINTENTOS}s antes de reintentar...")
                time.sleep(ESPERA_ENTRE_REINTENTOS)
            else:
                raise ConnectionError(
                    f"❌ No se pudo conectar con la API de Hugging Face "
                    f"tras {REINTENTOS} intentos.\n"
                    f"   Detalle del error: {e}\n"
                    f"   Verifica tu conexión a internet y que tu token HF_TOKEN "
                    f"sea válido y tenga permisos de lectura."
                ) from e

        except Exception as e:
            # Cualquier otro error inesperado (timeout, red caída, etc.)
            print(f"   ⚠️  Error inesperado (intento {intento}): {type(e).__name__}: {e}")
            if intento < REINTENTOS:
                print(f"   ⏳ Esperando {ESPERA_ENTRE_REINTENTOS}s antes de reintentar...")
                time.sleep(ESPERA_ENTRE_REINTENTOS)
            else:
                raise ConnectionError(
                    f"❌ Error inesperado al llamar a la API tras {REINTENTOS} intentos.\n"
                    f"   Tipo de error: {type(e).__name__}\n"
                    f"   Detalle: {e}"
                ) from e

