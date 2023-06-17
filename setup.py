import setuptools

setuptools.setup(
    name="gyld-sdk",
    version="0.0.1",
    author="GYLD",
    author_email='info@gyld.com',
    description="GYLD SDK",
    url='https://github.com/cantek41/sdk.git',
    license='MIT',
    install_requires=['numpy~=1.24.2',
                      'pymssql~=2.2.7',
                      'SQLAlchemy~=1.4.44',
                      'requests~=2.28.1',
                      'pandas~=1.5.3'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=[
        'gyld.sdk',
        'gyld.sdk.data',
        'gyld.sdk.logservice',
        'gyld.sdk.media',
        'gyld.sdk.utility',
        'gyld.sdk.services'
    ],
    package_dir={'gyld.sdk': 'src'},
    python_requires=">=3.8"
)
