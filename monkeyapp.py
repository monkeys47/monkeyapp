import streamlit as st
import bcrypt
from datetime import datetime, timedelta

# Base de datos de usuarios
users = {
    "admin": {
        "password": bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode(),
        "tipo": "permanente",
        "expiración": None
    },
    "temp_user": {
        "password": bcrypt.hashpw("temp123".encode(), bcrypt.gensalt()).decode(),
        "tipo": "temporal",
        "expiración": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    }
}

# Función para verificar usuario y contraseña
def authenticate(username, password):
    if username in users:
        user = users[username]
        if user["tipo"] == "temporal" and user["expiración"]:
            # Verifica si la cuenta temporal ha expirado
            if datetime.now() > datetime.strptime(user["expiración"], "%Y-%m-%d"):
                st.error("Cuenta temporal expirada. Contacta al administrador.")
                return False
        hashed_pw = user["password"]
        return bcrypt.checkpw(password.encode(), hashed_pw.encode())
    return False

# Interfaz de inicio de sesión
def login():
    st.title("Inicio de Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar Sesión"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
            st.success(f"Acceso concedido ({users[username]['tipo']})")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

# Interfaz principal (después de iniciar sesión)
def main_app():
    st.title(f"Bienvenido, {st.session_state['user']}!")
    st.write(f"Tipo de cuenta: {users[st.session_state['user']]['tipo']}")
    if users[st.session_state['user']]['tipo'] == "temporal":
        expiración = users[st.session_state['user']]['expiración']
        st.warning(f"Tu cuenta expira el: {expiración}")
    st.file_uploader("Sube tu archivo de correos (CSV, TXT, etc.)", type=["csv", "txt"])
    if st.button("Cerrar Sesión"):
        st.session_state["authenticated"] = False
        st.experimental_rerun()

# Control de sesión
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state["authenticated"]:
    main_app()
else:
    login()