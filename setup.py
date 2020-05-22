import setuptools

setuptools.setup(
    name="learningcrux_dl",
    version="0.0.1",
    author="Swapnil Soni",
    install_requires=[
        'youtube-dl',
        'requests',
        'lxml',
        'bs4'
    ],
    packages=['learningcrux_dl'],
    entry_points={
        'console_scripts': [
            'lcx-dl=learningcrux_dl.cli:lcx'
        ]
    }
)