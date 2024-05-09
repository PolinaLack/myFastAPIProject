from typing import Annotated, Any

from fastapi import FastAPI, Path
from models import TaskCreate, TaskPatch, Task

app = FastAPI()


users_tasks: dict[int, Task] = {
    1: Task(**{
        "id": 1,
        "name": "Task1",
        "description": "To do something important",
        "completed": False,
    }),
    2: Task(**{
        "id": 2,
        "name": "Task2",
        "description": "To do something important too",
        "completed": False,
    }),
}


@app.get(path="/tasks")
def get_all_tasks() -> list[Task]:
    res = list(users_tasks.values())
    return res


@app.post(path="/tasks")
def post_new_task(user_task: TaskCreate) -> dict:
    users_tasks[max(users_tasks.keys()) + 1] = user_task.model_dump()
    # выбираем ключ через max, чтобы нечайно не перезаписывать данные
    return users_tasks


@app.delete(path="/tasks/{task_id}")
def delete_task(task_id: Annotated[int, Path()]) -> dict[int, dict[str, object]]:
    del users_tasks[task_id]
    return users_tasks


@app.put(path="/tasks/{task_id}")
def update_task(
    task_id: Annotated[int, Path()], user_task: TaskCreate
) -> dict[int, dict[str, object]]:
    users_tasks[task_id] = user_task.model_dump()
    return users_tasks


@app.patch(path="/tasks/{task_id}")
def update_part_task(
    task_id: Annotated[int, Path()], user_task: Annotated[TaskPatch, None]
) -> dict[int, dict[str, object]]:
    temp: dict[str, Any] = user_task.model_dump()
    for key, value in temp.items():
        if value is not None:
            users_tasks[task_id][key] = value
    return users_tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, reload=False)
