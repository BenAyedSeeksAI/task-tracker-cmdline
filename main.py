import typer
from rich.console import Console
from rich.table import Table
from models import Task

cnsle = Console()
app = typer.Typer()

tasks = [("start writing markdowns","work related"),("update github","work related")]


def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'work related': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

def formatTable():
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("id", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    return table

@app.command(short_help = "add a task")
def add(task: str, category: str):
    typer.echo(f"adding task -{task}- of category -{category}-")
    oneTask = Task(task,category)
    oneTask.save()
    

@app.command(short_help= 'show all tasks')
def show():
    cnsle.print("[bold magenta]Todos[/bold magenta]!", "💻")
    table = formatTable()
    for idx, data in enumerate(tasks, start= 1):
        color = get_category_color(data[1])
        table.add_row(str(idx),
                      data[0],
                      f"[{color}]{data[1]}[/{color}]"
                      )
    cnsle.print(table)

if __name__ == "__main__":
    app()