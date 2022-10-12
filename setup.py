from setuptools import setup

setup(
    name='rtsp-server',
    version='0.1.1',
    install_requires=[
        "PyGObject~=3.42.2",
    ],
    entry_points={
        'console_scripts': [
            'rtsp-server = rtsp-server:main',
        ]
    }
)