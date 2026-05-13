from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess, os

def run_post_install():
    try:
        result = subprocess.run(["code", "--version"], capture_output=True, timeout=5)
        if result.returncode != 0:
            return
        from tojscript import install_extension
        install_extension()
        print("✓ TojScript подсветка для VS Code установлена!")
    except Exception:
        pass

class PostInstall(install):
    def run(self):
        install.run(self)
        run_post_install()

class PostDevelop(develop):
    def run(self):
        develop.run(self)
        run_post_install()

setup(
    name="tojscript",
    version="1.0.14",
    packages=find_packages(),
    install_requires=["colorama", "chardet"],
    cmdclass={
        "install": PostInstall,
        "develop": PostDevelop,
    },
    entry_points={
        "console_scripts": [
            "toj=tojscript:main",
        ],
    },
)
