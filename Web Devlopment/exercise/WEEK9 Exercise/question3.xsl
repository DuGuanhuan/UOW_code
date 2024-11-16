<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Exam result</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    h1 { text-align: center; }
                    table { width: 50%; margin: 20px auto; border-collapse: collapse; }
                    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                    .digital-signature { color: maroon; }
                </style>
            </head>
            <body>
                <h1>Exam result</h1>
                <table>
                    <tr>
                        <th>Reference number</th>
                        <td><xsl:value-of select="@ref"/></td>
                    </tr>
                    <tr>
                        <th>Exam number</th>
                        <td><xsl:value-of select="examId"/></td>
                    </tr>
                    <tr>
                        <th>Contestant number</th>
                        <td><xsl:value-of select="contestantId"/></td>
                    </tr>
                    <tr>
                        <th>Digital signature</th>
                        <td class="digital-signature"><xsl:value-of select="digitalSignature"/></td>
                    </tr>
                    <tr>
                        <th>Score</th>
                        <td><xsl:value-of select="score"/></td>
                    </tr>
                    <tr>
                        <th>Band</th>
                        <td><xsl:value-of select="band"/></td>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>