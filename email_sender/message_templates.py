from string import Template

SUBJECT = "Temat wiadomości"

MESSAGE_TEMPLATE_TEXT = Template("""\
    Hi $name, 
    Template message


    Remember to visit my site
    http://cv.retip1994.usermd.net/""")

MESSAGE_TEMPLATE_HTML = Template("""\
    <html>
      <body>
        <p>Hi $name,<br>
            <h2>Template message</h2>
           Remember to visit my site<br>
           <a href="http://cv.retip1994.usermd.net/">Piotr Piekielny</a>
        </p>
      </body>
    </html>
    """)
