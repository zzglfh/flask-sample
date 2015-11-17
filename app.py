#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-15 00:10:41
# @Author  : zheng guang (zzglfh@gmail)
# @Link    : 
# @Version : $Id$

import flaskr

#flaskr.app.debug=False
flaskr.app.logger.setLevel("DEBUG")
flaskr.run()
#TODO　
'''
1.test http://dormousehole.readthedocs.org/en/latest/testing.html#testing
2.db config http://dormousehole.readthedocs.org/en/latest/patterns/sqlalchemy.html
3.env config
4.security http://dormousehole.readthedocs.org/en/latest/patterns/urlprocessors.html
5. build http://dormousehole.readthedocs.org/en/latest/patterns/distribute.html

6.restful http://flask-restful.readthedocs.org/en/0.3.4/
'''