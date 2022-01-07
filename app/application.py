import click
import time
from app.timer import Timer
from playsound import playsound


def run_timer(minutes, msg):
    t = Timer()
    t.start()
    while t.current_time() < minutes:
        click.echo(f"{int(t.current_time())}: {msg}")
        time.sleep(1)
    t.stop()


def start_session(_s, short_breaks, focus):
    click.echo(f"Starting work Session {_s +1} of {short_breaks}")
    run_timer(focus, "Focus...")


def short_break(_s, short_breaks, short):
    playsound('app/valarm.mp3')
    click.echo(f'Starting long break! {_s +1} of {short_breaks}')
    run_timer(short, "Take a short break!")
    if (_s + 1) != short_breaks:
        playsound('app/startBeep.mp3')


def long_break(_l, long_breaks, long):
    click.echo(f'Starting long break! {_l +1} of {long_breaks}')
    run_timer(long, "Take a long break!")
    if (_l+1) != long_breaks:
        playsound('app/startBeep.mp3')


def completed():
    click.echo("Doro Completed")
    playsound('app/valarm.mp3')
