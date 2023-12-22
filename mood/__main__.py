import click

@click.command()
@click.option('--rating', prompt=True, type=int)
@click.option('--comment', prompt=True, type=str)
def main(rating, comment):
    click.echo("Rating for today has been stored.")


if __name__ == '__main__':
    main()
