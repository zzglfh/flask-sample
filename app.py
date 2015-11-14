__author__ = 'zzg'
import flaskr

flaskr.app.logger.setLevel("DEBUG")
flaskr.app.run(host="0.0.0.0")