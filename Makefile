lint:
	ruff check .

test:
	pytest --maxfail=1 --disable-warnings -q
