import sys
print(sys.path)

try:
    from setuptools import setup, find_packages
except ImportError as e:
    print(e)
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

# Call setup function, adding use_2to3 kwarg if under python 3
extras = {}

setup(
    name='oyoyo',
    version="0.0.1",
    description='a fast, simple irc module suitable for clients, bots and games',
    author='Dunk Fordyce, Daniel da Silva (current)',
    author_email='dunkfordyce@gmail.com, meltingwax@gmail.com',
    license="MIT",
    url='http://code.google.com/p/oyoyo/',
    install_requires=[],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    entry_points="""
    [console_scripts]
    oyoyo_example_bot = oyoyo.examplebot:main
    """,
    **extras
)
