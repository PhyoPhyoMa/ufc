# -*- coding: utf-8 -*-
import re


def replace(input):

	output = input

	output = output.replace(u'\u1000', u'\u0075')#kagyi
	output = re.sub(u'\u1001', u'\u0063', output)#ka_kway
	output = output.replace(u'\u1002', u'\u002A',)#ga_nge
	output = re.sub(u'\u1003', u'\u0043', output)#ga_gyi
	output = re.sub(u'\u1004', u'\u0069', output)#ng
	output = re.sub(u'\u1005', u'\u0070', output)#sa_lone
	output = re.sub(u'\u1006', u'\u0071', output)#sa_lane
	output = re.sub(u'\u1007', u'\u005A', output)#za_gwe
	output = re.sub(u'\u1009', u'\u00DA', output)#nya_lay
	output = re.sub(u'\u100A', u'\u006E', output)#nya
	output = re.sub(u'\u100B', u'\u0023', output)#tatalinjade
	output = re.sub(u'\u100C', u'\u0058', output)#htawonbae
	output = re.sub(u'\u100D', u'\u0021', output)#dayinkaut
	output = re.sub(u'\u100E', u'\u00A1', output)#dayinmot
	output = re.sub(u'\u100F', u'\u0050', output)#nagyi
	output = re.sub(u'\u1010', u'\u0077', output)#ta_won_bu
	output = re.sub(u'\u1011', u'\u0078', output)#hta_sin_htoo
	output = re.sub(u'\u1012', u'\u0027', output)#da_dwe
	output = re.sub(u'\u1013', u'\u0022', output)#da_ot_chite
	output = re.sub(u'\u1014', u'\u0065', output)#na
	output = re.sub(u'\u1015', u'\u0079', output)#pa_south
	output = re.sub(u'\u1016', u'\u007A', output)#fa_ot_htoke
	output = re.sub(u'\u1017', u'\u0041', output)#ba_lat_chite
	output = re.sub(u'\u1018', u'\u0062', output)#ba_gone
	output = re.sub(u'\u1019', u'\u0072', output)#ma
	output = re.sub(u'\u101A', u'\u002C', output)#ya_palat
	output = re.sub(u'\u0026', u'\u101B', output)#ya_kaut
	output = re.sub(u'\u101C', u'\u0076', output)#la
	#output = re.sub(u'\0030', u'\u101D', output)#wa
	output = re.sub(u'\u101E', u'\u006F', output)#tha
	output = output.replace(u'\u101F', u'\u005B',)#ha
	output = re.sub(u'\u1020', u'\u0056', output)#lagyi
	output = re.sub(u'\u1021', u'\u0074', output)#A
	output = re.sub(u'\u1023', u'\u00A3', output)#ei
	output = re.sub(u'\u1024', u'\u00FE', output)#eii
	output = re.sub(u'\u1025', u'\u004F', output)#atkara u
	output = re.sub(u'\u1027', u'\u007B', output)#a
	output = re.sub(u'\u102B', u'\u0067', output)#yay_cha ashay
	output = re.sub(u'\u102C', u'\u006D', output)#yay_cha ato
	output = re.sub(u'\u102D', u'\u0064', output)#lone_gyi_tin
	output = re.sub(u'\u102E', u'\u0044', output)#lone_gyi_tin_san_kat
	output = re.sub(u'\u102F', u'\u004B', output)#ta_chaung_ngin
	output = re.sub(u'\u1030', u'\u004C', output)#2_chaung_ngin
	output = re.sub(u'\u1031', u'\u0061', output)#tha_wai_htoe
	output = re.sub(u'\u1032', u'\u004A', output)#naut_htoe_myint
	output = re.sub(u'\u1036', u'\u0048', output)#ta_ta_tin
	output = re.sub(u'\u1037', u'\u0055', output)#aut_myint
	output = re.sub(u'\u1038', u'\u003B', output)#wit_sa_2_lone_paut
	output = re.sub(u'\u103A', u'\u0066', output)#athat
	output = re.sub(u'\u103B', u'\u0073', output)#ya_pint
	output = re.sub(u'\u103C', u'\u006A', output)#yayit
	output = re.sub(u'\u103D', u'\u0047', output)#waswe
	output = re.sub(u'\u103E', u'\u0053', output)#ha_htoe
	output = re.sub(u'u103F', u'\u00F3', output)#tha_gyi
	output = output.replace(u'\u104A', u'\u003F',)#paut_ka_lay
	output = re.sub(u'\u104B', u'\u002F', output)#paut_ma
	output = re.sub(u'\u104D', u'\u00ED', output)#atkara_yaut
	output = re.sub(u'\u104E', u'\u00A4', output)#la_kaung
	output = output.replace(u'\u104F', u'\u005C')#atkara_ei
	output = re.sub(u'\u102B\u103A', u'\u003A', output)  # yay_cha_athat
	output = re.sub(u'\u103D\u103E', u'\u0054', output)#waswe_hahtoe
	output = re.sub(u'\u103E\u102F', u'\u0049', output)#hahtoe_1chaung
	output = re.sub(u'\u103E\u1030', u'\u00AA', output)#hahtoe_2chaung
	#----------------------------------------------------
	output = re.sub(u'\u103C\u103D', u'\u003E', output)#yayit_waswe
	output = re.sub(u'\u103C\u102F', u'\u00FB', output)#yayit_tachaungngin
	output = re.sub(u'\u103B\u103E', u'\u0051', output)#yapint_hahtoe
	output = re.sub(u'\u103B\u103D', u'\u0052', output)#yapint_waswe
	output = re.sub(u'\u103B\u103D\u103E', u'\u0057', output)#yapint_waswe_hahtoe


	return output

def logical2visual(input):
	output = input
	#place
	output = re.sub(u'([\u1000-\u1021])((?:\u103C)?)((?:\u103B)?)((?:\u103D)?)((?:\u103E)?)((?:\u1031)?)((?:\u102C)?)','\\6\\2\\1\\3\\4\\5\\7', output)
	return output

def precompose(input):
	output = input
	#pa_sint
	output = re.sub(u'\u1039\u1000', u'\u00FA', output)#kagyi
	output = re.sub(u'\u1039\u1001', u'\u00A9', output)#ka_kway
	output = re.sub(u'\u1039\u1002', u'\u00BE', output)#ga_nge
	output = re.sub(u'\u1039\u1003', u'\u00A2', output)#gagyi
	output = re.sub(u'\u1039\u1005', u'\u00F6', output)#sa_lone
	output = re.sub(u'\u1039\u1006', u'\u00E4', output)#sa_lane
	output = re.sub(u'\u1039\u1007', u'\u00C6', output)#za_gwe
	output = re.sub(u'\u1039\u1008', u'\u00D1', output)#za_myin_zwe
	output = re.sub(u'\u1039\u100B', u'\u00B3', output)#tatalinjade
	output = re.sub(u'\u1039\u100C', u'\u00B2', output)#htawonbae
	output = re.sub(u'\u100D\u1039\u100D', u'\u00D7', output)#dayinkaut
	output = re.sub(u'\u100E\u1039\u100D', u'\u00B9', output)#dayinmot
	output = re.sub(u'\u1039\u100F', u'\u00D6', output)#nagyi
	output = re.sub(u'\u1039\u1010', u'\u00C5', output)#da_won_bu
	output = re.sub(u'\u1039\u1011', u'\u00A6', output)#hta_sin_htoo
	output = re.sub(u'\u1039\u1012', u'\u00B4', output)#da_dwe
	output = re.sub(u'\u1039\u1013', u'\u00A8', output)#da_ot_chite
	output = re.sub(u'\u1039\u1014', u'\u00E9', output)#na
	output = re.sub(u'\u1039\u1015', u'\u00DC', output)#pa_south
	output = re.sub(u'\u1039\u1016', u'\u006E', output)#fa_ot_htoke
	output = re.sub(u'\u1039\u1017', u'\u00C1', output)#ba_lat_chite
	output = re.sub(u'\u1039\u1018', u'\u00C7', output)#ba_gone
	output = re.sub(u'\u1039\u1019', u'\u00AE', output)#ma
	output = re.sub(u'\u1039\u101C', u'\u0019', output)#la
	#ngr_sint
	output = re.sub(u'([\u1000-\u1021])\u0046', u'\u0046\\1',output)
	output = re.sub(u'\u1004\u103A\u1039', u'\u0046', output)
	output = re.sub(u'([\u1000-\u1021])\u0046\u102d', u'\\1\u00D8', output)#with lone_gyi_tin
	output = re.sub(u'([\u1000-\u1021])\u0046\u102e', u'\\1\u00D0', output)#with lone_gyi_tin_san_khat
	output = re.sub(u'([\u1000-\u1021])\u0046\u1036', u'\\1\u00F8', output)#with ta_ta_tin
	output = re.sub(u'\u102d\u1036', u'\u00F0', output)#lone_gyi_tin_ta_ta_tin
	return output

def shape(input):
	output = input
	#yayit

	#output = re.sub(u'\u103B([\u1000])', u'\u107E\\1', output)#yayit(107E)
	#output = re.sub(u'\u107E([\u1000-\u1021])([\u102D\u102E\u1036])', u'\u1080\\1\\2', output)  # yait(1080)
	#output = re.sub(u'\u103B([\u1000-\u1021])([\u102D\u102E\u1036])', u'\u107F\\1\\2', output)#yayiy(107F)

	#ta_chaung_ngin
	#output = re.sub(u'([\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084])([\u1000-\u1021])((?:[\u102D\u102E\u1036])?)\u102F', u'\\1\\2\\3\u1033', output)#with yayit
	#output = re.sub(u'([\u103A\u107D])((?:[\u102D\u102E\u1036])?)\u102F', u'\\1\\2\u1033', output)#with yapint
	#output = re.sub(u'\u103D\u102F', u'\u1088', output)#with hahtoe

	#ta_chaung_ngin with pa_sint
	#output = re.sub(u'([\u1060-\u1063])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
	#output = re.sub(u'([\u1065-\u1069])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
	#output = re.sub(u'([\u106C\u106D])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
	#output = re.sub(u'([\u1070-\u107C])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
	#output = re.sub(u'([\u1085\u1093])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)

	# 2_chaung_ngin
	#output = re.sub(u'([\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084])([\u1000-\u1021])((?:[\u102D\u102E\u1036])?)\u1030',u'\\1\\2\\3\u1034', output)  # with yayit
	#output = re.sub(u'([\u103A\u107D])((?:[\u102D\u102E\u1036])?)\u1030', u'\\1\\2\u1034', output)  # with yapint
	#output = re.sub(u'\u103D\u1030', u'\u1089', output)  # with hahtoe

	#yapint
	#output = re.sub(u'\u103A([\u103C\u103D])', u'\u107D\\1', output)

	#aut_myint
	#output = re.sub(u'([\u1014\u101B\u1008\u1030\u1033\u102F\u1034])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1094', output)
	#output = re.sub(u'([\u103C\u103D\u108A\u1088])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1095', output)

	#na_nge
	#output = re.sub(u'\u1014([\u103C\u103D\u108A])', u'\u108F\\1', output)

	#na_nge with pr_sint
	#output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1060-\u1063])', u'\u108F\\1\\2', output)
	#output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1065-\u1069])', u'\u108F\\1\\2', output)
	#output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u106C\u106D])', u'\u108F\\1\\2', output)
	#output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1070-\u107C])', u'\u108F\\1\\2', output)
	#output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1085\u1093])', u'\u108F\\1\\2', output)

	#hahtoe
	#output = re.sub(u'(\u100A)\u103D', u'\\1\u1087', output)#with nya

	# nya_lay
	#output = re.sub(u'\u1009(\u1039)', u'\u1025\\1', output)

	#ya_kaut
	#output = re.sub(u'\u101B\u108A', u'\u1090\u108A', output)#with waswe and waswe_hahtoe
	#output = re.sub(u'\u101B\u102F', u'\u1090\u102F', output)#with ta_chaung_ngin

	# ya_kaut with pr_sint
	#output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1060-\u1063])', u'\u1090\\1\\2', output)
	#output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1065-\u1069])', u'\u1090\\1\\2', output)
	#output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u106C\u106D])', u'\u1090\\1\\2', output)
	#output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1070-\u107C])', u'\u1090\\1\\2', output)
	#output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1085\u1093])', u'\u1090\\1\\2', output)


	return output



def convert(input):

	output = input

	output = logical2visual(output)
	output = shape(output)
	output = replace(output)
	output = precompose(output)


	return output
