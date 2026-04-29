from setuptools import setup, find_packages

setup(
    name="agent389",
    version="1.0",
    description="Agent389: Advanced LDAP Injection Security Toolkit [HELLHOUND-class]",
    author="Abinav3ac",
    packages=find_packages(),
    py_modules=["agent389"],
    entry_points={
        "console_scripts": [
            "agent389=agent389:main",
        ],
    },
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rich",
    ],
    python_requires=">=3.7",
)
