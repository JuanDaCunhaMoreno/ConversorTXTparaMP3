import pyttsx3

def criar_engine(voz_tipo="feminina", velocidade=1.0, texto="Teste de voz Python"):
    engine = pyttsx3.init()
    vozes = engine.getProperty('voices')

    # Definir voz
    if voz_tipo == "feminina":
        engine.setProperty('voice', vozes[0].id)
    else:
        engine.setProperty('voice', vozes[1].id)

    # Definir velocidade (rate)
    taxa_base = engine.getProperty('rate')  # padrão: geralmente 200
    nova_taxa = int(taxa_base * velocidade)
    engine.setProperty('rate', nova_taxa)

    engine.say(texto)
    engine.runAndWait()

    return engine
