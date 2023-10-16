import sys
from json import load
from os import environ
from os import path


def conf_path():
    locations = [
        "i3-quickterm/config.json",
        "i3/i3-quickterm.json",  # legacy location
    ]
    home_dir = environ["HOME"]
    xdg_dir = environ.get("XDG_CONFIG_DIR", f"{home_dir}/.config")

    for loc in locations:
        full_loc = f"{xdg_dir}/{loc}"
        if path.exists(full_loc):
            return full_loc

    return None


def read_conf(fn):
    if fn is None:
        print("no config file! using defaults", file=sys.stderr)
        return {}

    try:
        with open(fn, "r") as f:
            c = load(f)
        return c
    except Exception as e:
        print(f"invalid config file: {e}", file=sys.stderr)
        return {}
