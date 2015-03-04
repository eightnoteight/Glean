#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Glean
"""
from configparser import ConfigParser
from tempfile import NamedTemporaryFile
import argparse
import subprocess
import re

CONFIGFILE = 'config'
HELP = '''
Glean is a simple script to quickly execute a code on some testcases.
Which makes the competitive programming work flow quicker than ever.
'''


def get_tests(code, config, lang):
    """
    get_inputs
    """
    if config[lang].getboolean('newline'):
        delim = '\n'
    else:
        delim = ''
    return re.findall(
        "(?<={start:s})(?s)(.*?)(?={end:s})".format(
            start=re.escape(config[lang]['start'] + delim),
            end=re.escape(config[lang]['end'] + delim)),
        open(code, 'r').read()
    )


def run_tests(testcases, config, lang, codef):
    """
    run_tests
    """
    for test in testcases:
        with NamedTemporaryFile() as tmp:
            tmp.write(bytes(test, encoding='utf-8'))
            tmp.flush()
            proc = subprocess.Popen(
                config[lang]['cmd'].format(
                    filepath=tmp.name, codef=codef), shell=True)
            proc.communicate()


def main():
    """docstring for main"""
    argvparser = argparse.ArgumentParser(description=HELP)
    argvparser.add_argument(
        '--file',
        help='program to run')
    argvparser.add_argument(
        '--language',
        help='language of the program, i.e python, cpp, c, python3')
    args = argvparser.parse_args()
    config = ConfigParser()
    config.read(CONFIGFILE)
    testcases = get_tests(args.file, config, args.language)
    run_tests(testcases, config, args.language, args.file)


if __name__ == '__main__':
    main()
