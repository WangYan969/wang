# coding:utf-8
import codecs
import os
import io
import sys

try:
    from setuptools import setup , find_packages
except:
    from distutils.core import setup
"""
打包的用的setup必须引入，
"""


# def read(fname):
#     """
#     定义一个read方法，用来读取目录下的长描述
#     我们一般是将README文件中的内容读取出来作为长描述，这个会在PyPI中你这个包的页面上展现出来，
#     你也可以不用这个方法，自己手动写内容即可，
#     PyPI上支持.rst格式的文件。暂不支持.md格式的文件，<BR>.rst文件PyPI会自动把它转为HTML形式显示在你包的信息页面上。
#     """
#     return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

# with io.open("README.rst",encoding ='utf-8') as f:
#     LONG_DESCRIPTION =f.read()
long_description=open('READEME.rst').read()
NAME = "pypi_t1t2t10"
"""
名字，一般放你包的名字即可
"""
# install_reauires = open("requirtment.txt").readlines()
PACKAGES = find_packages()
"""
包含的包，可以多个，这是一个列表
"""

DESCRIPTION = "this is a test package for packing python liberaries tutorial."
"""
关于这个包的描述
"""

# LONG_DESCRIPTION = read("README.rst")
"""
参见read方法说明
"""

KEYWORDS = "test python package"
"""
关于当前包的一些关键字，方便PyPI进行分类。
"""

AUTHOR = "WangYan"
"""
谁是这个包的作者，写谁的名字吧
我是MitchellChu，自然这里写的是MitchellChu
"""

AUTHOR_EMAIL = "youremail@email.com"
"""
作者的邮件地址
"""

URL = "https://github.com/WangYan969/turing.git"
"""
你这个包的项目地址，如果有，给一个吧，没有你直接填写在PyPI你这个包的地址也是可以的
"""

VERSION = "1.0.1"
"""
当前包的版本，这个按你自己需要的版本控制方式来
"""

LICENSE = "MIT"
"""
授权方式，我喜欢的是MIT的方式，你可以换成其他方式
"""

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)

## 把上面的变量填入了一个setup()中即可。