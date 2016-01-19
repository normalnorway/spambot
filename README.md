Normals SpamBot
===============

Email addresses are read from stdin. One email per line.

Email body goes in a file named `body.html` in the currenty directory. To
create `body.txt` run `make` (each time body.html has changed).

The from address are set in `settings.yaml`

## Usage

### Testing

    $ echo test@example.org | python main.py -s 'My subject'

### The real thing

    $ python main.py -s 'My subject' < email-address | tee send.log
