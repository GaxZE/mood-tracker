import typer

def main():
    rating = typer.prompt("Please give yesterday a rating from 1 to 5 of how your day was yesterday")
    print(f"You rated yesterday: {rating}")


if __name__ == "__main__":
    typer.run(main)
