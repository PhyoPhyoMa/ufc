# -*- coding: utf-8 -*-
import re


def convert(input):
	output = input

	output = output.replace(u'\u106A', u'\1009')
	output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]',u'\u103C',output)#yayit
	output = re.sub(u'[\u103A\u107D]',u'\u103B',output)#yapint
	output = re.sub(u'[\u106B]',u'\u100A',output)#nya
	output = re.sub(u'[\u108F]',u'\u1014',output)#na
	output = re.sub(u'\u1097', u'\u100B',output)#tatalinjade
	output = re.sub(u'\u1092', u'\u100C',output)#htawonbae
	output = re.sub(u'\u1090', u'\u101B',output)#yakaut
	output_text = re.sub(u'(\u103c)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)', '\\2\\3\\1', output)#waswe

	return output