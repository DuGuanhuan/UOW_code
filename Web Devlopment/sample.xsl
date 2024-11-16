<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- 指定输出为 HTML 格式 -->
    <xsl:output method="html"/>

    <!-- 模板匹配根节点 -->
    <xsl:template match="/">
        <html>
            <head>
                <title>Greeting</title>
            </head>
            <body>
                <!-- 显示 message 元素的内容 -->
                <h1><xsl:value-of select="greeting/message"/></h1>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>