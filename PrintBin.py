#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Print all currently visible Resolve bin names and save as a text file.
Requires DaVinci Resolve 15.3 and above.

In Windows place this script in:
%AppData%Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\PrintBins.py
for access via the scripts dropdown menu. Or drag and drop onto the Resolve
console. Resolve 15 shows dropdown menu from within Fusion page only.

See also YouTube "DaVinci Resolve Running Scripts."
'''
# Copyright 2020 Igor Ridanovic, www.metafide.com

import os

# Windows file path only. Modify for MacOS/Linux. You can also use an absolute path.
file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
eol = '\r\n'

resolve = bmd.scriptapp('Resolve')
pm   = resolve.GetProjectManager()
proj = pm.GetCurrentProject()
mp   = proj.GetMediaPool()

current_bin      = mp.GetCurrentFolder()
sub_bins         = current_bin.GetSubFolders()
current_bin_name = current_bin.GetName()

file_name = current_bin_name + '_SubBins.txt'
file_report = os.path.join(file_path, file_name)

with open(file_report, 'w') as f:

	f.write('Sub bins for: ' + current_bin_name + eol*2)

	for i in sub_bins.values():
		print i.GetName()
		f.write(i.GetName() + eol)

	f.write(eol + 'Visit www.metafide.com for DaVinci Resolve Apps')
