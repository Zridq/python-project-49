brain-games:
	@poetry run brain-games

build:
	@poetry build

publish:
	@poetry publish --dry-run --username BIBA --password BUBA

package-install:
	@python3 -m pip install --user dist/*.whl

RE:
	@python3 -m pip install --force-reinstall --user dist/*.whl
 
lint:
	@poetry run flake8 brain_games

Asci:
	@asciinema rec