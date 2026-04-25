# Sample for Ruff rule AIR302: airflow3-moved-to-provider
# This file is designed to trigger the AIR302 rule.
# Run: ruff check --select AIR302 <this_file>

from airflow.auth.managers.fab.fab_auth_manager import FabAuthManager

fab_auth_manager_app = FabAuthManager().get_fastapi_app()
