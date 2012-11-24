# -- coding: utf8 --
import sys
import os
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath)
#os.chdir(abspath)

#sys.path.append('/Users/rabbit/Documents/Proj/post_bar')
#os.chdir('/Users/rabbit/Documents/Proj/post_bar')
import web
from config.config import *
from config.urls import *
from libraries import widget
from libraries import helper
from models.site_model import *

#web.template.Template.globals['render'] = render
#web.template.Template.globals['site_title'] = site_title
web.template.Template.globals['widget'] = widget
web.template.Template.globals['site_options'] = site_model().get_options()
web.template.Template.globals['helper'] = helper

app = web.application(urls, globals(), autoreload = True)

if web.config.get('_session') is None:
    #session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user_id': None})
    curdir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(curdir,'sessions')), initializer={'user_id': None})
    web.config._session = session
else:
    session = web.config._session
    
# 如果这里不 不将 session 赋值给模板全局变量， 模板中将不能得到此变量
web.template.Template.globals['session'] = session
web.template.Template.globals['site_url'] = 'http://post_bar.localhost'
application = app.wsgifunc()
#if __name__ == "__main__":
#    app.run()