import TaskRepository
import Menu
import Options

def main():
    todo_list = TaskRepository.TodoList()
    while True:

        print("\n")

        for option, data in Menu.menu_mapping.items():
            print(f"{option.value}. {data['Name']}")

        print("\n")

        try:
            user_choice = int(input("Seleccione una opción: "))
            print("\n")
            selected_option = Options.MenuOptions(user_choice)
        except ValueError:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue
        except KeyError:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue

        if selected_option == Options.MenuOptions.EXIT:
            print("Saliendo del programa...")
            break

        selected_task = Menu.menu_mapping[selected_option]["Task"]

        if selected_task:
            task_method = getattr(todo_list, selected_task)
            task_method()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
