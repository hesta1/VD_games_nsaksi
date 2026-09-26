install:
	uv sync

VD-games:
	uv run VD-games

VD-calc:
	uv run VD-calc

VD-gcd:
	uv run VD-gcd

VD-even:
	uv run VD-even

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check VD_games
