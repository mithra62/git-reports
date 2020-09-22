# git-reports

This is a simple script to take a Git repository and generate reports on it.

## Reports
At the moment, is just a single CSV file that includes the below points grouped by monthyear

1. insertions
2. deletions
3. lines
4. files
5. commits


## Example

```
python ./commit-track.py --repo 'PATHTOREPO' --name 'Eric Lamb'
```
