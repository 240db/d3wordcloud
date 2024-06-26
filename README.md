# d3wordcloud
A simple Jupyter (Lab/Notebook) wrapper of Jason Davies d3 JS wordcloud generator https://www.jasondavies.com/wordcloud/

![image](https://user-images.githubusercontent.com/47481567/191727287-f7ff45ea-2ded-4dcd-a8fb-435bc2183d42.png)

## Installation 
`pip install d3wordcloud` 

## Usage 

### Function save_wordcloud()
Input: text
Output: HTML File export 
i.e.

```python
import d3wordcloud as d3wc
d3wc.save_wordcloud(df.topics.unique()[2])
```

You can then load this in gradio using Markdown embedded as a link or try using gr.HTML(). A custom iframe should work too


### Function display_wordcloud()
Input: text, boolean for show_settings
Output: An interactive SVG wordcloud right in your Jupyter Notebook (or Jupyter Lab).

```python
import d3wordcloud as d3wc
d3wc.display_wordcloud(sample_data, show_settings=False)
```
- `sample_data` is a space-separated string, e.g. `"energy fossil fuel EU"`
- `show_settings` shows the original settings for interactive control in your notebook, just like in the [original version](https://www.jasondavies.com/wordcloud/)

![image](https://user-images.githubusercontent.com/47481567/191727836-05fbe1bd-d4b0-425f-9856-42b3addd4ab2.png)

## Settings
If you'd like to use all the customization the library offers, either use the manual mode or build a modified wheel yourself. 
For the manual mode, simply copy the `manual` folder with the two files to your working directory and edit the html template directly.

## Building the installable Python wheel yourself
1. `git clone https://github.com/do-me/d3wordcloud.git`
2. `cd d3wordcloud`
3. `python setup.py sdist`
4. `tar tzf dist/d3wordcloud-0.0.1.tar.gz`
5. `python setup.py bdist_wheel sdist`
6. `cd dist`
7. `pip install d3wordcloud-0.0.1-py3-none-any.whl`

Uninstalling is as easy as 

`pip uninstall d3wordcloud-0.0.1-py3-none-any.whl`

## Troubleshooting
If you are using a virtual env (like conda env) and the wordcloud SVG is not showing it is probably related to a [Jupyter bug](https://github.com/jupyter-widgets/ipywidgets/issues/2257). A possible workaround is [working in just one notebook at a time](https://github.com/jupyter-widgets/ipywidgets/issues/2257#issuecomment-1270112153)

## To Do
- add probabilities (percentage) parameter so that we can fit LDA models and the top words percentages to control the size of each word
- Port all the settings for full control in Python. 
