class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        numeroTarea = 0
        for task in self.tasks:
            print(f'{numeroTarea} - {task}')
            numeroTarea += 1

    def delete_task(self, index):
        size = len(self.tasks) - 1
        if index > size:
            print("El valor ingresado no es valido.")
        else:
            del self.tasks[index]
            print("Se elimino la tarea correctamente.")

def main():
    todo_list = TodoList()
    while True:
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            task = input("Ingrese la tarea: ")
            todo_list.add_task(task)
        elif option == "2":
            todo_list.view_tasks()
        elif option == "3":
            todo_list.view_tasks()
            toDelete = input("Ingrese el numero de tarea a eliminar.")
            try:
                index = int(toDelete)
                todo_list.delete_task(index)
            except ValueError:
                print("La opcion no es valida.")
        elif option == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

main()