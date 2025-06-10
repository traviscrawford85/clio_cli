from pathlib import Path

# Re-check for existence and contents of the clio_tokens.db file after kernel reset
db_path = Path("/home/sysadmin01/clio_cli/clio_tokens.db")
db_exists = db_path.exists()
db_size = db_path.stat().st_size if db_exists else None

db_exists, db_size
