#!/usr/bin/env python3
"""Verify metadata structure and links; no theorem is proved by this script."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
claims = json.loads((root/'metadata/claims.json').read_text(encoding='utf-8'))
statuses = {'PROVED','CONDITIONAL','COMPUTATIONAL_EVIDENCE','CONJECTURE',
            'FAILED_DISPROVED','OPEN_GAP','REPORTED_UNVERIFIED','EXTERNAL_RESULT'}
seen = set()
for item in claims:
    assert item['id'] not in seen, item['id']
    seen.add(item['id'])
    assert item['status'] in statuses, item
    assert (root/item['file']).is_file(), item['file']
    if item['status'] == 'PROVED':
        assert 'preprints/' in item['proof'], item['id']
        assert (root/item['proof']).is_file(), item['proof']
print(f'Validated {len(claims)} claim IDs, statuses and file paths.')
