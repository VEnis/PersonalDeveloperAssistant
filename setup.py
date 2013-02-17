from distutils.core import setup
from nose import commands

setup(
    name="pda",
    version="1.0",
    description="Personal Developer Assistant",
    author="Vyacheslav Enis",
    author_email="venis@difane.com",
    url='https://github.com/VEnis/PersonalDeveloperAssistant',
    packages=[
        'pda',
        'pda.config'
    ]
)
