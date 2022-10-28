from setuptools import setup

setup(
    name='rtsp-server',
    version='0.1.1',
    packages=['rtsp_server'],
    install_requires=[
        "PyGObject>=3.20.0",
    ],
    entry_points={
        'console_scripts': [
            'rtsp-server=rtsp_server:run_server',
        ]
    }
)