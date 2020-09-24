#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Git Commit Report Object
Generates a Dictionary about a repository
Example:
    $ python commit-track.py
"""
from git import Repo
import sys
import datetime
import csv
from pathlib import Path

class CommitReport:

	def __init__(self):
		self.repo = ''
		self.commits = ''

	def parse(self, repo_path = '',  name = '', limit = 10000000 ):
		repo = Repo(repo_path)
		report = {}
		count = 0
		file_list = []
		for commit in repo.iter_commits( ):
			count += 1
			s = commit.stats
			#commit.message
			#commit.author.name
			#commit.authored_date
			#commit.committer.name
			#commit.committed_date
			#commit.tree.blobs <- files

			total = s.total
			authored_date = datetime.datetime.fromtimestamp(
				int(commit.authored_date)
			).strftime('%Y-%m')

			if name != None:
				if commit.author.name != name:
					continue

			if authored_date not in report.keys():
				report[authored_date] = {'monthyear':authored_date, 'insertions':0, 'deletions':0, 'lines':0, 'files':0, 'commits':0}
				file_list = []

			report[authored_date]['insertions'] += total['insertions']
			report[authored_date]['deletions'] += total['deletions']
			report[authored_date]['lines'] += total['lines']
			report[authored_date]['files'] += total['files']
			report[authored_date]['commits'] += 1
			if count >= limit:
				break

		self.commits = report

	def save(self, save_path ):
		csv_columns = ['monthyear','insertions','deletions','lines','files','commits']
		with open(save_path, 'w', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
			writer.writeheader()
			for data in self.commits:
				writer.writerow(self.commits[data])

	def list_paths(self, root_tree, path=Path(".")):
		for blob in root_tree.blobs:
			yield path / blob.name
		for tree in root_tree.trees:
			yield from self.list_paths(tree, path / tree.name)