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
                    .result { margin: 20px; }
                </style>
            </head>
            <body>
                <h1>Exam result</h1>
                <div class="result">
                    <p>Reference number: <xsl:value-of select="@ref"/></p>
                    <p>Exam number: <xsl:value-of select="examId"/></p>
                    <p>Contestant number: <xsl:value-of select="contestantId"/></p>
                    <p>Digital signature: <xsl:value-of select="digitalSignature"/></p>
                    <p>Score: <xsl:value-of select="score"/></p>
                    <p>Band: <xsl:value-of select="band"/></p>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>