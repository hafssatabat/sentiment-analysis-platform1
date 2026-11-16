# Plateforme d'analyse automatique des sentiments

## 1. Présentation du projet

Ce projet consiste à développer une plateforme web d'analyse automatique des sentiments basée sur le traitement automatique du langage naturel (NLP), le Machine Learning et le Deep Learning.

La plateforme permettra d'analyser des avis clients rédigés en français et de les classifier en trois catégories :

- **Positif**
- **Neutre**
- **Négatif**

Ce projet est réalisé dans le cadre des travaux pratiques de DevOps à l'ENSA Khouribga, année universitaire 2026-2027.

## 2. Objectifs du projet

- Collecter et préparer des données textuelles issues d'avis clients.
- Effectuer le prétraitement des textes.
- Développer et comparer plusieurs modèles de classification : TF-IDF + SVM, LSTM et CamemBERT.
- Développer une API REST pour exploiter le modèle de prédiction.
- Créer une interface web permettant de saisir un avis et de visualiser le sentiment détecté.
- Mettre en place un workflow collaboratif avec Git, GitHub et Jira.
- Préparer l'automatisation et le déploiement avec les outils MLOps.

## 3. Technologies envisagées

- **Langage :** Python
- **Machine Learning :** Scikit-learn
- **Deep Learning :** PyTorch, Hugging Face Transformers
- **Traitement du langage naturel :** NLP, CamemBERT
- **Backend :** FastAPI
- **Versionnement :** Git et GitHub
- **Gestion de projet :** Jira (Scrum)
- **MLOps :** MLflow, DVC
- **Déploiement et automatisation :** Docker, GitHub Actions

## 4. Structure du projet

```text
sentiment-analysis-platform/
├── src/
│   ├── data/
│   └── models/
├── data/
├── models/
├── notebooks/
├── tests/
├── docs/
├── api/
├── frontend/
├── README.md
└── .gitignore
```

## 5. Membres de l'équipe

| Membre | Rôle |
|---|---|
| Fatima Chamani | Cheffe de projet / ML Engineer |
| Zeroual Assiya | Data Engineer / NLP |
| Tabat Hafssa | Backend & DevOps |
| Elmenhi Ikram | Frontend & Scrum Master |

## 6. Organisation collaborative

Le projet est développé de manière collaborative avec Git et GitHub.

Chaque membre travaille sur une branche dédiée à sa tâche Jira. Les modifications sont ensuite intégrées à la branche principale `main` à travers des Pull Requests, après une revue de code par un autre membre de l'équipe.
## Collaboration

Ce projet est développé en équipe avec Git et GitHub.

## Organisation du projet

Le développement est organisé en branches de fonctionnalités.
Les modifications sont examinées au moyen de Pull Requests.