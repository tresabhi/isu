from setuptools import find_packages, setup
import os
from glob import glob

package_name = "my_turtle"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name), glob("launch/*.launch")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="exouser",
    maintainer_email="43380238+tresabhi@users.noreply.github.com",
    description="TODO: Package description",
    license="Apache-2.0",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "publish_vel = my_turtle.publish_velocity:main",
            "subscribe_pose = my_turtle.pose_subscriber:main",
            "turtle_owner = my_turtle.turtle_owner:main",
            "turtle_renter = my_turtle.turtle_renter:main",
        ],
    },
)
