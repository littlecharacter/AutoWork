# HelloPython
Python学习

## 一、为什么要设计好目录结构?  
1. 可读性高: 不熟悉这个项目的代码的人，一眼就能看懂目录结构，知道程序启动脚本是哪个，测试目录在哪儿，配置文件在哪儿等等。从而非常快速的了解这个项目。
2. 可维护性高: 定义好组织规则后，维护者就能很明确地知道，新增的哪个文件和代码应该放在什么目录之下。这个好处是，随着时间的推移，代码/配置的规模增加，项目结构不会混乱，仍然能够组织良好。

## 二、目录结构示例
```angular2html
|-- bin/    存放项目的一些可执行文件，当然你可以起名script/之类的也行，但bin/更直观。易懂  
|   |-- __init__  
|　 |-- start.py   写启动程序  
|  
|-- core/   存放项目的所有源代码(核心代码）(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。 (2) 其子目录tests/存放单元测试代码； (3) 程序的入口最好命名为main.py。
|   |-- tests/   
|   |   |-- __init__.py
|   |   |-- test.main.py  
|   |
|   |-- __init__.py
|   |-- test_main.py|  存放核心逻辑  
|
|-- conf/    配置文件
|   |-- __init__.py
|   |-- setting.py   写上相关配置
|
|---db/    数据库文件
|   |--db.json    写数据库文件
|   
|-- docs/   存放一些文档
|   
|-- lib/   库文件，放自定义模块和包
|   |-- __init__.py
|   |-- common.py    放常用的功能
|
|-- log/   日志文件
|   |-- access.log    写上日志
|
|-- __init__.py
|-- README    项目说明文件
```
> _\_\_init\_\_.py的作用
有__init__.py的目录是Python包，目录下的Python脚本叫做模块，没有的只是普通目录，一般__init__.py都为空，当导入带有__init__.py的包时都会先去执行__init__.py脚本，因此可以在__init__.py做相应的初始化。

## 三、python — 项目命名规范
|类型 |	公有/外部成员 |	私有/内部成员 |
|  ----  | ----  |  ----  |
|项目（project）|	MyProject | |	
|模块（module）|	my_naming_convention |	_my_naming_convention|
|包（package）|	my_naming_convention |	|
|类（class）|	MyNamingConvention |	_MyNamingConvention|
|异常（Exception）|	MyNamingConvention	| |
|函数（function）|	my_naming_convention() |	_my_naming_convention()|
|全局/类常量（constant）|	MY_NAMING_CONVENTION |	_MY_NAMING_CONVENTION|
|全局/类变量（variable）|	my_naming_convention |	_my_naming_convention|

## grid 布局
![img.png](./img/sticky.png)