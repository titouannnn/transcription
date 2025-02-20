# Transcription  

## Installation des dépendances  

Avant de lancer l'application, assurez-vous d'installer les dépendances requises :  

```bash
pip install -r requirements.txt
```  

De plus, vous devez installer `ffmpeg` si ce n'est pas déjà fait 


## Lancement de l'interface  

Pour lancer l'interface, exécutez la commande suivante :  

```bash
streamlit run app.py
```  

## Utilisation avec Docker  

### Construire l'image Docker  
```bash
docker build -t transcription-app .
```  

### Lancer le conteneur  
```bash
docker run -p 8501:8501 transcription-app
```  

Si il n'y a rien sur l'adresse affichée dans le terminal, vous pouvez vous rendre à l'adresse suivante (l'adresse http://0.0.0.0:8501 marche sous linux mais pas sous windows) :
```bash
http://127.0.0.1:8501/
```
