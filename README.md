# 📝 Python Task CLI

Un gestionnaire de tâches en ligne de commande écrit en Python pur

---

## ✨ Fonctionnalités

- Ajouter une tâche
- Lister toutes les tâches
- Marquer une tâche comme terminée
- Supprimer une tâche
- Persistance des données en JSON
- Gestion des erreurs et validation des entrées

---

## 🛠️ Stack technique

- Python 3.13
- `argparse` — interface en ligne de commande
- `uuid` — génération d'identifiants uniques
- `json` — persistance des données
- `dataclasses` — modélisation des données
- `datetime` — horodatage des tâches

---

```
python-task-cli/
│
├── task_manager/
│   ├── __init__.py
│   ├── task.py          # Modèle de données Task
│   ├── task_manager.py  # Logique métier (CRUD)
│   └── storage.py       # Persistance JSON
│
├── data/
│   └── tasks.json       # Données sauvegardées
│
├── main.py              # Point d'entrée CLI
└── README.md
```

---

## 💡 Concepts pratiqués

- Programmation orientée objet
- Dataclasses et sérialisation
- Gestion de fichiers JSON
- Interface CLI avec `argparse`
- Gestion des erreurs
- Bonne structure de projet Python
- Conventional Commits

---

## ⚙️ Installation
- git clone https://github.com/FerrandBen/python-task-cli
- Créer et activer le venv
- Aucune dépendance externe requise

---

## 🚀 Utilisation

- python main.py add "Ma tâche"
- python main.py list
- python main.py done <id>
- python main.py delete <id>