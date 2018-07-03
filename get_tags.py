import authorise

def main(argv):
  service = authorise.main(argv)
  accouts = service.accounts().list()
  containers = [service.accounts().get(x).containers().list(parent=account_path).execute() for x in accounts]


if __name__ == '__main__':
  main(sys.argv)

