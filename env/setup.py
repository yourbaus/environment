from pathlib import Path
import shutil

from setuptools import setup # type: ignore
from setuptools.command.install import install # type: ignore
from setuptools.command.egg_info import egg_info # type: ignore
from setuptools.command.develop import develop # type: ignore


def run_post_processing():
    # copy plottr settings
    plottr_dir = Path('~/.plottr').expanduser()
    plottr_dir.mkdir(exist_ok=True)
    plottr_copy = plottr_dir / 'plottrcfg_main.py'
    if not plottr_copy.is_file():
        shutil.copyfile('./plottrcfg_main.py', plottr_copy)
    # copy leklab json
    settings_dir = Path('~/.leklab').expanduser()
    settings_dir.mkdir(exist_ok=True)
    leklab_copy = settings_dir / 'leklab.json'
    if not leklab_copy.is_file():
        shutil.copyfile('./leklab.json', leklab_copy)


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        run_post_processing()


class PostEggCommand(egg_info):
    def run(self):
        egg_info.run(self)
        run_post_processing()


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        run_post_processing()


setup(
    name='environment',
    packages=['leklab'],
    version=0.1,
    cmdclass={
        'install' : PostInstallCommand,
        'egg_info': PostEggCommand,
        'develop': PostDevelopCommand
        }
)