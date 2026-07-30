import streamlit as st

# --------------------------------------------------
# CONFIGURAZIONE PAGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Inclusione e Rispetto",
    page_icon="🤝",
    layout="wide"
)

# --------------------------------------------------
# TITOLI
# --------------------------------------------------

st.title("🤝 Inclusione e Rispetto")
st.subheader("Survey preliminare")

st.markdown("""
Quanto sei d’accordo con le seguenti 20 affermazioni?

Scala di valutazione:

- Per niente
- Poco
- Abbastanza
- Molto
- Del tutto
""")

# --------------------------------------------------
# SCALA
# --------------------------------------------------

scala = {
    "Per niente": 1,
    "Poco": 2,
    "Abbastanza": 3,
    "Molto": 4,
    "Del tutto": 5
}

opzioni = list(scala.keys())

# --------------------------------------------------
# BLOCCO A
# --------------------------------------------------

st.header("A - Io: consapevolezza e confini")

A1 = scala[st.radio(
    "1. Conosco e so nominare i valori che guidano le mie scelte al lavoro.",
    opzioni,
    key="A1"
)]

A2 = scala[st.radio(
    "2. So dire no quando qualcosa supera i miei confini o priorità.",
    opzioni,
    key="A2"
)]

A3 = scala[st.radio(
    "3. Spiego i miei confini con chiarezza e senza senso di colpa.",
    opzioni,
    key="A3"
)]

A4 = scala[st.radio(
    "4. Prendo decisioni senza lasciarmi guidare dal bisogno di approvazione.",
    opzioni,
    key="A4"
)]

A5 = scala[st.radio(
    "5. Prima di reagire, mi prendo tempo per riflettere.",
    opzioni,
    key="A5"
)]

# --------------------------------------------------
# BLOCCO B
# --------------------------------------------------

st.header("B - Relazione 1:1")

B1 = scala[st.radio(
    "6. Evito di attribuire i comportamenti principalmente all’età; cerco altre spiegazioni.",
    opzioni,
    key="B1"
)]

B2 = scala[st.radio(
    "7. Ascolto colleghi di altre età con curiosità e senza interrompere.",
    opzioni,
    key="B2"
)]

B3 = scala[st.radio(
    "8. Evito etichette 'noi/loro' e uso un linguaggio inclusivo.",
    opzioni,
    key="B3"
)]

B4 = scala[st.radio(
    "9. Faccio domande per capire prima di valutare.",
    opzioni,
    key="B4"
)]

B5 = scala[st.radio(
    "10. Riconosco e valorizzo contributi diversi dai miei.",
    opzioni,
    key="B5"
)]

# --------------------------------------------------
# BLOCCO C
# --------------------------------------------------

st.header("C - Team / Gruppo")

C1 = scala[st.radio(
    "11. Nei meeting c’è spazio e tempo per ogni voce, a prescindere dall’età.",
    opzioni,
    key="C1"
)]

C2 = scala[st.radio(
    "12. Nessuno deve recitare una parte per sentirsi accettato nel team.",
    opzioni,
    key="C2"
)]

C3 = scala[st.radio(
    "13. Prima di giudicare, dedichiamo tempo a fare domande chiarificatrici.",
    opzioni,
    key="C3"
)]

C4 = scala[st.radio(
    "14. Affrontiamo e risolviamo le tensioni legate all’età invece di evitarle.",
    opzioni,
    key="C4"
)]

C5 = scala[st.radio(
    "15. Abbiamo regole condivise per collaborare in modo inclusivo.",
    opzioni,
    key="C5"
)]

# --------------------------------------------------
# BLOCCO D
# --------------------------------------------------

st.header("D - Organizzazione / Azienda")

D1 = scala[st.radio(
    "16. Manager e Team Leader mostrano rispetto e curiosità, non giudizio.",
    opzioni,
    key="D1"
)]

D2 = scala[st.radio(
    "17. Le decisioni tengono conto di prospettive di età diverse senza avvantaggiare sempre gli stessi.",
    opzioni,
    key="D2"
)]

D3 = scala[st.radio(
    "18. Posso esprimere dubbi o dissentire senza timore di conseguenze.",
    opzioni,
    key="D3"
)]

D4 = scala[st.radio(
    "19. Le priorità e i criteri decisionali sono chiari e coerenti.",
    opzioni,
    key="D4"
)]

D5 = scala[st.radio(
    "20. È legittimo dire 'non fa per me' o chiedere alternative senza penalità.",
    opzioni,
    key="D5"
)]

# --------------------------------------------------
# CALCOLO
# --------------------------------------------------

blocco_a = A1+A2+A3+A4+A5
blocco_b = B1+B2+B3+B4+B5
blocco_c = C1+C2+C3+C4+C5
blocco_d = D1+D2+D3+D4+D5

totale = (
    blocco_a +
    blocco_b +
    blocco_c +
    blocco_d
)

# --------------------------------------------------
# PROFILI
# --------------------------------------------------

def profilo(score):

    if score <= 39:
        return "Poco inclusivo"

    elif score <= 59:
        return "In avvio"

    elif score <= 79:
        return "Inclusivo"

    else:
        return "Molto inclusivo"


# --------------------------------------------------
# RISULTATO
# --------------------------------------------------

if st.button("📊 Calcola il mio risultato"):

    st.success("Questionario completato!")

    st.metric(
        "Punteggio Totale",
        f"{totale}/100"
    )

    st.metric(
        "Profilo",
        profilo(totale)
    )

    st.divider()

    st.subheader("Punteggi per area")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Blocco A", f"{blocco_a}/25")

    with col2:
        st.metric("Blocco B", f"{blocco_b}/25")

    with col3:
        st.metric("Blocco C", f"{blocco_c}/25")

    with col4:
        st.metric("Blocco D", f"{blocco_d}/25")

    blocchi = {
        "A - Io": blocco_a,
        "B - Relazione 1:1": blocco_b,
        "C - Team": blocco_c,
        "D - Organizzazione": blocco_d
    }

    blocco_debole = min(blocchi, key=blocchi.get)

    st.warning(
        f"Area prioritaria di miglioramento: {blocco_debole}"
    )

    # Suggerimenti sintetici

    if blocco_debole.startswith("A"):
        st.info(
            "Lavora su consapevolezza personale, valori e capacità di comunicare i tuoi confini."
        )

    elif blocco_debole.startswith("B"):
        st.info(
            "Allenati nell'ascolto attivo, nella curiosità e nel non giudizio."
        )

    elif blocco_debole.startswith("C"):
        st.info(
            "Favorisci pratiche di team inclusive e una maggiore partecipazione alle decisioni."
        )

    else:
        st.info(
            "Promuovi maggiore trasparenza, sicurezza psicologica e inclusione organizzativa."
        )
