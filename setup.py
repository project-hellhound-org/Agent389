from setuptools import setup, find_packages

setup(
    name="dirrogue",
    version="1.0",
    description="DirRogue: Advanced LDAP Injection Security Toolkit [HELLHOUND-class]",
    author="Abinav3ac",
    packages=find_packages(),
    py_modules=["dirrogue"],
    entry_points={
        "console_scripts": [
            "dirrogue=dirrogue:main",
        ],
    },
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rich",
    ],
    python_requires=">=3.7",
)
