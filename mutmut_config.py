"""Mutmut configuration."""

files_to_mutate = ['geometry.py']

def pre_mutation(context):
    if context.filename not in files_to_mutate:
        context.skip = True
