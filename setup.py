from setuptools import setup
import os

package_name = 'topic_store'
def parse_package_requirements():
    requirements_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
    with open(requirements_file, "r") as fh:
        return [x.strip() for x in fh.readlines()]


setup(
    name=package_name,
    version='0.1.9',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'].extend(parse_package_requirements()),
    zip_safe=True,
    maintainer='kasm-user',
    maintainer_email='marc@hanheide.net',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ts_convert = topic_store.convert:_convert_cli'
        ],
    },
)
