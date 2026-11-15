# Contrat de l'API : Plateforme d'analyse automatique des sentiments

Ce document décrit les endpoints de l'API d'inférence (FastAPI).
Implémentation prévue dans SAP-39, le squelette actuel renvoie des valeurs factices.

## Conventions

- Format des échanges : JSON
- Labels possibles : `negative` (0), `neutral` (1), `positive` (2)
- `score` : score de confiance du modèle, entre 0 et 1

## 1. GET /health

Vérifie que l'API fonctionne.

**Réponse (200)**
```json
{ "status": "ok" }
```

## 2. POST /predict

Analyse le sentiment d'un seul avis.

**Requête**
```json
{ "text": "Produit excellent, livraison rapide !" }
```

**Réponse (200)**
```json
{ "label": "positive", "score": 0.94 }
```

**Erreurs**
| Code | Cas |
|---|---|
| 422 | Champ `text` manquant, vide ou trop long |

## 3. POST /predict/batch

Analyse plusieurs avis en une seule requête (import CSV côté interface).

**Requête**
```json
{ "texts": ["Très bon produit", "Décevant", "Correct sans plus"] }
```

**Réponse (200)**
```json
{
  "results": [
    { "text": "Très bon produit", "label": "positive", "score": 0.91 },
    { "text": "Décevant", "label": "negative", "score": 0.88 },
    { "text": "Correct sans plus", "label": "neutral", "score": 0.73 }
  ]
}
```

## 4. GET /history

Retourne l'historique des prédictions enregistrées (alimente le dashboard).

**Réponse (200)**
```json
{
  "items": [
    {
      "text": "Très bon produit",
      "label": "positive",
      "score": 0.91,
      "date": "2026-11-15T10:30:00"
    }
  ]
}
```

## Remarque

Ce contrat est la référence pour le frontend (SAP-43 formulaire, SAP-44 import CSV, SAP-45 dashboard)
et pour l'implémentation de l'API (SAP-39).