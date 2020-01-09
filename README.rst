一、Chatbot_Help介绍
==========================

    Chatbot_Help是一个接入机器人的第三方扩展工具，提供一系列相关api来将自己开发的机器人（Chatbot）接入到相关外部平台，实现与用户的交互

目前，Chatbot_Help支持的第三方平台有：

1、钉钉群：

2、微信公众号；

3、QQ群；

4、外部平台：如电商平台、网页端等


二、安装使用
============

::

    pip install Chatbot_Help



三、各消息类型使用示例
======================

1、dingtalk

    import chatbot_help as ch
    from chatbot_help import DingtalkChatbot

    print(ch.__version__)                # 打印版本信息
    dtalk = DingtalkChatbot(webhook)     # 你设置群机器人的时候生成的webhook

详情请参考：`Dingtalk_README`_

四、Update News
======================

    * 2020.1.7  接入钉钉群，支持主动推送消息、outgoing交互

    * 2020.1.9  接入微信





五、Resources
======================

.. _`Dingtalk_README`：https://github.com/charlesXu86/Chatbot_Help/blob/master/Dingtalk_README.rst
