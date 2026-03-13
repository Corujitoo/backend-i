from typer import Typer
import uvicorn
from src.api.main import api



cli = Typer()

@cli.command()
def run():
    uvicorn.run(api, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    cli()
