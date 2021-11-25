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
    ...


@cli.command()
def start():
    t = Timer()
    t.start()
    click.echo("Starting work Session")
    timer_flag = 0
    while timer_flag < 1:
        print("This prints once every 5 seconds.")
        time.sleep(5)
        timer_flag += 1

    t.stop()
    bk = Timer()
    bk.start()
    playsound('./app/alarm.mp3')
    while bk.current_time() < 57:
        print("Take a break!")
        # print(bk.current_time())

    tn = Timer()
    playsound('./app/startBeep.mp3')
    tn.start()
    click.echo("Starting Second work Session")
    timer_flag = 0
    while timer_flag < 1:
        print("This prints once every 5 seconds.")
        time.sleep(5)
        timer_flag += 1

    tn.stop()
    playsound('./app/alarm.mp3')
