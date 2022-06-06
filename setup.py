import setuptools

setuptools.setup(
    name="arclet-alconna-cli",
    url="https://github.com/ArcletProject/Alconna-CLI",
    version="0.1.0",
    author="ArcletProject",
    author_email="rf_tar_railt@qq.com",
    description="Simple Cli For Alconna",
    license='MIT',
    packages=['arclet.alconna_cli'],
    install_requires=['arclet-alconna'],
    entry_points={
        'console_scripts': [
            'alconna = arclet.alconna_cli.__main__:main'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords=['alconna', 'cli', 'arclet', 'commandline'],
    python_requires='>=3.8',
    project_urls={
        'Documentation': 'https://arcletproject.github.io/docs/alconna/tutorial',
        'Bug Reports': 'https://github.com/ArcletProject/Alconna/issues',
        'Source': 'https://github.com/ArcletProject/Alconna',
    },
)
