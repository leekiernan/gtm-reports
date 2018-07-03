# https://developers.google.com/tag-manager/api/v2/devguide
import argparse
import sys

import httplib2

from apiclient.discovery import build
from oauth2client import client
from oauth2client import file
from oauth2client import tools


def GetService(api_name, api_version, scope, client_secrets_path):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    flags = parser.parse_args([])
    flow = client.flow_from_clientsecrets(
        client_secrets_path, scope=scope,
        message=tools.message_if_missing(client_secrets_path))
    storage = file.Storage(api_name + '.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)
    http = credentials.authorize(http=httplib2.Http())
    service = build(api_name, api_version, http=http)

    return service

def main(argv):
    scope = ['https://www.googleapis.com/auth/tagmanager.edit.containers']
    service = GetService('tagmanager', 'v2', scope, 'client_secrets.json')


# if __name__ == '__main__':
#   main(sys.argv)
