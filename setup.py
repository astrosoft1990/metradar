from setuptools import setup, find_packages
import os
# 尝试读取 pyproject.toml
def get_version():
    try:
        # Python 3.11+
        import tomllib
    except ImportError:
        # Python < 3.11，需要安装 tomli
        try:
            import tomli as tomllib
        except ImportError:
            raise RuntimeError("tomli is required to read pyproject.toml in Python < 3.11")

    with open(os.path.join(os.path.dirname(__file__), "pyproject.toml"), "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]


setup(
    name="metradar",
    version=get_version(),
    packages=find_packages(),  # 自动发现所有包
)


# python ./setup.py install
