# -*- coding: utf-8 -*-
import re


def replace(input):

	output = input

	output = output.replace(u'\u0075', u'\u1000')#kagyi
	output = re.sub(u'\u0063', u'\u1001', output)#ka_kway
	#output = re.sub(u'\u002A', u'\u1002', output)#ga_nge
	output = re.sub(u'\u0043', u'\u1003', output)#ga_gyi
	output = re.sub(u'\u0069', u'\u1004', output)#ng
	output = re.sub(u'\u0070', u'\u1005', output)#sa_lone
	output = re.sub(u'\u0071', u'\u1006', output)#sa_lane
	output = re.sub(u'\u005A', u'\u1007', output)#za_gwe
	output = re.sub(u'\u00DA', u'\u1009', output)#nya_lay
	output = re.sub(u'[\u006E\u00F1]', u'\u100A', output)#nya
	output = re.sub(u'\u0023', u'\u100B', output)#tatalinjade
	output = re.sub(u'\u0058', u'\u100C', output)#htawonbae
	output = re.sub(u'\u0021', u'\u100D', output)#dayinkaut
	output = re.sub(u'\u00A1', u'\u100E', output)#dayinmot
	output = re.sub(u'\u0050', u'\u100F', output)#nagyi
	output = re.sub(u'\u0077', u'\u1010', output)#ta_won_bu
	output = re.sub(u'\u0078', u'\u1011', output)#hta_sin_htoo
	output = re.sub(u'\u0027', u'\u1012', output)#da_dwe
	output = re.sub(u'\u0022', u'\u1013', output)#da_ot_chite
	output = re.sub(u'\u0065', u'\u1014', output)#na
	output = re.sub(u'\u0079', u'\u1015', output)#pa_south
	output = re.sub(u'\u007A', u'\u1016', output)#fa_ot_htoke
	output = re.sub(u'\u0041', u'\u1017', output)#ba_lat_chite
	output = re.sub(u'\u0062', u'\u1018', output)#ba_gone
	output = re.sub(u'\u0072', u'\u1019', output)#ma
	output = re.sub(u'\u002C', u'\u101A', output)#ya_palat
	output = re.sub(u'\u0026', u'\u101B', output)#ya_kaut
	output = re.sub(u'\u0076', u'\u101C', output)#la
	output = re.sub(u'\u0030', u'\u101D', output)#wa
	output = re.sub(u'\u006F', u'\u101E', output)#tha
	#output = re.sub(u'\u005B', u'\u101F', output)#ha
	output = re.sub(u'\u0056', u'\u1020', output)#lagyi
	output = re.sub(u'\u0074', u'\u1021', output)#A
	output = re.sub(u'\u00A3', u'\u1023', output)#ei
	output = re.sub(u'\u00FE', u'\u1024', output)#eii
	output = re.sub(u'\u004F', u'\u1025', output)#atkara u
	output = re.sub(u'\u007B', u'\u1027', output)#a
	output = re.sub(u'\u0067', u'\u102B', output)#yay_cha ashay
	output = re.sub(u'\u006D', u'\u102C', output)#yay_cha ato
	output = re.sub(u'\u0064', u'\u102D', output)#lone_gyi_tin
	output = re.sub(u'\u0044', u'\u102E', output)#lone_gyi_tin_san_kat
	output = re.sub(u'[\u004B\u006B]', u'\u102F', output)#ta_chaung_ngin
	output = re.sub(u'[\u004C\u006C]', u'\u1030', output)#2_chaung_ngin
	output = re.sub(u'\u0061', u'\u1031', output)#tha_wai_htoe
	output = re.sub(u'\u004A', u'\u1032', output)#naut_htoe_myint
	output = re.sub(u'\u0048', u'\u1036', output)#ta_ta_tin
	output = re.sub(u'[\u0055\u0059\u0068]', u'\u1037', output)#aut_myint
	output = re.sub(u'\u003B', u'\u1038', output)#wit_sa_2_lone_paut
	output = re.sub(u'\u0066', u'\u103A', output)#shay_htoe
	output = re.sub(u'00DF', u'\u103B', output)#ya_pint
	output = re.sub(u'[\u0042\u004D\u004E\u0060\u006A\u007E\u00EA]', u'\u103C', output)#yayit
	output = re.sub(u'\u0047', u'\u103D', output)#waswe
	output = re.sub(u'[\u0053\u00A7]', u'\u103E', output)#ha_htoe
	output = re.sub(u'\u00F3', u'u103F', output)#tha_gyi
	#output = re.sub(u'\u003F', u'\u104A', output)#paut_ka_lay
	output = re.sub(u'\u002F', u'\u104B', output)#paut_ma
	output = re.sub(u'\u00ED', u'\u104D', output)#atkara_yaut
	output = re.sub(u'\u00A4', u'\u104E', output)#la_kaung
	#output = re.sub(u'\u005C', u'\u104F', output)#atkara_ei

	return output

def visual2logical(input):
	output = input
	#place
	output = re.sub(u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103D)?)((?:\u103B)?)((?:\u103E)?)((?:\u102C)?)', u"\\3\\2\\5\\4\\6\\1\\7", output);
	return output

def convert(input):

	output = input

	output = replace(input)
	output = visual2logical(output)

	return output
