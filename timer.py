import click
import time
from playsound import playsound
from app.timer import Timer


def run_timer(minutes, msg):
    t = Timer()
    t.start()
    while t.current_time() < minutes:
        click.echo(msg)
        time.sleep(1)
    t.stop()


def start_session(_s, short_breaks, focus):
    click.echo(f"Starting work Session {_s +1} of {short_breaks}")
    run_timer(focus, "Focus...")


def short_break(_s, short_breaks, short):
    playsound('./app/valarm.mp3')
    run_timer(short, "Take a short break!")
    if (_s + 1) != short_breaks:
        playsound('./app/startBeep.mp3')


def long_break(_l, long_breaks, long):
    click.echo(f'Starting long break! {_l +1} of {long_breaks}')
    run_timer(long, "Take a long break!")
    if (_l+1) != long_breaks:
        playsound('./app/startBeep.mp3')


def completed():
    click.echo("Pomodoro Completed")
    playsound('./app/falarm.mp')


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

            start_session(_s, short_breaks, focus)

            short_break(_s, short_breaks, short)

        long_break(_l, long_breaks, long)

    completed()


@cli.command()
@click.option('-bs', '--breaks', default='4', help='Number of long breaks')
def start(breaks):
    long_breaks = int(breaks)
    short_breaks = 4
    twenty_five_min = 1500
    five_min = 300

    for _l in range(long_breaks):
        for _s in range(short_breaks):

            start_session(_s, short_breaks, twenty_five_min)

            short_break(_s, short_breaks, five_min)

        long_break(_l, long_breaks, twenty_five_min)

    completed()


@cli.command()
@click.option('-m', '--minutes', default='30', help='Number of minutes')
def timer(minutes):
    run_timer(int(minutes)*60, 'Counting down...')
    playsound('./app/falarm.mp')
