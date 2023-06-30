class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def insert_task(self):
        if self.tasks is None or len(self.tasks) == 0:
            print("Para poder insertar es necesario tener tareas ya en la lista.")
            return
        
        else:
            print("Orden de tareas:")
            self.view_tasks()

            place = input("Ingrese el lugar que desea insertar la tarea: ")
            task = input("Ingrese la tarea: ")

            self.tasks.insert(int(place), task)            

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f'{index} - {task}')

    def duplicate_task(self):
        if self.tasks is None or len(self.tasks) == 0:
            print("No existen tareas para duplicar.")
            return

        print("Tareas:")
        self.view_tasks()

        place = input("Ingrese el número de la tarea que desea duplicar: ")
        task = self.tasks[int(place)]
        self.add_task(task)

    def delete_task(self, index):
        size = len(self.tasks) - 1
        if index > size:
            print("El valor ingresado no es valido.")
        else:
            del self.tasks[index]
            print("Se elimino la tarea correctamente.")
            
    def update_task(self):
        print("Elige la tarea que deseas modificar:")
        self.view_tasks()

        place = input("Ingresa el número de tarea: ")

        if int(place) > len(self.tasks):
            print("La tarea elegida no existe.")
            return

        task = input("Ingresa el nuevo contenido de la tarea: ")

        self.tasks[int(place)] = task

def main():
    todo_list = TodoList()
    while True:
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Insertar tarea")
        print("4. Duplicar tarea")
        print("5. Eliminar tarea")
        print("6. Actualizar una tarea")
        print("7. Salir")

        option = input("Seleccione una opción: ")
        if option == "1":
            task = input("Ingrese la tarea: ")
            todo_list.add_task(task)
        elif option == "2":
            todo_list.view_tasks()
        elif option == "3":
            todo_list.insert_task()
        elif option == "4":
            todo_list.duplicate_task()
        elif option == "5":
            todo_list.view_tasks()
            toDelete = input("Ingrese el numero de tarea a eliminar.")
            try:
                index = int(toDelete)
                todo_list.delete_task(index)
            except ValueError:
                print("La opcion ingresada tiene que ser un numero.")
        elif option == "6":
            todo_list.update_task()
        elif option == "7":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
