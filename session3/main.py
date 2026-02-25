from dataclasses import dataclass
from typer import Typer, echo,style,colors
from datetime import datetime  



@dataclass
class Meeting:
    title: str
    owner: str
    date: str



cli = Typer()

@cli.command()
def greetings(name: str = "", surname: str = ""):
    echo(style(f"Greetings {name} {surname}", fg=colors.BLUE))



@cli.command()
def goodbye():
    echo(style("Goodbye", fg=colors.RED))


@cli.command()
def create_meeting(meeting: Meeting):
    """
    Command to create a new meeting note.
    """
    echo(style(f"""
    ============================
         {meeting.title}
    ============================
    
   created by {meeting.owner} on {meeting.date} 
   """,fg=colors.BRIGHT_CYAN, bold=True))

if __name__ == "__main__":
    cli()


