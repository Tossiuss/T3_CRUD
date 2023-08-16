import datetime

def log_activity(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Выполнено: {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper



class Task:
    def __init__(self, task, description, status=False):
        self.task = task
        self.description = description
        self.status = status
        self.creation_date = datetime.datetime.now()

    @log_activity
    def mark_as_done(self):
        self.status = True

    @log_activity
    def mark_as_undone(self):
        self.status = False

    @log_activity
    def edit_description(self, new_description):
        self.description = new_description

    def __str__(self):
        status_str = "выполнено" if self.status else "не выполнено"
        return f"Пункт: {self.task}\nОписание: {self.description}\nСтатус: {status_str}\nДата создания: {self.creation_date}"



class TaskList:
    def __init__(self):
        self.tasks = []

    @log_activity
    def create_task(self, task, description):
        new_task = Task(task, description)
        self.tasks.append(new_task)

    @log_activity
    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            return None

    @log_activity
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    @log_activity
    def get_all_tasks(self):
        return self.tasks

    def __len__(self):
        return len(self.tasks)



if __name__ == "__main__":
    task_list = TaskList()



    task_list.create_task("Makers", "Прийти на лекцию")
    task_list.create_task("Спорт", "Сделать зарядку")
    task_list.create_task("Дом", "Прибраться дома")

    task_list.get_task(0).mark_as_done()
    task_list.get_task(1).mark_as_undone()
    task_list.get_task(1).edit_description("Сходить в спортзал")
    task_list.get_task(2).mark_as_done()

    print("\nСписок всех задач:")
    for idx, task in enumerate(task_list.get_all_tasks()):
        print(f"\nЗадача {idx + 1}:\n{task}")

# В requirements.txt записал библиотеку datetime