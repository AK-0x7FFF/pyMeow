import subprocess
from pathlib import Path

from setuptools import setup, find_packages
from setuptools.command.build import build



class BuildPy(build):
   @staticmethod
   def build() -> bool:
      script = Path("build.cmd")

      if not script.exists():
         print(f"Warning: Build script not found {script}")
         return True

      print(f"Executing build script: {script}")

      try:
         result = subprocess.run(
            [str(script)],
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
         )

         if result.returncode != 0:
            print(f"Build failed!")
            if result.stderr:
               print(f"Error output:\n{result.stderr[:1000]}")
            return False
         else:
            print(f"Build successful!")
            if result.stdout and result.stdout.strip():
               print(f"Output:\n{result.stdout[:500]}")
            return True

      except Exception as e:
         print(f"Error executing build script: {e}")
         return False

   def run(self):
      if not self.build():
         exit(1)
      super().run()


setup(
   name='pyMeow',
   version='1.73.42',
   description='Python Library for external Game Hacking',
   author='qb',
   url='https://github.com/qb-0/PyMeow',
   license='MIT',
   cmdclass={
      'build': BuildPy
   },
   packages=find_packages(where="py"),
   package_dir={
      "": "py"
   },
   package_data={
        'pyMeow': ['*.pyd'],
    },
   include_package_data=True,
)