.PHONY: sync-poetry

sync-poetry:
	poetry lock --regenerate
	poetry sync --no-root