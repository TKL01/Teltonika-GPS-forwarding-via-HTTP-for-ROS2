from setuptools import setup

package_name = 'gps_tools'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'gps_tools.gps_publisher',
        'gps_tools.gps_server',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TKL',
    maintainer_email='your_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gps_publisher = gps_tools.gps_publisher:main',
            'gps_server = gps_tools.gps_server:main',
        ],
    },
)

