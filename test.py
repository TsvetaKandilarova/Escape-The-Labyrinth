import glob
import subprocess
import sys


def main():
    tests = glob.glob("test_*.py")
    if len(sys.argv) > 1 and sys.argv[1] == "coverage":
        coverage(tests)
    else:
        test(tests)


def test(tests):
    for test_ in tests:
        print("\nTests for %s" % test_[5:])
        subprocess.call("python3.4 %s" % test_, shell=True)


def coverage(tests):
    subprocess.call("coverage erase", shell=True)

    for test_ in tests:
        subprocess.call("coverage run -p %s" % test_, shell=True)

    subprocess.call("coverage combine", shell=True)
    subprocess.call("coverage report -m", shell=True)


if __name__ == '__main__':
    main()
