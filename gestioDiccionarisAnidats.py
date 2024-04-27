diccionari = {}
type(diccionari)

print(diccionari)

paraula = "xarxa"
entrada = {
  "PESCA" : "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}

diccionari.update({paraula:entrada})

print(diccionari)

auxiliar = diccionari[paraula]

entrada = {
  "TÈXTIL" : "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà."}
  
auxiliar.update(entrada)


diccionari.update({paraula:auxiliar})

print(diccionari)

# paraules = {
  # "xarxa": {
          # "PESCA": "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o
          # rombal, anomenada malla. Són anomenades filats i, preferentment, arts.",  
          # "TÈXTIL": "Teixit de les xarxes de pescar, fabricat amb torçal de cotó o amb fil d’abacà, de cànem, de
          # lli o, modernament, de niló.",
        # },
        
        # "informàtica": {
          # "TECNOLOGIA": "Conjunt de ciències, tècniques o activitats relacionades amb el tractament
          # automatitzat de dades. Informàtica de gestió. Informàtica d’oficina.",
          # "NÚVOL": "Organització d’un sistema informàtic en què l’usuari fa ús de recursos i serveis de
          # processament i emmagatzematge de dades allotjats en servidors externs accessibles a través
          # d’internet.",
        # },
        
      # "acrònim": {
        # "NOM": "Qualsevol abreviació formada amb lletres o segments inicials o finals extrets dels mots
        # que componen una frase, que és pronunciable com un mot ordinari; per exemple, radar, làser, UNESCO,
        # etc."
  # },
# }





