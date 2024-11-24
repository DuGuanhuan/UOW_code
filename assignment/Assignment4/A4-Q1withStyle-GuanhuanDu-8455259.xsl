<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/loginReport">
        <html>
            <head>
                <title>Login Report</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    h1 { color: #333; }
                    h2 { color: #555; }
                    h3 { color: #777; }
                    ul { list-style-type: none; padding: 0; }
                    li { margin: 5px 0; }
                </style>
            </head>
            <body>
                <h1>Login Report <xsl:value-of select="@date"/></h1>
                <h2>Device name: <xsl:value-of select="device/@name"/></h2>
                <xsl:for-each select="user">
                    <h3>Username: <xsl:value-of select="username"/></h3>
                    <p>Name: <xsl:value-of select="name"/></p>
                    <p>Group: <xsl:value-of select="group"/></p>
                    <h4>Login:</h4>
                    <ul>
                        <xsl:for-each select="login/entry">
                            <li>
                                <xsl:value-of select="@date"/> <xsl:value-of select="@time"/>: <xsl:value-of select="@status"/>
                            </li>
                        </xsl:for-each>
                    </ul>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>