# Start, Stop, Pause and Toggle Full Screen Controls

Start, stop, pause and toggle full screen mode programatically using this script.

Start, stop and pause are interacting with the rotation, not the contents of the page.

## Usage

The script can be re-used as a CLI tool by passing arguments via the command line.

Your machines ID can be found in the URL when viewing the machines edit page from the dashboard.

The script is called by passing 2 arguments

- The action: `start`, `stop`, `pause` or `fullscreen`
- The machine ID (an integer ie 2313)

```
python control.py <action> <machine_id>
```

For example, to `start` the rotation on a machine

```
python control.py start 7363
```

To `stop` the rotation on a machine

```
python control.py stop 7363
```

To `pause` the rotation on a machine

```
python control.py pause 7363
```

To `toggle full screen` the rotation on a machine

```
python control.py fullscreen 7363
```
