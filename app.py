import streamlit as st

# ==================================================
# CONFIGURAZIONE
# ==================================================

st.set_page_config(
    page_title="Inclusione e Rispetto",
    page_icon="🤝",
    layout="wide"
)

# ==================================================
# COPERTINA
# ==================================================

st.image("images/cover.png", use_container_width=True)

st.title("🤝 Inclusione e Rispetto")
st.subheader("Survey preliminare")

st.markdown("""
Questa survey ha l'obiettivo di esplorare il livello di inclusione,
rispetto e collaborazione intergenerazionale.

Per ogni affermazione scegli il livello che meglio rappresenta la tua esperienza.

### Scala di valutazione

- Per niente = 1
- Poco = 2
- Abbastanza = 3
- Molto = 4
- Del tutto = 5
""")

# ==================================================
# SCALA
# ==================================================

scala = {
    "Per niente": 1,
    "Poco": 2,
    "Abbastanza": 3,
    "Molto": 4,
    "Del tutto": 5
}

# ==================================================
# QUESTIONARIO
# ==================================================

questionario = {

    "A - Io: Consapevolezza e Confini": {

        "immagine": "images/blocco_a.png",

        "descrizione": """
Conoscere sé stessi è il primo passo verso relazioni inclusive.
Questa sezione esplora valori personali, confini e capacità di riflessione.
""",

        "domande": [

            "Conosco e so nominare i valori che guidano le mie scelte al lavoro.",

            "So dire no quando qualcosa supera i miei confini o priorità.",

            "Spiego i miei confini con chiarezza e senza senso di colpa.",

            "Prendo decisioni senza lasciarmi guidare dal bisogno di approvazione.",

            "Prima di reagire, mi prendo tempo per riflettere."
        ]
    },

    "B - Tu: Ascolto e Non Giudizio": {

        "immagine": "images/blocco_b.png",

        "descrizione": """
L'ascolto autentico e la curiosità permettono di
comprendere prospettive differenti e superare stereotipi.
""",

        "domande": [

            "Evito di attribuire i comportamenti principalmente all'età; cerco altre spiegazioni.",

            "Ascolto colleghi di altre età con curiosità e senza interrompere.",

            "Evito etichette 'noi/loro' e uso un linguaggio inclusivo.",

            "Faccio domande per capire prima di valutare.",

            "Riconosco e valorizzo contributi diversi dai miei."
        ]
    },

    "C - Noi: Collaborazione e Decisioni Inclusive": {

        "immagine": "images/blocco_c.png",

        "descrizione": """
L'inclusione si manifesta nella qualità delle relazioni
e nella partecipazione alle decisioni del team.
""",

        "domande": [

            "Nei meeting c'è spazio e tempo per ogni voce, a prescindere dall'età.",

            "Nessuno deve recitare una parte per sentirsi accettato nel team.",

            "Prima di giudicare dedichiamo tempo a fare domande chiarificatrici.",

            "Affrontiamo e risolviamo le tensioni legate all'età invece di evitarle.",

            "Abbiamo regole condivise per collaborare in modo inclusivo."
        ]
    },

    "D - Azienda: Clima di Cooperazione Intergenerazionale": {

        "immagine": "images/blocco_d.png",

        "descrizione": """
La cultura organizzativa e le pratiche aziendali
possono favorire o ostacolare l'inclusione.
""",

        "domande": [

            "Manager e Team Leader mostrano rispetto e curiosità, non giudizio.",

            "Le decisioni tengono conto di prospettive di età diverse senza favorire sempre gli stessi.",

            "Posso esprimere dubbi o dissentire senza timore di conseguenze.",

            "Le priorità e i criteri decisionali sono chiari e coerenti.",

            "È legittimo dire 'non fa per me' o chiedere alternative senza penalità."
        ]
    }
}

# ==================================================
# GENERAZIONE DINAMICA
# ==================================================

risultati_blocchi = {}
numero_domanda = 1

for nome_blocco, dati in questionario.items():

    st.divider()

    st.image(
        dati["immagine"],
        width=180
    )

    st.header(nome_blocco)

    st.markdown(dati["descrizione"])

    totale_blocco = 0

    for domanda in dati["domande"]:

        risposta = st.radio(
            f"{numero_domanda}. {domanda}",
            list(scala.keys()),
            horizontal=True,
            key=f"Q{numero_domanda}"
        )

        totale_blocco += scala[risposta]

        numero_domanda += 1

    risultati_blocchi[nome_blocco] = totale_blocco

# ==================================================
# PROFILI
# ==================================================

def profilo(score):

    if score <= 39:
        return "Poco inclusivo"

    elif score <= 59:
        return "In avvio"

    elif score <= 79:
        return "Inclusivo"

    else:
        return "Molto inclusivo"

# ==================================================
# DESCRIZIONI PROFILI
# ==================================================

descrizioni_profili = {

    "Poco inclusivo":
    """
### Poco inclusivo (0-39)

Pratiche e comportamenti inclusivi non sono ancora stabili.

La priorità è costruire basi solide:
- ascolto
- rispetto reciproco
- chiarezza nei confini
- collaborazione
- sicurezza psicologica
""",

    "In avvio":
    """
### In avvio (40-59)

Sono presenti buone intenzioni e primi comportamenti inclusivi,
ma l'applicazione è ancora discontinua.

L'obiettivo è trasformare le buone intenzioni
in comportamenti abituali.
""",

    "Inclusivo":
    """
### Inclusivo (60-79)

La cultura inclusiva è ben presente.

Le persone ascoltano, collaborano e valorizzano le differenze.

Occorre consolidare le pratiche più efficaci
e ridurre eventuali aree di fragilità.
""",

    "Molto inclusivo":
    """
### Molto inclusivo (80-100)

Il livello di inclusione è elevato e diffuso.

La cultura di rispetto e cooperazione è consolidata.

L'obiettivo è mantenere questi risultati e diventare modello positivo per gli altri.
"""
}

# ==================================================
# RISULTATI
# ==================================================

if st.button("📊 Visualizza il risultato"):

    totale = sum(risultati_blocchi.values())

    st.divider()

    st.success("Questionario completato")

    st.metric(
        "Punteggio Totale",
        f"{totale}/100"
    )

    profilo_finale = profilo(totale)

    st.metric(
        "Profilo",
        profilo_finale
    )

    # Descrizione profilo
    st.markdown(descrizioni_profili[profilo_finale])

    st.divider()

    st.subheader("Dettaglio per area")

    col1, col2 = st.columns(2)

    elementi = list(risultati_blocchi.items())

    with col1:
        st.metric(elementi[0][0], f"{elementi[0][1]}/25")
        st.metric(elementi[1][0], f"{elementi[1][1]}/25")

    with col2:
        st.metric(elementi[2][0], f"{elementi[2][1]}/25")
        st.metric(elementi[3][0], f"{elementi[3][1]}/25")

    area_debole = min(
        risultati_blocchi,
        key=risultati_blocchi.get
    )

    st.warning(
        f"Area prioritaria di sviluppo: {area_debole}"
    )
