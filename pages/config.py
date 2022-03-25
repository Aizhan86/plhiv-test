import os


class UserData(object):
    NAME = "aizha.o"
    PASSWORD ="Sunshine86!"
    URL = "https://plhiv-demo.dec.kz/"

    def get_environ(name, *args):
        environ = os.environ.get(name, URL)

        if str(environ).startswith('/run/secrets/'):
            if os.path.exists(environ):
                with open(environ, 'r') as secrets_file:
                    environ = secrets_file.read()
                    secrets_file.close()

        return environ


