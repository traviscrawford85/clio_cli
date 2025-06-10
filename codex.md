# Codex Environment Notes

- Run `python setup_codex.py` to install all required dependencies.
- Use `PYTHONPATH=.` and ensure all models are importable from root.
- Forward refs in Pydantic should call `.model_rebuild()` post definition.
- Use `TYPE_CHECKING` for safe circular imports.
