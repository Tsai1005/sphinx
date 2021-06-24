.. toctree::
   :maxdepth: 1
   :caption: Contents:

.. _kernel:

快速开始
#####################

该文档主要描述AC697N_SDK开发包的使用方法及开发中注意的一些问题，
为用户进行二次开发提供参考,其中包括：

- 安装包管理工具
- 配置工具使用
- 配置宏的选择以及充电仓使用注意事项 

.. _host_setup:

.. rst-class:: numbered-step

包管理工具安装 
*******************

双击 :file:`杰理包管理器-setup-1.0.15.exe` 安装，按照提示安装完成即可.
详细的安装及使用步骤如下:

#. 安装`杰理软件包`工具之后，开始菜单栏会出现对应的菜单

    .. figure:: build-build-phase-1.svg
        :align: center
        :alt: JL's build stage I
        :figclass: align-center
        :width: 80%

#. 使用方式,杰理包管理器界面如下图所示

    .. attention::
      并不是说有包都有执行按钮。这是因为有一些包里面没有可执行程序。

#. 安装软件包,也可以单独选择特定的包安装。

    .. caution::
      如果下载安装过的软件被破坏了、或者出现了缺失。可以点击“校验”来校验是否出现缺失或者破损，并从服务器中下载安装对应的正确文件。

配置工具使用
*******************
#. 打开sdk工程目录，进入cbp_out\cpu\*CPU*\tools\*CHIP*_config_tool目录；

#. 双击【AC697N-配置工具入口.jlxproj】，打开【杰理SDK工具】


【杰理SDK配置工具】界面说明
----------------------------

.. note::
    编辑fw文件有以下几点需要注意：

    #. 板级配置的可配选项取决cfg_tool.bin文件，也就是说编译前配置选了什么，编辑fw文件就有什么配置，比如说编译前配置是选了3个key，则编辑fw文件的时候也是只有3个key的选项。
    #. fw版本号控制，只有工具和fw的版本号对得上，才能编辑对应的fw文件，版本号在AC697N_config_tool\conf\entry 目录下的user_cfg.lua文件下修改，如下图：
    
    如果版本号提示不对，请确认版本号。

#. 编辑FW文件：点击【编辑FW文件】，可对一个FW文件的进行编辑，修改FW文件的板级配置、蓝牙配置，状态配置和提示音配置，界面如下:

    .. code-block:: none

       点击`恢复默认值`，可以恢复sdk发布时的原始配置，配置完成后，
       点击`保存`，可选择保存路径保存修改过后的fw和ufw文件。

#. fw文件制作：当fw文件测试没有问题后，想发布一个可编辑的fw文件时，把生成的fw文件替换AC697N_config_tool\conf\output\default 目录下default_cfg.fw文件即可

#. 默认值的制作：用编译前选项配置好后，点击保存后会在AC697N_config_tool\conf\output生成一个default_cfg.lua文件，把该文件覆盖AC697N_config_tool\conf\output\default目录下的default_cfg.lua文件，到时在编辑fw文件的时候点击恢复默认设置，就会恢复之前设置的值。

程序升级
********

通过**USB 升级工具**连接到开发板，并按照说明使用 :ref:``

.. _help:

关于帮助
********

开发者可以通过邮件或Github issuses 形式进行提问，请上传bug reports 或功能需求到Github。

* **邮件**: users@lists.jieli.org 是获得帮助的最佳形式. `Search archives and sign up here`_.

* **GitHub**: 使用 `GitHub issues`_ 进行bugs and feature requests.

.. _GitHub issues: https://github.com/Jieli-Tech/fw-AC63_BT_SDK/issues

如何提问
==========

.. important::

   提问前，请先查阅文档 :ref:`faq`，可能你的答案已经存在。

请不要使用过于简略的描述方法，如“这不能工作” 或者“这是否工作正常”。描述内容尽可能的包括以下细节：

#. 你的使用目的
#. 你已经尝试过那些操作
#. 对现象的详细描述，如有log 提供将会更好
#. 所使用的SDK 版本
#. 问题出现条件，频率（可选）

提问内容格式
==============
请使用 **复制/粘贴 文本** 的形式来进行问题描述，包含代码片段，log 输出，尽量避免使用拍照形式。

这样将会让协助解决问题的工程师更高效的了解问题，同时有助于帮助其他开发者提问前进行搜索。

