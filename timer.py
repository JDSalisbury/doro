import click
import time
from playsound import playsound
import timer


@click.group()
def cli():
    pass


@cli.command()
def start():
    click.echo("Starting")
    timer_flag = 0
    while timer_flag < 1:
        print("This prints once every 5 seconds.")
        time.sleep(5)
        timer_flag += 1

    playsound('./app/alarm.mp3')
