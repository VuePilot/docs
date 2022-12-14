# Hijack Start & Stop

Immediately show content on a given machines screen by using the `hijack` functionality.

This script can be used to perform a programmatic hijack of machines on your account and display any URL or app in your account immediately.

This may be used to programmatically trigger screens to display important content, dashboards and alerts in your business on an event triggered basis.

## Usage

The script can be re-used as a CLI tool by passing arguments via the command line.

Your machines ID can be found in the URL when viewing the machines edit page from the dashboard.

The script is called by passing 4 arguments

- The action: `start` or `stop`
- The machine ID (an integer ie 2313)
- The category of hijack: `url` or `app`
- The URL or token ID of the app (get the apps token from the URL on the apps edit page)

```
python hijack.py <action> <machine_id> <url | app> <url | token>
```

For example, to perform a `URL` hijack on a machine

```
python hijack.py start 7363 url https://mydashboard.com
```

To perform a an `app` hijack on a machine

```
python hijack.py start 7363 app af3gef62
```

To stop a hijack (and restart the rotation)

```
python hijack.py stop 7363
```
