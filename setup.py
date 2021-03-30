from setuptools import setup, find_packages

setup(
    name='zeddo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['click', 'requests', 'click-config-file'],
    entry_points='''
        [console_scripts]
        zeddo=zeddo.__init__:top_news
    ''',
    description='News CLI for lazy people',
    url='http://github.com/clabe45/zeddo',
    author='Caleb Sacks',
    license='GPLv3',
)
