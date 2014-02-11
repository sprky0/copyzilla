#!/usr/bin/python
import os
import sys
import shutil
import subprocess

targetlist = sys.argv[1:];
target = targetlist.pop();

if not targetlist:
	print "No files!";
	exit;

if not target.endswith("/"):
	target += "/";

for item in targetlist:
	target_full = os.path.normpath(target + item)
	target_dir = os.path.dirname(target_full);
	subprocess.check_output(['mkdir', '-p', target_dir]);
	subprocess.check_output(['cp', '-Rf', item, target_full]);