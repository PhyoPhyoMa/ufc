# -*- coding: utf-8 -*-
import re


def convert(input):

	output = input

	output = output.replace(u'\u106A', u'\u1009')
	output = re.sub(u'[\u103D\u1087]', u'\u103E',output)#hahtoe
	output = re.sub(u'\u103C', u'\u103D',output)#waswe
	output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]',u'\u103C',output)#yayit
	output = re.sub(u'[\u103A\u107D]',u'\u103B',output)#yapint
	output = re.sub(u'[\u106B]',u'\u100A',output)#nya
	output = re.sub(u'[\u108F]',u'\u1014',output)#na
	output = re.sub(u'\u1097', u'\u100B',output)#tatalinjade
	output = re.sub(u'\u1092', u'\u100C',output)#htawonbae
	output = re.sub(u'\u1090', u'\u101B',output)#yakaut
	output = re.sub(u'\u1033', u'\u102F',output)#ta_chaung_ngin
	output = re.sub(u'\u1034', u'\u1030',output)#2chaung_ngin
	output = re.sub(u'\u1086', u'\u103F',output)#tagyi
	output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038',output)#laguang
	output = re.sub(u'\u1039', u'\u103A',output)#nga_tat
	output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037',output)#aut_myit
	#pa_sint
	#place
	output = re.sub(u'((?:\u103C)?)([\u1000-\u1021])', u"\\2\\1",output);
	return output