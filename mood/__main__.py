import click
from datetime import date

@click.command()
@click.option('--rating', required=True, prompt=True, type=int)
@click.option('--comment', required=False, prompt=True, type=str)
@click.option('--date', prompt=True, required=True, type=click.DateTime(formats=["%Y-%m-%d"]),
              default=str(date.today()))
def main(rating, comment, date):
    click.echo(f"Rating of {rating} for {date} has been stored.")


if __name__ == '__main__':
    main()
