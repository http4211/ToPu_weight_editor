#!/usr/bin/env python3
"""Build a Blender repository index from the latest stable GitHub release."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import tomllib
import urllib.request
import zipfile

FIELDS = ('schema_version', 'id', 'name', 'tagline', 'version', 'type',
          'maintainer', 'license', 'blender_version_min', 'blender_version_max',
          'website', 'permissions', 'tags', 'platforms', 'copyright')

def make_index(path, url):
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f'Corrupt ZIP member: {bad}')
        manifest = tomllib.loads(archive.read('blender_manifest.toml').decode('utf-8'))
        if '__init__.py' not in archive.namelist():
            raise ValueError('Expected extension __init__.py at ZIP root')
    if manifest['id'] != 'topu_weight_editor':
        raise ValueError('Unexpected extension ID')
    if manifest['type'] != 'add-on':
        raise ValueError('Expected add-on')
    entry = {key: manifest[key] for key in FIELDS if key in manifest}
    data = Path(path).read_bytes()
    entry.update(archive_url=url, archive_size=len(data),
                 archive_hash='sha256:' + hashlib.sha256(data).hexdigest())
    return {'version': 'v1', 'blocklist': [], 'data': [entry]}

def latest_release(repository):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Invalid repository')
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'TPWE-Repository-Builder'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    request = urllib.request.Request('https://api.github.com/repos/' + repository + '/releases/latest', headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        release = json.load(response)
    if release['draft'] or release['prerelease']:
        raise ValueError('Only stable published releases are supported')
    matches = [asset for asset in release['assets'] if re.fullmatch(
        r'ToPu_weight_editor_\d+\.\d+\.\d+\.zip', asset['name'])]
    if len(matches) != 1:
        raise ValueError('Latest release must have exactly one ToPu_weight_editor_X.Y.Z.zip asset; upload it before publishing, or run workflow again after upload')
    return release, matches[0]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', default='http4211/ToPu_weight_editor')
    parser.add_argument('--zip', type=Path)
    parser.add_argument('--archive-url')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.zip:
        if not args.archive_url:
            parser.error('--zip requires --archive-url')
        index = make_index(args.zip, args.archive_url)
    else:
        release, asset = latest_release(args.repository)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'extension.zip'
            # Public download: do not forward the API token to asset/CDN hosts.
            with urllib.request.urlopen(asset['browser_download_url'], timeout=120) as response:
                path.write_bytes(response.read())
            index = make_index(path, asset['browser_download_url'])
        version = index['data'][0]['version']
        if asset['name'] != f'ToPu_weight_editor_{version}.zip':
            raise ValueError('Asset filename and manifest version differ')
        if release['tag_name'] not in (version, 'v' + version):
            raise ValueError('Release tag and manifest version differ')
        if index['data'][0]['archive_size'] != asset['size']:
            raise ValueError('Downloaded file size differs from GitHub asset')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Generated index for', index['data'][0]['version'])

if __name__ == '__main__':
    main()
