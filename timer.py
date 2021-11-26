import click
import time
from playsound import playsound
from app.timer import Timer


@click.group()
def cli():
    pass


@cli.command()
@click.option('-f', '--focus', default="25", help='Time between breaks in minutes')
@click.option('-s', '--short', default="5", help='Short break length in minutes')
@click.option('-l', '--long', default="25", help='Long break taken after 4 focus+short pomodoro intervals in minutes')
@click.option('-bs', '--breaks', default='4', help='Number of long breaks in minutes')
def custom(focus, short, long, breaks):

    long_breaks = int(breaks)
    short_breaks = 4
    focus = int(focus)*60
    short = int(short)*60
    long = int(long)*60

    for _l in range(long_breaks):
        for _s in range(short_breaks):

            t = Timer()
            t.start()
            click.echo(f"Starting work Session {_s +1} of {short_breaks}")
            while t.current_time() < focus:
                print("Focus...")
                time.sleep(1)
            t.stop()

            bk = Timer()
            bk.start()
            playsound('./app/valarm.mp3')
            while bk.current_time() < short:
                print("Take a short break!")
                time.sleep(1)
            if (_s + 1) != short_breaks:
                playsound('./app/startBeep.mp3')
            bk.stop()

        click.echo(f'Starting long break! {_l +1} of {long_breaks}')
        lb = Timer()
        lb.start()
        while lb.current_time() < long:
            print("Take a long break!")
        if (_l+1) != long_breaks:
            playsound('./app/startBeep.mp3')
        lb.stop()

    click.echo("Pomodoro Completed")
    playsound('./app/falarm.mp')


@cli.command()
@click.option('-bs', '--breaks', default='4', help='Number of long breaks')
def start(breaks):
    long_breaks = int(breaks)
    short_breaks = 4
    twenty_five_min = 1500
    five_min = 300

    for _l in range(long_breaks):
        for _s in range(short_breaks):

            t = Timer()
            t.start()
            click.echo(f"Starting work Session {_s +1} of {short_breaks}")
            while t.current_time() < twenty_five_min:
                print("Focus...")
                time.sleep(1)
            t.stop()

            bk = Timer()
            bk.start()
            playsound('./app/valarm.mp3')
            while bk.current_time() < five_min:
                print("Take a short break!")
                time.sleep(1)
            if (_s + 1) != short_breaks:
                playsound('./app/startBeep.mp3')
            bk.stop()

        click.echo(f'Starting long break! {_l +1} of {long_breaks}')
        lb = Timer()
        lb.start()
        while lb.current_time() < twenty_five_min:
            print("Take a long break!")
        if (_l+1) != long_breaks:
            playsound('./app/startBeep.mp3')
        lb.stop()

    click.echo("Pomodoro Completed")
    playsound('./app/falarm.mp')
