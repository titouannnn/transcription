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
