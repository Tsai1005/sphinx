.. _sdk_release_notes:

发布版本信息
#############

杰理开源项目提供工具链，源代码，开发和量产工具支持，而非turn-key 方案，项目由市场
和开发者需求驱动更新，迭代时间根据收集需求而定。

所有的杰理开源项目均维护在 `Github仓库`_ 和 `Gitee仓库`_ 。

开源项目内，同时可以使用Git clone 下载或者直接下载压缩包 tar.gz 文件，请使用 *Github releases*
进行下载。


项目的技术文档也符合一个标记
特定的版本,可以在 https://docs.zephyrproject.org/找到。

.. comment We need to split the globbing of release notes to get the
   single-digit and double-digit subversions sorted correctly.  Specify
   names in normal order and use the :reversed: option to reverse it.
   This will get us through 10 subversions (0-9) before we need to
   update this list for two-digit subversions again.

.. toctree::
   :maxdepth: 1
   :glob:
   :reversed:

   release-notes-1.?
   release-notes-1.*
   release-notes-*

.. _`Github仓库`: https://github.com/Jieli-Tech
.. _`Gitee仓库`: https://gitee.com/Jieli-Tech

