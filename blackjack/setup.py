from setuptools import setup

setup(
    name='blackjack',
    version='0.0.1',
    packages=['blackjack'],
    entry_points={
        'console_scripts': [
            'blackjack=blackjack.game:main',
        ],
    },
    install_requires=[
        'termcolor==1.1.0',
    ],
)
