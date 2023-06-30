import enumerators.Options as Options
import TaskRepository

todo_class = TaskRepository.TodoList()

menu_mapping = {
    Options.MenuOptions.ADD_TASK: {
        "Name": "Agregar Tarea",
        "Task": todo_class.add_task.__name__
    },
    Options.MenuOptions.VIEW_TRASK: {
        "Name": "Ver Tareas",
        "Task": todo_class.view_tasks.__name__
    },
    Options.MenuOptions.INSERT_TASK: {
        "Name": "Insertar Tarea",
        "Task": todo_class.insert_task.__name__
    },
    Options.MenuOptions.COPY_TASK: {
        "Name": "Duplicar Tarea",
        "Task": todo_class.duplicate_task.__name__
    },
    Options.MenuOptions.DELETE_TASK: {
        "Name": "Eliminar Tarea",
        "Task": todo_class.delete_task.__name__
    },
    Options.MenuOptions.UPDATE_TASK: {
        "Name": "Actualizar Tarea",
        "Task": todo_class.update_task.__name__
    },
    Options.MenuOptions.EXIT: {
        "Name": "Salir",
        "Task": ""
    },
}