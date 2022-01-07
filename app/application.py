import click
import time
from app.timer import Timer
from playsound import playsound

SHORT_ALARM = 'app/alarms/sbalarm.mp3'
START_ALARM = 'app/alarms/stalarm.mp3'
END_ALARM = 'app/alarms/endalarm.mp3'


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
    playsound(SHORT_ALARM)
    click.echo(f'Starting long break! {_s +1} of {short_breaks}')
    run_timer(short, "Take a short break!")
    if (_s + 1) != short_breaks:
        playsound(START_ALARM)


def long_break(_l, long_breaks, long):
    click.echo(f'Starting long break! {_l +1} of {long_breaks}')
    run_timer(long, "Take a long break!")
    if (_l+1) != long_breaks:
        playsound(START_ALARM)


def completed():
    click.echo("Doro Completed")
    playsound(END_ALARM)
