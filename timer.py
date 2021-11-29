import click
from app.application import run_timer, start_session, short_break, long_break, completed


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
    completed()


@cli.command()
def hour():
    run_timer(60*60, 'Counting down...')
    completed()


@cli.command()
def half():
    run_timer(30*60, 'Counting down...')
    completed()
