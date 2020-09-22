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

def main( repo = '', name = '' , limit = 10000000, csv_file = "commits.csv"):
	repo = Repo(repo)
	report = {}
	count = 0

	for commit in repo.iter_commits( ):
		count += 1
		s = commit.stats
		total = s.total
		authored_date = datetime.datetime.fromtimestamp(
	        int(commit.authored_date)
	    ).strftime('%Y-%m')

		if name != None:
			if commit.author.name != name:
				continue

		if authored_date not in report.keys():
			report[authored_date] = {'monthyear':authored_date, 'insertions':0, 'deletions':0, 'lines':0, 'files':0, 'commits':0}

		report[authored_date]['insertions'] += total['insertions']
		report[authored_date]['deletions'] += total['deletions']
		report[authored_date]['lines'] += total['lines']
		report[authored_date]['files'] += total['files']
		report[authored_date]['commits'] += 1
		if count >= limit:
			break

	csv_columns = ['monthyear','insertions','deletions','lines','files','commits']
	with open(csv_file, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
		writer.writeheader()
		for data in report:
			writer.writerow(report[data])

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='A tutorial of argparse!')
	parser.add_argument("--repo", required=True, type=str, help="Full system path to the repo to report on")
	parser.add_argument("--name", required=False, type=str, help="A specific commiter you want results from")
	args = parser.parse_args()

	if os.path.isdir(args.repo) == False:
		raise Exception("That repository can't be found :( ")

	main(repo=args.repo, name=args.name)
