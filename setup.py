from setuptools import setup, find_packages
import os

version = '1.0.dev0'


tests_require = ['plone.app.testing',
                 'plone.mocktestcase',
                 'ftw.testing',
                 ]


extras_require = {
    'tests': tests_require,
    }


setup(name='onegov.policy',
      version=version,
      description="OneGov Box policy package",
      long_description=open("README.rst").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Programming Language :: Python',
        ],

      keywords='onegov box policy',
      author='Verein OneGov',
      url='https://github.com/OneGov/onegov.policy',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['onegov'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',

        'collective.quickupload',
        'collective.js.extjs',

        'ftw.billboard',
        'ftw.blog',
        'ftw.book',
        'ftw.calendarwidget',
        'ftw.colorbox',
        'ftw.contentmenu',
        'ftw.dashboard.dragndrop',
        'ftw.dashboard.portlets.favourites',
        'ftw.dashboard.portlets.postit',
        'ftw.dashboard.portlets.recentlymodified',
        'ftw.dictstorage',
        'ftw.file',
        'ftw.geo',
        'ftw.globalstatusmessage',
        'ftw.inflator',
        'ftw.journal',
        'ftw.keywordoverlay',
        'ftw.meeting',
        'ftw.notification.email',
        'ftw.participation',
        'ftw.pdfgenerator',
        'ftw.permissionmanager',
        'ftw.poodle',
        'ftw.tabbedview',
        'ftw.table',
        'ftw.tagging',
        'ftw.task',
        'ftw.tooltip',
        'ftw.upgrade',
        'ftw.usermanagement',
        'ftw.workspace',
        'ftwbook.graphicblock',

        'izug.ticketbox',
        ],

      tests_require=tests_require,
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
