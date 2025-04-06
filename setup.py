from setuptools import setup, find_packages

setup(
    name="deeptminter",
    version="0.0.1",
    keywords=["pip", "deeptminter"],
    description="deeptminter",
    long_description="transmembrane protein interaction site prediction",
    license="GPL-3.0",

    url="https://github.com/2003100127/deeptminter",
    author="Jianfeng Sun",
    author_email="jianfeng.sunmt@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>=3.11,<4',
    install_requires=[
        'numpy==2.1.3',
        'tensorflow==2.19',
        'scikit-learn==1.6.1',
        'pandas==2.2.3',
        'joblib==1.4.2',
        'biopython',
        'pyfiglet',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'deeptminter=deeptminter.predict:isite_',
            'deeptminter_download=deeptminter.predict:download',
            'deeptminter_assemble=deeptminter.predict:stacking_',
        ],
    }
)