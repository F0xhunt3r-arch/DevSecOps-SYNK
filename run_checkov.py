import sys
from checkov.main import Checkov

if __name__ == "__main__":
    checkov = Checkov()
    sys.exit(checkov.run())
