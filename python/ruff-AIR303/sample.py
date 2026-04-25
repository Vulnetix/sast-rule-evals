# Sample for Ruff rule AIR303: airflow3-incompatible-function-signature
# This file is designed to trigger the AIR303 rule.
# Run: ruff check --select AIR303 <this_file>

from airflow.lineage.hook import HookLineageCollector

collector = HookLineageCollector()
# Passing positional arguments will raise a runtime error in Airflow 3.0
collector.create_asset("s3://bucket/key")
