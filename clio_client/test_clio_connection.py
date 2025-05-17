# test_clio_connection.py

from clio_client.session import ClioSession

# Create session (auto-loads token, auto-refreshes if needed)
session = ClioSession()

# Use the Matters API (already authenticated)
matters = session.matters_api.list_matters().data

for matter in matters:
    print(matter.display_number)
