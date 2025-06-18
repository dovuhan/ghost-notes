from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ghostnotes-app',
    version='2.1.0',
    author='Dovuhan',
    author_email='dovuhan@mail.ru',
    description='A stylish, note-taking application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dovuhan/ghost-notes',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Desktop Environment',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'doguhan = ghostnotes.main:run',
        ],
    },
)
