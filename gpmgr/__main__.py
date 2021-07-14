import click
from rich.console import Console

from gpmgr import util

console = Console()


@click.group()
def cli():
    pass


@cli.command('set')
@click.argument('profile-name')
@click.option('--globally', '-G', is_flag=True)
def command_set(profile_name, globally):
    profiles = util.load_conf()
    for profile in profiles:
        if profile_name == profile['name']:
            if util.change_current(profile, globally):
                console.print(f'[green]Your git profile have been changed! [blue]{profile_name}')
