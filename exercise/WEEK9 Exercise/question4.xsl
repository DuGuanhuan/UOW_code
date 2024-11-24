question4.xsl<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Enrolment Statistics</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    h1 { text-align: center; }
                    table { width: 80%; margin: 20px auto; border-collapse: collapse; }
                    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <h1>Enrolment Statistics</h1>
                <p>Campus: <xsl:value-of select="@campus"/></p>
                <p>Year: <xsl:value-of select="@year"/></p>
                <p>Session: <xsl:value-of select="@session"/></p>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Subject</th>
                        <th>Enrol</th>
                        <th>Withdrawn</th>
                    </tr>
                    <xsl:for-each select="audit/subject">
                        <tr>
                            <td><xsl:value-of select="@sid"/></td>
                            <td><xsl:value-of select="code"/>: <xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="statistics/enrol"/></td>
                            <td><xsl:value-of select="statistics/withdrawn"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>