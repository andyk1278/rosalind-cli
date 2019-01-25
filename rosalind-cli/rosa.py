import os
import sys

import click


@click.command(name='rosa', options_metavar='[OPTION]')
def main(option, problem):
	"""Python-based Rosalind command line tool"""
	# No problem given (or given option ignores the problem arg)
	files = problem_glob()