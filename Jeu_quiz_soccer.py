import streamlit as st
# Configuration
st.set_page_config(page_title="Quiz Soccer", page_icon="⚽", layout="centered")
# Initialisation
if "étape" not in st.session_state:
   st.session_state.étape = 0
if "score" not in st.session_state:
   st.session_state.score = 0
if "vies" not in st.session_state:
   st.session_state.vies = 3
# Fonction de redémarrage
def recommencer():
   st.session_state.étape = 0
   st.session_state.score = 0
   st.session_state.vies = 3
# Style
st.markdown(
   """
<style>
       .stButton>button {
           background-color: #1e90ff;
           color: blue;
           font-size: 16px;
           border-radius: 10px;
           padding: 0.75em 2em;
       }
       .stRadio label {
           font-size: 36px;
       }
       .score {
           text-align:center;
           font-size:36px;
           color:# 66fff;
           margin-bottom:10px;
       }
       .vie {
           text-align:center;
           font-size:18px;
           color:#dc3545;
           margin-bottom:20px;
       }
</style>
   """, unsafe_allow_html=True
)
# Affichage score et vies
st.markdown(f"<div class='score'>Score : {st.session_state.score}/10</div>", unsafe_allow_html=True)
st.markdown(f"<div class='vie'>Vies restantes : {st.session_state.vies}</div>", unsafe_allow_html=True)
# Données des questions
questions = [
   {
       "question": "Quel pays a remporté la Coupe du Monde 2014 ?",
       "options": ["", "France", "Allemagne", "Brésil"],
       "réponse": "Allemagne"
   },
   {
       "question": "Quel joueur a le plus de Ballon d'Or (jusqu'en 2024) ?",
       "options": ["", "Cristiano Ronaldo", "Lionel Messi", "Zinedine Zidane"],
       "réponse": "Lionel Messi"
   },
   {
       "question": " Quel est le pays qui a remporté le plus de coupe du monde ?",
       "options": ["", "Brezil", "France", "Allemagne"],
       "réponse": "Brezil"
   },
   {
       "question": "Quel club a remporté le plus de Ligue des Champions ?",
       "options": ["", "Barcelone", "Manchester City", "Real Madrid"],
       "réponse": "Real Madrid"
   },
   {
       "question": "Quel pays a organisé la Coupe du Monde 2022 ?",
       "options": ["", "Qatar", "Russie", "États-Unis"],
       "réponse": "Qatar"
   },
   {
       "question": "Qui est surnommé 'CR7' ?",
       "options": ["", "Cristiano Ronaldo", "Karim Benzema", "Neymar"],
       "réponse": "Cristiano Ronaldo"
   },
   {
       "question": "Comment s'appelle le stade du FC Barcelone ?",
       "options": ["", "Old Trafford", "Santiago Bernabeu", "Camp Nou"],
       "réponse": "Camp Nou"
   },
   {
       "question": " Qui est nome la pulga ?",
       "options": ["", "Messi", "Ronaldinho", "Zidane"],
       "réponse": "Messi"
   },
   {
       "question": "Quel joueur brésilien porte souvent le numéro 10 ?",
       "options": ["", "Ronaldinho", "Neymar", "Vinicius Jr"],
       "réponse": "Neymar"
   },
   {
       "question": "Qui a gagner le balon d'or en 2011 ?",
       "options": ["", " Cristiano Ronaldo, " Lionel Messi ", "Robert Lewandowski"],
       "réponse": "Lionel Messi"
   }
]
# Jeu
if st.session_state.étape == 0:
   st.title("⚽ Quiz Soccer")
   st.markdown("Bienvenue dans le quiz soccer ! Réponds correctement à 10 questions pour gagner. "
               "Tu as **3 vies**, attention aux erreurs !")
   if st.button("Commencer"):
       st.session_state.étape = 1
elif 1 <= st.session_state.étape <= len(questions):
   q = questions[st.session_state.étape - 1]
   st.markdown(f"**Question {st.session_state.étape} :** {q['question']}")
   choix = st.radio("Fais ton choix :", q["options"], key=f"question_{st.session_state.étape}")
   if st.button("Valider", key=f"valider_{st.session_state.étape}"):
       if choix == q["réponse"]:
           st.session_state.score += 1
           st.session_state.étape += 1
       elif choix == "":
           st.warning("Choisis une réponse avant de valider.")
       else:
           st.session_state.vies -= 1
           if st.session_state.vies == 0:
               st.error("C’EST FAUX. Tu as perdu toutes tes vies. On recommence !")
               recommencer()
           else:
               st.error(f"C’EST FAUX. Il te reste {st.session_state.vies} vies.")
elif st.session_state.étape > len(questions):
   st.balloons()
   st.success("Félicitations ! Tu as complété le quiz.")
   st.markdown(f"**Score final : {st.session_state.score}/10**")
   if st.button("Recommencer"):
       recommencer()
