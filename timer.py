import click
import time
from playsound import playsound
from app.timer import Timer


@click.group()
def cli():
    pass


@cli.command()
@click.option('-f', '--focus', default="25", help='Time between breaks')
@click.option('-s', '--short', default="5", help='Short break length')
@click.option('-l', '--long', default="25", help='Long preak taken after 4 focus+short pomodoro intervals.')
def custom(focus, short, long):
    click.echo(f'Focus: {focus}')
    click.echo(f'Short: {short}')
    click.echo(f'Long: {long}')


@cli.command()
def start():
    long_breaks = 4
    short_breaks = 4

    for _l in range(long_breaks):
        for _s in range(short_breaks):
            t = Timer()
            t.start()
            click.echo(f"Starting work Session {_s +1} of {short_breaks}")
            timer_flag = 0
            while timer_flag < 1:
                print("This prints once every 5 seconds.")
                time.sleep(5)
                timer_flag += 1

            t.stop()
            bk = Timer()
            bk.start()
            playsound('./app/valarm.mp3')
            while bk.current_time() < 17:
                print("Take a short break!")
            playsound('./app/startBeep.mp3')

        playsound('./app/lalarm.mp3')
        click.echo(f'Starting long break! {_l +1} of {long_breaks}')
        lb = Timer()
        lb.start()
        playsound('./app/valarm.mp3')
        while lb.current_time() < 27:
            print("Take a long break!")
        playsound('./app/startBeep.mp3')
