import os
import pandas as pd
import streamlit as st
import joblib
import altair as alt

# --- TITRE ET DESCRIPTION ---
st.markdown("<h1 style='color:blue; font-weight:bold;'>Prédiction du Risque de Crédit avec Machine Learning</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color:green;'>Application réalisée par <b>Fidèle Ledoux</b></h2>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Cette application utilise un modèle de Machine Learning pour détecter si un client peut être considéré comme risqué ou non en fonction de ses informations financières et personnelles.</p>", unsafe_allow_html=True)

# --- CHARGEMENT DU MODÈLE ---
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, "tree_model.pkl")

try:
    model_pipeline = joblib.load(model_path)
    if model_pipeline is None:
        st.error("Le modèle n'a pas été chargé correctement.")
except Exception as e:
    st.error(f"Erreur lors du chargement du modèle : {str(e)}")
    model_pipeline = None

# --- SIDEBAR : INPUTS UTILISATEUR ---
st.sidebar.header("Informations du Client")

# Inputs numériques
person_age = st.sidebar.number_input("Âge", min_value=18, max_value=100, value=30)
person_income = st.sidebar.number_input("Revenu Annuel (€)", min_value=1000.0, max_value=1000000.0, value=50000.0, step=1000.0)
person_emp_length = st.sidebar.number_input("Ancienneté Professionnelle (années)", min_value=0.0, max_value=60.0, value=5.0, step=0.5)
loan_amnt = st.sidebar.number_input("Montant du Prêt (€)", min_value=500.0, max_value=1000000.0, value=10000.0, step=500.0)
loan_int_rate = st.sidebar.number_input("Taux d'Intérêt (%)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
loan_percent_income = st.sidebar.number_input("Pourcentage du Prêt sur le Revenu (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
cb_person_cred_hist_length = st.sidebar.number_input("Historique de Crédit (années)", min_value=0.0, max_value=50.0, value=10.0, step=0.5)

# Catégories pour propriété du logement
st.sidebar.subheader("Propriété du Logement")
home_options = ["OTHER", "OWN", "RENT"]
home_choice = st.sidebar.selectbox("Choisissez la catégorie", home_options)

# Catégories pour l'intention du prêt
st.sidebar.subheader("Intention du Prêt")
intent_options = ["EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"]
intent_choice = st.sidebar.selectbox("Choisissez le type de prêt", intent_options)

# Catégories pour le grade du prêt
st.sidebar.subheader("Grade du Prêt")
grade_options = ["B", "C", "D", "E", "F", "G"]
grade_choice = st.sidebar.selectbox("Choisissez le grade", grade_options)

# Historique de défaut
st.sidebar.subheader("Historique de Défaut")
default_option = st.sidebar.radio("Le client est-il déjà en défaut ?", ("Non", "Oui"))
cb_person_default_on_file_Y = 1 if default_option == "Oui" else 0

# --- CONSTRUCTION DU DATAFRAME ---
input_data = {
    "person_age": [person_age],
    "person_income": [person_income],
    "person_emp_length": [person_emp_length],
    "loan_amnt": [loan_amnt],
    "loan_int_rate": [loan_int_rate],
    "loan_percent_income": [loan_percent_income],
    "cb_person_cred_hist_length": [cb_person_cred_hist_length],
    f"person_home_ownership_{home_choice}": [1],
    f"loan_intent_{intent_choice}": [1],
    f"loan_grade_{grade_choice}": [1],
    "cb_person_default_on_file_Y": [cb_person_default_on_file_Y]
}

input_df = pd.DataFrame(input_data).fillna(0)  # Remplir les valeurs manquantes par 0

# --- VERIFICATION DES COLONNES ---
if model_pipeline is not None:
    missing_cols = set(model_pipeline.feature_names_in_) - set(input_df.columns)
    for col in missing_cols:
        input_df[col] = 0  # Ajouter les colonnes manquantes avec des valeurs par défaut

    # Réordonner les colonnes pour correspondre au modèle
    input_df = input_df[model_pipeline.feature_names_in_]

    # S'assurer que toutes les valeurs sont bien en float64
    input_df = input_df.astype('float64')

# --- AFFICHAGE DES DONNÉES ---
st.subheader("Résumé des Informations Saisies")
st.dataframe(input_df.T)

# --- PREDICTION ---
if st.button("Prédire le Risque de Crédit"):
    if model_pipeline is None:
        st.error("Le modèle n'est pas chargé. Impossible de faire la prédiction.")
    else:
        try:
            st.write("Vérification des données avant prédiction...")
            st.write(input_df)

            prediction = model_pipeline.predict(input_df)
            resultat = "Risqué" if prediction[0] == 1 else "Non Risqué"
            couleur = "red" if prediction[0] == 1 else "green"

            st.markdown(f"<h3 style='color:{couleur}; font-weight:bold;'>Prédiction: {resultat}</h3>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {str(e)}")

# --- VISUALISATION INTERACTIVE ---
st.subheader("Visualisation Interactive des Caractéristiques")
df_melt = input_df.melt(var_name="Caractéristique", value_name="Valeur")
chart = alt.Chart(df_melt).mark_bar().encode(
    x=alt.X("Caractéristique:N", sort=None, title="Caractéristiques"),
    y=alt.Y("Valeur:Q", title="Valeur"),
    tooltip=["Caractéristique", "Valeur"]
).properties(
    width=800,
    height=400
)
st.altair_chart(chart, use_container_width=True)

