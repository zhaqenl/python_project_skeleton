try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup
    config = [
        'description': 'My Project',
        'author': 'Raymund Martinez',
        'url': 'https://github.com/zhaqenl',
        'download_url': 'https://github.com/zhaqenl',
        'author_email': 'zhaqenl@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
    ]
    setup(**config)
