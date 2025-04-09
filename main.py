from task_manager import TaskManager, Task

def main():
    manager = TaskManager()
    task_id_counter = max([task.task_id for task in manager.tasks], default=0) + 1

    while True:
        print("\nGestión de Tareas")
        print("1. Agregar tarea")
        print("2. Editar tarea")
        print("3. Eliminar tarea")
        print("4. Listar tareas")
        print("5. Filtrar tareas")
        print("6. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            title = input("Título: ")
            description = input("Descripción: ")
            category = input("Categoría: ")
            task = Task(task_id_counter, title, description, category)
            manager.add_task(task)
            task_id_counter += 1
            print("Tarea agregada con éxito.")

        elif choice == "2":
            task_id = int(input("ID de la tarea a editar: "))
            new_title = input("Nuevo título (dejar vacío para mantener): ")
            new_description = input("Nueva descripción (dejar vacío para mantener): ")
            new_category = input("Nueva categoría (dejar vacío para mantener): ")
            if manager.edit_task(task_id, new_title, new_description, new_category):
                print("Tarea editada con éxito.")
            else:
                print("Tarea no encontrada.")

        elif choice == "3":
            task_id = int(input("ID de la tarea a eliminar: "))
            manager.delete_task(task_id)
            print("Tarea eliminada con éxito.")

        elif choice == "4":
            print("Listado de tareas:")
            manager.list_tasks()

        elif choice == "5":
            cat = input("Categoría (dejar vacío para ignorar): ")
            status = input("Estado (Pendiente/Completada, dejar vacío para ignorar): ")
            print("Tareas filtradas:")
            filtered = manager.filter_tasks(by_category=cat or None, by_status=status or None)
            for task in filtered:
                print(task)

        elif choice == "6":
            print("Saliendo del sistema.")
            manager.save_tasks()
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
