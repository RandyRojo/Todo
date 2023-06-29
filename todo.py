class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self):
        print("Elige la tarea que deseas modificar:")
        self.view_tasks()

        place = input("Ingresa el número de tarea: ")

        if int(place) -1 > len(self.tasks):
            print("La tarea elegida no existe.")
            return

        task = input("Ingresa el nuevo contenido de la tarea: ")

        self.tasks[int(place) - 1] = task

def main():
    todo_list = TodoList()
    while True:
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Actualizar tarea")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            task = input("Ingrese la tarea: ")
            todo_list.add_task(task)
        elif option == "2":
            todo_list.view_tasks()
        elif option == "3":
            todo_list.update_task()
        elif option == "4":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()