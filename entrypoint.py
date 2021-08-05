#!/usr/bin/env python3

import sys
import os
import requests

if __name__ == "__main__" :
    # Rename these variables to something meaningful
    percent = float(sys.argv[1])
    text = sys.argv[2]
    output_path = sys.argv[3]

    colors = ['red', 'orange', 'green']

    if percent < 33:
        color = colors[0]
    elif percent < 66:
        color = colors[1]
    else:
        color = colors[2]


    text = text.replace('-', '--').replace('_', '__').replace(' ', '_')
    url = f"https://img.shields.io/badge/{text}-{percent}%25-{color}"
    r = requests.get(url, allow_redirects=True)

    with open(os.path.join(output_path, 'badge.svg'), 'w+') as f:
        f.write(r.text)

