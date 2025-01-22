from setuptools import setup, find_packages

setup(
    name="nora_package",
    version="0.0.1",
    author="noraliao",
    license='MIT License',
    description="工具箱",
    packages=find_packages(),
    py_modules=['nora_tool'],
    include_package_data=True,
    install_requires=[
        'requests>=2.32.3',
        'beautifulsoup4>=4.12.3',
    ],
)
