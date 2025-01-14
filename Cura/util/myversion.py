"""
Helper module to check sha256 sum.
"""
__copyright__ = "Copyright (C) 2019 Dagoma - Released under terms of the AGPLv3 License"

import os
import urllib.request, urllib.error, urllib.parse

url_handle = None
version_url = "https://dist.dagoma3d.com/version/CuraByDagoma"

try:
	url_handle = urllib.request.urlopen(version_url, timeout=2)
except urllib.error.URLError:
	try:
		import ssl
		context = ssl._create_unverified_context()
		url_handle = urllib.request.urlopen(version_url, timeout=2, context=context)
	except:
		pass
except:
	pass

def isLatest():
	if url_handle is None:
		return True
	official_version = url_handle.read().decode('utf-8')
	return official_version == os.environ['CURABYDAGO_RELEASE_VERSION']
