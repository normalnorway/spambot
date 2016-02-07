.PHONY: test


body.txt: body.html
	w3m -dump body.html > body.txt

# BUG: 'w3m -dump' will remove url links (only show text)


test:
	echo torkel@normal.no | python main.py -s "Testing SpamBot"
