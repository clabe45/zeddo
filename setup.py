from setuptools import setup, find_packages

with open('README.md', 'r') as r:
    long_description = r.read()

setup(
    name='zeddo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['click', 'requests', 'click-config-file', 'toml'],
    entry_points='''
        [console_scripts]
        zeddo=zeddo.__init__:top_news
    ''',
    description='News CLI for lazy people',
    long_description=long_description,
    keywords='cli news current events tool',
    url='http://github.com/clabe45/zeddo',
    author='Caleb Sacks',
    license='GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers"
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        "Topic :: Internet",
        "Topic :: Office/Business :: News/Diary"
    ]
)
