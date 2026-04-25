# Sample for Ruff rule ISC004: implicit-string-concatenation-in-collection-literal
# This file is designed to trigger the ISC004 rule.
# Run: ruff check --select ISC004 <this_file>

facts = (
    "Lobsters have blue blood.",
    "The liver is the only human organ that can fully regenerate itself.",
    "Clarinets are made almost entirely out of wood from the mpingo tree."
    "In 1971, astronaut Alan Shepard played golf on the moon.",
)
