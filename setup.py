from __future__ import with_statement
from setuptools import setup, find_packages
import io
import versioneer

def readme():
    with io.open('README.md', encoding="utf-8") as f:
        return f.read()

def pip_requirements(fname='requirements.txt'):
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            reqs.append(line)
    return reqs

reqs = [line.strip() for line in open('requirements.txt')]

setup(
    name                 = "compliance-checker",
    version              = versioneer.get_version(),
    description          = "Checks Datasets and SOS endpoints for standards compliance",
    long_description     = readme(),
    license              = 'Apache License 2.0',
    author               = "Dave Foster",
    author_email         = "dave@axiomdatascience.com",
    url                  = "https://github.com/ioos/compliance-checker",
    packages             = find_packages(),
    install_requires     = pip_requirements(),
    tests_require        = ['pytest'],
    classifiers          = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
    include_package_data = True,
    scripts=['cchecker.py'],

    # Note: Do not use colons in the entry-point keys. Python 3 reserves
    # portions of the key after a colon for special use.

    # Note: The entry point names are not used at all. All methods in the
    # compliance checker use class attributes to determine the checker's name
    # and version. But, an entry point must be defined for each plugin to be
    # loaded.

    entry_points         = {
        'console_scripts': [
            'compliance-checker = cchecker:main'
        ],
        'compliance_checker.suites': [
            'cf-1.6 = compliance_checker.cf.cf:CF1_6Check',
            'cf-1.7 = compliance_checker.cf.cf:CF1_7Check',
            'acdd-1.1 = compliance_checker.acdd:ACDD1_1Check',
            'acdd-1.3 = compliance_checker.acdd:ACDD1_3Check',
            'ioos_sos = compliance_checker.ioos:IOOSBaseSOSCheck',
            'ioos-0.1 = compliance_checker.ioos:IOOS0_1Check',
            'ioos-1.1 = compliance_checker.ioos:IOOS1_1Check',
        ]
    },
    package_data         = {
        'compliance_checker': ['data/*.xml', 'tests/data/*.nc', 'tests/data/*.cdl', 'tests/data/non-comp/*.cdl', 'data/templates/*.j2'],
    },
    cmdclass=versioneer.get_cmdclass(),
)
