import streamlit as st
# Configuration de la page
st.set_page_config(page_title="Aventure Foot", page_icon="⚽", layout="centered")
# Initialisation des variables
if "étape" not in st.session_state:
   st.session_state.étape = 0
if "score" not in st.session_state:
   st.session_state.score = 0
# Fonction pour recommencer
def recommencer():
   st.session_state.étape = 0
   st.session_state.score = 0
# Affiche le score en haut
st.markdown(f"<div style='text-align:center; color:#32CD32; font-size:18px;'>Score : {st.session_state.score}/10</div>", unsafe_allow_html=True)
# Styles CSS
st.markdown("""
<style>
       body {
           background-color: #001f3f;
       }
       .stButton>button {
           background-color: #006400;
           color: white;
           border-radius: 10px;
           height: 3em;
           width: 100%;
           font-size: 16px;
       }
       .stRadio label {
           font-size: 18px;
           color: #FAFAFA;
       }
       .stMarkdown h1, h2, h3 {
           color: #32CD32;
       }
</style>
""", unsafe_allow_html=True)
# MENU PRINCIPAL
if st.session_state.étape == 0:
   st.title("⚽ Aventure Football")
   st.image("https://cdn.pixabay.com/photo/2013/07/12/12/58/soccer-146298_960_720.png", width=200)
   st.markdown("**Bienvenue jeune footballeur !** Tu vas devoir répondre à 10 questions pour atteindre la finale de la Coupe du Monde. "
               "Attention, une seule erreur et tu recommences tout…")
   if st.button("Commencer le quiz"):
       st.session_state.étape = 1
# Étapes 1 à 10
questions = [
   ("Quel pays a gagné la Coupe du Monde 2018 ?", ["", "Brésil", "France", "Argentine"], "France"),
   ("Qui a le plus de Ballons d’Or ?", ["", "Cristiano Ronaldo", "Messi", "Pelé"], "Messi"),
   ("Quel club est basé à Manchester ?", ["", "Chelsea", "Real Madrid", "Manchester City"], "Manchester City"),
   ("Quelle est la couleur principale du maillot de l’Italie ?", ["", "Bleu", "Rouge", "Vert"], "Bleu"),
   ("Combien y a-t-il de joueurs dans une équipe sur le terrain ?", ["", "10", "11", "12"], "11"),
   ("Quel joueur est surnommé 'CR7' ?", ["", "Cristiano Ronaldo", "Carlos Ramos", "Ronaldinho"], "Cristiano Ronaldo"),
   ("Dans quel pays se joue la Liga ?", ["", "Italie", "Espagne", "Portugal"], "Espagne"),
   ("Quel est le surnom de l’équipe de France ?", ["", "Les Diables Rouges", "Les Bleus", "La Roja"], "Les Bleus"),
   ("Quel joueur argentin est considéré comme l’un des meilleurs de l’histoire ?", ["", "Messi", "Ronaldo", "Zidane"], "Messi"),
   ("Combien de minutes dure un match de foot (hors prolongation) ?", ["", "60", "90", "120"], "90"),
]
for i in range(10):
   if st.session_state.étape == i + 1:
       st.subheader(f"Question {i+1}")
       question, options, reponse = questions[i]
       choix = st.radio(question, options, key=f"q{i}")
       if st.button("Valider", key=f"btn{i}"):
           if choix == reponse:
               st.session_state.étape += 1
               st.session_state.score += 1
           else:
               st.error("C’EST FAUX ! Tu dois recommencer depuis le début.")
               recommencer()
if st.session_state.étape == 11:
   st.balloons()
   st.success("VICTOIRE ! Tu as remporté la Coupe du Monde !")
   st.markdown(f"**Score final : {st.session_state.score}/10**")
   st.image("https://cdn.pixabay.com/photo/2014/10/13/09/07/trophy-486700_960_720.jpg", width=300)
   if st.button("Rejouer"):
       recommencer()