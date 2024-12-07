import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données utilisateur
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

authenticator.login()

def accueil():
    st.title("Bienvenue sur ma page")
    st.image("welcome.png")

def album_chat():
    st.title("Bienvenue dans l'album de mon chat 😻")
    # Affichage des images en ligne (3 par ligne)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Chat_mignion01.png", width=450)

    with col2:
        st.image("Chat_mignion02.png", width=450)

    with col3:
        st.image("Chat_mignion03.png", width=450)

    # Affichage des images en ligne (3 par ligne) 
    # autres méthodes
    #cols = st.columns(3)
    #for i, img in enumerate(images):
    #    with cols[i % 3]:
    #        st.image(img, use_column_width=True, caption=f"Chat {i + 1}")
    

if st.session_state["authentication_status"]:

    # Ajouter le bouton de déconnexion
    authenticator.logout("Déconnexion", "sidebar")

    # Menu dans la sidebar
    with st.sidebar:
        
        choix = option_menu(
            "Menu",
            ["🤩 Accueil", " 🐱 Les photos de mon chat"],
            icons=["house", "camera"],
            menu_icon="menu",
            default_index=0
    )
    
    if choix == "🤩 Accueil":
        accueil()
    elif choix == " 🐱 Les photos de mon chat":
        album_chat()
    
    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le mot de passe est incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis.")
