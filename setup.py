from setuptools import setup, find_packages
import os

versionfile = open(os.path.join('pleiades', 'portlet', 'references',
                                'version.txt'))
version = versionfile.read().strip()
versionfile.close()

setup(name='pleiades.portlet.references',
      version=version,
      description="Display references of a page",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Sean Gillies',
      author_email='scg4@nyu.edu',
      url='http://atlantides.org/svn/pleiades/pleiades.portlet.references',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pleiades', 'pleiades.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
