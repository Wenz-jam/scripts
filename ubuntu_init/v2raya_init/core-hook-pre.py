#!/usr/bin/python3

import argparse
from os import path
import json

def main():
    # parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--v2raya-confdir', type=str, required=True)
    parser.add_argument('--stage', type=str, required=True)
    args = parser.parse_args()

# we only modify the config file at the pre-start stage
    if args.stage != 'pre-start':
        return

# read the content from the config.json
    conf_path = path.join(args.v2raya_confdir, 'config.json')
    print(conf_path)
    with open(conf_path) as f:
        conf = json.loads(f.read())

# confirm service port
    port = -1
    for inbound in conf['inbounds']:
        if inbound["tag"] != "api-in_ipv4":
            continue
        port = inbound["port"]
        break

    with open('/etc/v2ray/port', 'w') as f:
        f.write(str(port))

# add stat service
    conf["api"]['services'].append("StatsService")

# write back to the file
    with open(conf_path, 'w') as f:
        f.write(json.dumps(conf))

if __name__ == '__main__':
    main()
