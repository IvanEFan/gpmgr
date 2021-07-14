from gpmgr import constant

import json
import os

from rich.console import Console


console = Console()


def load_conf():
    with open(constant.GPMGRCONF_PATH, 'r') as f:
        profiles = json.load(f)

    return profiles


def save_profiles(profiles: list):
    with open(constant.GPMGRCONF_PATH, 'w') as f:
        json.dump(profiles, f)


def change_current(profile: dict, globally=False) -> bool:
    for k, v in profile.items():
        if k != 'name':
            cmd = f'git config {"--global" if globally else ""} {k} "{v}" > /dev/null 2>&1'
            console.print(f'[blue]Running command: {cmd}')
            status = os.system(cmd)
            if status:
                console.print('[red]Error: Failed to apply git profile.')
                return False
    return True
