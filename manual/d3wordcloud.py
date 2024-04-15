from IPython.display import display, HTML

def save_wordcloud(text):
    with open('d3wordcloud-template.html') as file:
        wc = file.read().replace("$text",text)
    with open('./saving.html', 'rw+') as f:
        f.write(wc)
        f.close


def display_wordcloud(text, show_settings=False):
    with open('d3wordcloud-template.html') as file:
        wc = file.read().replace("$text",text)
        if show_settings == False: # hidden=true doesn't work for some reason
            wc = wc.replace("""<form id="form" style="">""","""<form id="form" style="display:none">""")        
    display(HTML(wc))
