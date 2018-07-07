# -*- coding: utf-8 -*-

import re


def replace(input):
	output = input

	output = re.sub(u'\u103A', u'\u1039',output)#athat
	output = re.sub(u'\u103B', u'\u103A',output)#yapint
	output = re.sub(u'\u103C', u'\u103B',output)#yayit
	output = re.sub(u'\u103D', u'\u103C',output)#waswe
	output = re.sub(u'\u103E', u'\u103D',output)#hahtoe
	output = re.sub(u'\u103F', u'\u1086',output)#tagyi
	#output = re.sub(u'\u102F', u'\u1033',output)#ta_chaung_ngin
	#output = re.sub(u'\u1030', u'\u1034',output)#2chaung_ngin

	return output

def precompose(input):
	output = input

	# ngr_sint
	output = re.sub(u'\u1004\u103A\u1039', u'\u1064', output)
	output = re.sub(u'(\u1064)([\u1000-\u1021])', u'\\2\\1', output)

	#pa_sint
	output = re.sub(u'\u1039\u1000', u'\u1060', output)  # kagyi
	output = re.sub(u'\u1039\u1001', u'\u1061', output)  # ka_kway
	output = re.sub(u'\u1039\u1002', u'\u1062', output)  # ga_nge
	output = re.sub(u'\u1039\u1003', u'\u1063', output)  # gagyi
	output = re.sub(u'\u1039\u1005', u'\u1065', output)  # sa_lone
	output = re.sub(u'\u1039\u1006', u'\u1066', output)  # sa_lane
	output = re.sub(u'\u1039\u1007', u'\u1068', output)  # za_gwe
	output = re.sub(u'\u1039\u1008', u'\u1069', output)  # za_myin_zwe
	output = re.sub(u'\u1039\u100B', u'\u106C', output)  # tatalinjade
	output = re.sub(u'\u1039\u100C', u'\u106D', output)  # htawonbae
	output = re.sub(u'\u100D\u1039\u100D', u'\u106E', output)  # dayinkaut
	output = re.sub(u'\u100E\u1039\u100D', u'\u106F', output)  # dayinmot
	output = re.sub(u'\u1039\u100F', u'\u1070', output)  # nagyi
	output = re.sub(u'\u1039\u1010', u'\u1071', output)  # da_won_bu
	output = re.sub(u'\u1039\u1011', u'\u1073', output)  # hta_sin_htoo
	output = re.sub(u'\u1039\u1012', u'\u1075', output)  # da_dwe
	output = re.sub(u'\u1039\u1013', u'\u1076', output)  # da_ot_chite
	output = re.sub(u'\u1039\u1014', u'\u1077', output)  # na
	output = re.sub(u'\u1039\u1015', u'\u1078', output)  # pa_south
	output = re.sub(u'\u1039\u1016', u'\u1079', output)  # fa_ot_htoke
	output = re.sub(u'\u1039\u1017', u'\u107A', output)  # ba_lat_chite
	output = re.sub(u'\u1039\u1018', u'\u107B', output)  # ba_gone
	output = re.sub(u'\u1039\u1019', u'\u107C', output)  # ma
	output = re.sub(u'\u1039\u101C', u'\u1085', output)  # la


	return output

def logical2visual(input):
	output = input

	# 1=letters,
	output = re.sub(u'([\u1000-\u1021])((?:\u103B)?)((?:\u103A)?)((?:\u103C)?)((?:\u103D)?)((?:\u1031)?)((?:\u102C)?)', '\\6\\2\\1\\3\\4\\5\\7', output)

	return output

def convert(input):
	output = input

	output = precompose(output)
	output = replace(output)
	output = logical2visual(output)
	return output
