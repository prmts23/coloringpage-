#Download  coloring page from Duck Duck go 
#download some image from https://pluscoloring.com/

from duckduckgo_search import ddg_images
keywords = "Disney coloring Page"
ddg_images(keywords, region='wt-wt', safesearch='Off', size='Medium',
 color='Monochrome', type_image=None, layout=None, license_image=None, max_results=150,
              download=(bool,keywords))
