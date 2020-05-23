import setuptools

with open("README.md", 'r+') as f:
    print("opened")
    long_desc = f.read()

setuptools.setup(
    name="learningcrux_dl",
    version="0.0.1",
    author="Swapnil Soni",
    license="MIT",
    keywords=["learningcrux", "downloader", "learningcrux-dl", "lcx-dl"],
    description="Downloader for learningcrux.com",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    install_requires=[
        'youtube-dl',
        'requests',
        'lxml',
        'bs4',
        'click',
    ],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "License :: Unlicensed",
        "Operating System :: OS Independent",
    ],
    packages=['learningcrux_dl'],
    entry_points={
        'console_scripts': [
            'lcx-dl=learningcrux_dl.cli:lcx'
        ]
    },
    python_requires='>=3.6'
)