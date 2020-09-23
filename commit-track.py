#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Git Commit Tracker
Parses a Git repository and generates a basic report
Example:
    $ python commit-track.py
"""
import os.path
from git import Repo
import sys
import datetime
import csv
import argparse
from Report import Report

def main():
	
	parser = argparse.ArgumentParser(description='A tutorial of argparse!')
	parser.add_argument("--repo", required=True, type=str, help="Full system path to the repo to report on")
	parser.add_argument("--name", required=False, type=str, help="A specific commiter you want results from")
	parser.add_argument("--file", required=False, default="commits.csv", type=str, help="A specific commiter you want results from")
	parser.add_argument("--limit", required=False, default=100000000, type=int, help="How many results to return")
	args = parser.parse_args()

	if os.path.isdir(args.repo) == False:
		raise Exception("That repository can't be found :( ")

	report = Report()
	report.parse(args.repo, args.name, args.limit)
	report.save(args.file)
	sys.exit()

if __name__ == "__main__":
	main()
