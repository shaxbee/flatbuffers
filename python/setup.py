from setuptools import setup, Extension

setup(
  name="Flatbuffers",
  version="1.0",
  description="Efficent serialization library",
  install_requires=["enum34"],
  ext_modules=[Extension('flatbuffers', ['flatbuffers.cpp'], extra_compile_args=["-std=c++11"])]
)
