from Task import Task
from enumerators.Status import Status
from mappings.Status import status_mapping
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, newTask = ""):
        task_name = newTask if newTask != "" else input("Ingrese la tarea: ")
        self.tasks.append(Task(task_name, Status.PENDING))

    def insert_task(self):
        if self.tasks is None or len(self.tasks) == 0:
            print("Para poder insertar es necesario tener tareas ya en la lista.")
            return
        
        else:
            print("Orden de tareas:")
            self.view_tasks()

            place = input("Ingrese el lugar que desea insertar la tarea: ")
            task_name = input("Ingrese la tarea: ")

            self.tasks.insert(int(place), Task(task_name,  Status.PENDING))            

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f'{index} - {task.name} - {status_mapping.get(task.status)["Name"]}')

    def duplicate_task(self):
        if self.tasks is None or len(self.tasks) == 0:
            print("No existen tareas para duplicar.")
            return

        print("Tareas:")
        self.view_tasks()

        place = input("Ingrese el número de la tarea que desea duplicar: ")
        task = self.tasks[int(place)]
        self.tasks.append(task)

    def delete_task(self):
        self.view_tasks()
        toDelete = input("Ingrese el numero de tarea a eliminar.")
        try:
            index = int(toDelete)
            size = len(self.tasks) - 1
            if index > size:
                print("El valor ingresado no es valido.")
            else:
                del self.tasks[index]
                print("Se elimino la tarea correctamente.")
        except ValueError:
            print("La opcion ingresada tiene que ser un numero.")

    def update_task(self):
        print("Elige la tarea que deseas modificar:")
        self.view_tasks()

        place = input("Ingresa el número de tarea: ")

        if int(place) > len(self.tasks):
            print("La tarea elegida no existe.")
            return

        print("1. Modificar nombre")
        print("2. Modificar estado")
        selected_option = int(input("Ingresa el número del dato que desea modificar: "))

        if selected_option == 1:
            task_name = input("Ingresa el nuevo nombre de la tarea: ")
            self.tasks[int(place)].name = task_name
        elif selected_option == 2:
            while True:
                print("Estados posibles")
                for option, data in status_mapping.items():
                    print(f"{option.value}. {data['Name']}")

                try:    
                    user_choice = int(input("A que estado desea actualizar: "))
                    print("\n")
                    selected_status = Status(user_choice)
                except ValueError:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
                    continue
                except KeyError:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
                    continue
                
                self.tasks[int(place)].status = selected_status
                break