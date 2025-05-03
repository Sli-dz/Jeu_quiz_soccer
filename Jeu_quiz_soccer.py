import streamlit as st
def erreur():
   st.markdown(
       "<h1 style='text-align: center; color: red; font-size: 100px;'>C’EST FAUX !</h1>",
       unsafe_allow_html=True
   )
   st.stop()  # Arrête tout et reste sur le message
def recommencer():
   st.experimental_rerun()
def jeu_foot():
   st.markdown("<h1 style='text-align: center; color: darkgreen;'>QUIZ AVENTURE FOOT</h1>", unsafe_allow_html=True)
   # Étape 1
   q1 = st.radio("1. Quel pays a gagné la Coupe du Monde 2018 ?", ["Brésil", "France", "Argentine", "Allemagne"])
   if q1 != "France":
       erreur()
       recommencer()
   st.success("Bonne réponse !")
   # Étape 2
   q2 = st.radio("2. Qui est surnommé 'La Pulga' ?", ["Cristiano Ronaldo", "Mbappé", "Messi", "Griezmann"])
   if q2 != "Messi":
       erreur()
       recommencer()
   st.success("Bonne réponse !")
 
   # Étape 3
   q10 = st.radio("10. Quel pays a remporté la première Coupe du Monde en 1930 ?", ["Italie", "Argentine", "Uruguay", "France"])
   if q10 != "Uruguay":
       erreur()
       recommencer()
   st.success("Félicitations ! Tu as terminé le quiz comme un champion !")
jeu_foot()