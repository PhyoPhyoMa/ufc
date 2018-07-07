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

    #pa_sint
    output = re.sub(u'\u1039\u1000', u'\u1060', output)  # kagyi
    output = re.sub(u'\u1039\u1001',u'\u1061', output)  # ka_kway
    output = re.sub(u'\u1062', u'\u1039\u1002', output)  # ga_nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output)  # gagyi
    output = re.sub(u'\u1065', u'\u1039\u1005', output)  # sa_lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output)  # sa_lane
    output = re.sub(u'\u1068', u'\u1039\u1007', output)  # za_gwe
    output = re.sub(u'\u1069', u'\u1039\u1008', output)  # za_myin_zwe
    output = re.sub(u'\u106C', u'\u1039\u100B', output)  # tatalinjade
    output = re.sub(u'\u106D', u'\u1039\u100C', output)  # htawonbae
    output = re.sub(u'\u106E', u'\u100D\u1039\u100D', output)  # dayinkaut
    output = re.sub(u'\u106F', u'\u100E\u1039\u100D', output)  # dayinmot
    output = re.sub(u'\u1070', u'\u1039\u100F', output)  # nagyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output)  # da_won_bu
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output)  # hta_sin_htoo
    output = re.sub(u'\u1075', u'\u1039\u1012', output)  # da_dwe
    output = re.sub(u'\u1076', u'\u1039\u1013', output)  # da_ot_chite
    output = re.sub(u'\u1077', u'\u1039\u1014', output)  # na
    output = re.sub(u'\u1078', u'\u1039\u1015', output)  # pa_south
    output = re.sub(u'\u1079', u'\u1039\u1016', output)  # fa_ot_htoke
    output = re.sub(u'\u107A', u'\u1039\u1017', output)  # ba_lat_chite
    output = re.sub(u'[\u107B\u1093]', u'\u1039\u1018', output)  # ba_gone
    output = re.sub(u'\u107C', u'\u1039\u1019', output)  # ma
    output = re.sub(u'\u1085', u'\u1039\u101C', output)  # la

    return output

def logical2visual(input):
    output = input

    output = re.sub(u'([\u1000-\u1021])((?:\u103B)?)((?:\u1031)?)', '\\3\\2\\1', output)#1=letters,2=yayit,3=tawaihtoe

    return output

def convert(input):
    output = input

    output = replace(output)
    output = precompose(output)
    output = logical2visual(output)
    return output
