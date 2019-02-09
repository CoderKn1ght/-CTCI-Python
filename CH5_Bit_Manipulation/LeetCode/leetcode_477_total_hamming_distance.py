# Times out on leetcode

def get_total_hamming_distance(x,y):
    hamming_distance = 0

    while x or y != 0:
        first_bit_of_x = x & 1
        first_bit_of_y = y & 1

        if first_bit_of_x != first_bit_of_y:
            hamming_distance += 1
        if x != 0:
            x = x >> 1
        if y != 0:
            y = y >> 1

    return hamming_distance

def get_all_combinations(nums):
    total_hamming_distance = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            total_hamming_distance += get_total_hamming_distance(nums[i],nums[j])
            j += 1
        i +=1
    print(total_hamming_distance)

nums = [482445,7558884,1225282,3443150,5483536,9123732,7149476,1322368,7028661,7060197,5315284,9776394,9188784,7757815,3157818,282441,7852638,6281131,7707215,4877395,7266823,7005195,9416625,2023564,8563798,7265436,1403019,160238,6888730,9349906,6174510,2050048,9175317,3664615,2023253,9747197,8658341,1577259,5631092,3430688,2005837,2396574,3214815,4992241,4628078,1995765,9131803,1072506,7205232,5479080,3102540,7591273,2913026,7747614,3954032,7135502,95172,7081401,7018534,6460665,5053992,7374999,9926447,5249064,327565,4525439,9753361,9647444,1182494,534322,1058779,7566566,3145677,7527411,4763193,8686879,955224,8033126,409922,1520290,4735290,5736491,1800211,1454132,9643939,942735,2161616,4219780,2883910,2716535,548624,9095180,1948390,5711447,7635193,8818066,4607020,3571138,8178760,7176846,1815645,7997903,1349093,712536,9166427,9791762,4669739,5228947,2864659,4920110,8214583,1939917,9458159,9046946,27241,5062933,1707718,1292260,7843639,4256583,3857640,8069516,7330295,3258697,2166170,4866636,7692621,8390172,3152636,853502,761252,9279194,4941372,5000417,5032419,8217655,5861888,8139477,2872154,4445732,9385903,5588266,2480708,5988663,3607676,9080593,5623014,45253,3071793,6232979,537861,6475172,3468854,2467441,8565550,1904080,1207032,2393867,6849267,3532466,8738858,8945987,2205487,5102855,7744193,2305309,5631961,3012748,229842,707825,1059673,8698001,6065767,2057403,3311204,236894,1047700,8810745,2782817,9708263,4768559,4979218,2804406,3930008,8036512,2158111,5662090,2641361,2947230,9194175,5067396,3390184,8127710,9595275,6195022,6658142,5922771,3658458,7459800,7906962,7104376,9783490,4954524,2839769,7769526,288994,4355087,1445034,9849521,1180384,2476286,1895843,1120419,1180266,2616618,3613385,4680911,1056729,2819548,1765004,3057258,7621701,7950244,9307972,8613218,2112244,6929198,150826,3373624,3665346,675348,6485024,2638794,7240862,2923089,9945677,1867741,9114504,23814,1921719,6720041,4960507,9718030,4710127,9401883,4605615,4778502,9756154,1396615,8680633,4038680,6619857,3077822,4583804,9318494,6922538,3406738,89233,9341740,1005660,6366222,9829851,2234048,9384181,8205570,1573647,4192299,9621342,5873780,1258831,7742682,8206441,6609835,6838291,6294011,7692086,5062915,9939126,129461,827804,7038055,7937712,4697981,2059997,9761781,5418983,4351018,5789707,5850678,5748340,6443533,6812069,817835,3306430,3940745,5117402,4710025,3138302,5743542,9086524,1443775,4198418,6324931,6890570,2779408,6047022,1041301,3521152,7943195,2087740,1152249,956544,9563122,8792108,5001491,7237361,8449761,1932603,119137,1770959,3616899,9024133,6427862,2346818,8984658,8896226,6820272,6687457,2513999,5522231,9774996,6394288,2922266,5165604,991214,3007700,7421020,5950214,7746178,6062247,7401832,7916121,9650288,2369202,9572256,4428556,4433337,8377228,962917,4339068,8059477,9871112,2594255,444354,7319249,982196,5900797,9487774,1672384,3188854,1476983,4739252,9379714,7371321,9239501,1150544,7537587,6095624,7465357,7716085,1573974,8298787,6805700,906854,6714159,4895868,3713669,1146209,2725241,7253678,442911,3675546,3586793,1780280,8595125,5946081,3566271,1753159,4849590,6133078,2879424,3595867,7309774,9582094,4111334,2388013,5208331,6508637,5517818,3821261,1577994,3053906,752504,2374669,3103479,733582,1236947,8595339,9147736,2094968,4022646,3016910,9174487,1836115,9135280,9937955,2829975,5803480,7774978,2912868,6739462,7398566,2778237,46293,1025029,6222538,8171642,9575286,637190,737362,9316674,6821733,4753195,8268982,3400910,611546,8442145,2022936,7216668,2479421,9211720,2587923,3030320,7335159,2106032,8462782,7110261,1548152,1452966,3390379,9509251,3733056,3012830,9045217,7062184,6236390,294495,9665861,1630210,5546082,1677309,2238863,8051486,8849352,6887644,182059,8780611,3802078,40560,9907476,8784978,2572315,1531465,4110225,159426,7135469,4563764,4964390,1987054,5277094,6190797,3053301,9545713,1175822,8795309,6679388,4042849,886662,6966151,6319785,6540192,2273079,50576,7725986,2146036,5099076,6535386,5055794,4241146,3325227,5967901,8431654,2203967,9769970,442261,8201729,7110852,2078156,7037206,2279168,3471153,6085759,2644681,2717158,4699653,3534922,1055406,5820865,9660274,8768057,1691779,2717776,8720201,1302477,6187137,4258058,4572654,9583131,6516970,1813616,8308677,1163573,5995588,3857707,1881495,5561406,1472198,9736023,6307656,5464643,6521660,8380046,6768333,8681263,8079624,3321428,2942909,3318370,8387237,9184180,3143210,1301520,3520657,8585174,8395225,7209408,9038733,2816151,4715823,8431511,3785233,7781665,4004768,8770452,9291101,8909898,985286,4109961,7539289,2716918,315128,5924290,7538689,81650,8137326,186810,5728755,133905,6419578,6795650,4041149,8543850,8976624,6173634,8228582,9161132,8156985,3190889,779116,2068262,8764528,4703210,3147864,3427052,1246430,2602052,4650647,5037414,6185754,5303043,1841684,612153,718858,9878904,178530,9559352,1445051,7935017,3083384,6493649,4913259,65538,6550608,5350571,8477024,6338465,2493151,3008585,7576391,58896,2550982,6194046,3765221,1746628,3219716,7319150,266215,119033,845584,1805183,2681223,9871109,8038765,7949418,3166990,6727112,6184315,3422616,9195200,9304262,9237826,8405354,8135222,1955436,2056457,1136248,8730781,8251538,4462222,1556556,2561904,1272612,305613,8050330,9771305,8558073,9444453,2707338,9608467,3682077,5339778,6040517,2873433,8355863,4049118,9839369,3411187,3901685,2576451,3640483,9993886,8189914,2643925,1827977,1412002,9367054,1039792,7978101,8752882,4770466,3215057,9700800,1719429,2147902,6539851,1214270,1875177,8122469,8531210,2200632,4037003,1289985,7972091,6841346,404219,251703,7345049,1580020,9258665,8386226,7045969,8397242,2589172,9259241,4614524,3078466,4401423,7449363,1058704,1464106,3475826,9724758,2855044,8086075,704829,2276590,5119484,9702199,6087442,3935150,4899595,6871512,9007337,2274133,541708,6538236,1780098,255075,5958275,7946229,7278600,696366,8345149,4713077,8113534,7796065,5244965,2915717,2975251,5638053,6743947,1174805,145880,199756,1158400,9143621,8659076,7745514,4033400,2291074,8858719,1800212,295293,2557445,5809797,784931,6901302,9258109,6627556,1041316,1561303,1352623,3414867,5979179,6988890,1744668,1272354,5404807,9989009,543708,1448745,5912297,6887783,534012,6963830,5616938,4842720,3310700,6789389,9590877,9773214,9604080,3934435,1753390,5265494,5734666,2763059,4034202,9620113,6502755,9818910,9998263,7204886,5070393,3667871,1816514,84585,3513671,4150050,1224468,1318962,3341176,7091966,3318199,2734438,2222700,1727567,2512892,764459,4873043,4122759,5367631,2530265,4583360,3594184,9725283,3679166,7316067,7028366,4316334,3938473,8198188,1017332,492881,1353580,9104123,7704124,2453002,1126255,3724541,8985780,7065969,7132508,7451680,1571212,5297920,107402,1762012,2986717,4271804,2441810,673267,717323,3208912,1537900,6324602,8154755,5190877,8396237,5470403,1894133,1005027,1133926,4377305,9839737,8083651,9706708,2604362,663548,4437958,4697172,7210823,4807106,196935,2999965,5722827,5920275,6684963,1726541,2153242,6807385,5118871,909772,5115720,6394205,9359529,1892938,4340729,1519529,7258806,4598541,7307652,2607152,8502990,8381048,2798125,3739309,181865,1807318,7098102,47306,736430,8066975,2546596,3426456,7367902,9257767,224318,6994710,81810,34112,114072,9025015,9083880,7266268,6592308,2782404,5180950,163747,9407671,6375621,9783064,8482453,6805313,5057789,4734356,7961641,643596,2692070,3045637,523110,3520161,3654990,1250236,3532739,855014,3882569,4500151,3181235,1684204,978595,9226367,5951031,6793388,7443335,6937087,7490292,2858161,6883870,2126509,4255344,3156878,9033128,248539,7710879,4427577,3994617,5748617,151160,1064274,880674,9485701,4891451,2467459,6960521,3987242,6896880,7625713,1992328,7811235,1368822,2894906,2242883,2242005,8905079,3535531,1855469,8446823,8413392,6234176,8016376,6452984,8724248,54563,8369317,1255498,4961482,438119,7290626,3900102,46281,9571034,8258381,2418634,9304857,2321192,7036165,2310926,601480,7445972,9911943,6076049,1051867,922626,5869474,3606713,5964674,2729399,6066161,9030206]

get_all_combinations(nums)