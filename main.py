from task_manager.task_manager import Task_manager
from task_manager.storage import save_tasks, load_tasks
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple Task Manager")
    parser.add_argument(
        "choix", choices=["add", "list", "done", "delete"], help="Choix possibles"
    )
    parser.add_argument("valeur", nargs="?", help="Titre ou id selon la commande")
    args = parser.parse_args()

    manager = Task_manager()
    manager.task_list = load_tasks()
    if args.choix == "add":
        result = manager.add_task(args.valeur)
        save_tasks(manager.task_list)
        print("La tâche a bien été ajoutée")
    elif args.choix == "list":
        print("Voici la liste des tâches :")
        result = manager.show_tasks()
        for task in manager.show_tasks():
            print(task)
    elif args.choix == "done":
        result = manager.search_by_id(args.valeur)
        result.mark_as_done()
        print("La tâche a bien été marqué comme terminé")
        save_tasks(manager.task_list)
    elif args.choix == "delete":
        result = manager.delete_task(args.valeur)
        save_tasks(manager.task_list)
        print("La tâche a bien été supprimée")
