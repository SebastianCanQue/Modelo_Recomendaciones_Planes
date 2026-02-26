# 🗺️ Asistente de Planes Familiares con IA

Asistente de inteligencia artificial que recomienda **10 planes familiares, aptos para niños y de bajo coste o gratuitos** para cualquier ciudad que indiques.

Utiliza la API de inferencia de Hugging Face (modelo **Llama-3.2-3B-Instruct**), por lo que el modelo corre en los servidores de HF y **no consume recursos de tu PC**.

Incluye una **interfaz web con Streamlit** profesional y minimalista, además de la versión de consola.

---

## 📁 Estructura del proyecto

```
├── app.py               → Aplicación web Streamlit (punto de entrada UI)
├── main.py              → Punto de entrada por consola (CLI)
├── asistente.py         → Lógica de IA (versión consola)
├── config.py            → Configuración (versión consola)
├── src/
│   ├── __init__.py
│   ├── asistente.py     → Lógica de IA adaptada para Streamlit
│   ├── config.py        → Configuración con soporte Streamlit secrets
│   └── ui/
│       ├── __init__.py
│       ├── components.py → Componentes reutilizables de la UI
│       └── styles.py     → CSS personalizado
├── .streamlit/
│   └── config.toml      → Tema y configuración de Streamlit
├── requirements.txt     → Dependencias
├── .env.example         → Plantilla para configurar tu token
└── .gitignore           → Excluye archivos sensibles
```

---

## ⚙️ Preparar el entorno

### 1. Crear y activar el entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar el token de Hugging Face

Copia el archivo de ejemplo y añade tu token:

```bash
cp .env.example .env
```

Edita `.env` y reemplaza el valor:

```
HF_TOKEN=hf_tu_token_real_aqui
```

> 🔑 Consigue tu token gratuito en **https://huggingface.co/settings/tokens**
> (crea uno de tipo **Read**)

---

## ▶️ Ejecutar la aplicación

### Interfaz web (Streamlit) — Recomendado

```bash
streamlit run app.py
```

Se abrirá automáticamente en tu navegador en `http://localhost:8501`.

### Versión por consola (CLI)

```bash
python main.py
```

---

### Ejemplo de uso (consola)

```
📍 Ingresa el nombre de una ciudad: Granada

✅ 10 planes familiares recomendados para: GRANADA
------------------------------------------------------------
1. Visita a la Alhambra (entrada gratuita menores de 12 años): ...
2. Paseo por el Albaicín: ...
...
```

---

## 🚀 Desplegar en Streamlit Cloud

1. Sube el proyecto a un repositorio de GitHub.
2. Ve a [share.streamlit.io](https://share.streamlit.io) y conecta tu repo.
3. En **Advanced settings → Secrets**, añade:
   ```
   HF_TOKEN = "hf_tu_token_real_aqui"
   ```
4. Haz clic en **Deploy**.

---

## 🔒 Seguridad

- **Nunca subas el archivo `.env` a GitHub.** Ya está incluido en el `.gitignore`.
- Si compartes el proyecto, usa `.env.example` como referencia.

