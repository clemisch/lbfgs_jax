from setuptools import setup

setup(
    name="lbfgs_jax",
    version="1.0",
    description="Wrapper around scipy LBFGS to use with JAX",
    author="Clemens Schmid",
    author_email="clemens.schmid@psi.ch",
    packages=["lbfgs_jax"],
    install_requires=["numpy", "scipy", "jax"],
    license="MIT",
)
