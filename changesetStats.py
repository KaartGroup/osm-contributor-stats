#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
#========================================================================="
# https://github.com/pierzen/osm-contributor-stats/blob/master/Script-to-run-OsmContributorStats-Module-Extract-Objects-Calculate-Statistics.py
# Pierre Beland, 10-2013
# Example running version 0.1 of OsmContributorStats
# OSM Contributors Histor Statistics, for a specific bbox zone and date range
# STATISTIQUES Historiques, contributeurs OSM pour une zone bbox et paire de dates
#========================================================================="
#========================================================================="
"""
import os
import OsmApi
# Instantiation classe OsmApi
osmApi = OsmApi.OsmApi(debug=False)
import OsmContributorStats
# Instantiation classe OsmContributorStats
ContributorStats = OsmContributorStats.OsmContributorStats(
    rep='.', lang="en", debug=False)
dir(ContributorStats)

#===============================================================================
# users :  array of contributor ID's or Name by team - if no users, all users in the bbox will be selected
# users = [None] * 2
# users[0] = [""]
# users[1] = [""]

"""
Example with usernames
users=[None]*2
users[0] = ["abc","def","gjol"]
users[1] = ["zyx","avb Yul"]
"""

print('Enter Start Date (YYYY-MM-DD):')
from_date = raw_input()

print('Enter End Date (YYYY-MM-DD):')
to_date = raw_input()

print('Enter BBOX (min_lon, max_lon, min_lat, max_lat):')
bbox = input()

print('Enter File Name Prefix:')
prefix = raw_input()

print('Enter Users (Comma Seperated):')
users = [raw_input().replace(' ', '').split(',')]

# Step 1 - Extract History Data
ContributorStats.API6_Collect_Changesets(team_from=0, team_to=0, from_date=from_date,
                                         to_date=to_date,
                                         min_lon=bbox[0], max_lon=bbox[1], min_lat=bbox[2], max_lat=bbox[3],
                                         prefix=prefix, users=users)

# Step 2 - Statistics from data stored locally	
ContributorStats.Changesets_Contributor_Statistics(team_from=0, team_to=0, from_date=from_date,
                                         to_date=to_date,
                                         min_lon=bbox[0], max_lon=bbox[1], min_lat=bbox[2], max_lat=bbox[3],
                                         prefix=prefix, users=users)


print "\n-----------------------------------------------------"

ContributorStats.__del__()
del OsmContributorStats

import sys
sys.exit('\n=== Travail complété ===')
