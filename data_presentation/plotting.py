
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 25})

########## reliability ###########
x_data_1 = [
    6,
    5,
    4,
    3,
    2,
    1,
    0.9,
    0.8,
    0.7,
    0.6,
    0.5,
    0.4,
    0.3,
    0.2,
    0.19,
    0.18,
    0.17,
    0.16,
    0.15,
    0.14,
    0.13,
    0.12,
    0.11,
    0.1
]

x_data_2 = [
    6,
    5,
    4,
    3,
    2,
    1,
    0.9,
    0.8,
    0.7,
    0.6,
    0.5,
    0.4,
    0.3,
    0.2,
    0.1
]

y_data_1 = [
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    100,
    97.63247952,
    95.25153744,
    92.86946678,
    88.11686127,
    83.35309198,
    78.58882638,
    73.82510585
]

y_data_2 = [
    100,
    99.9658639,
    99.87803981,
    99.8248207,
    94.57334365,
    70.12043848,
    66.80264341,
    63.43036693,
    63.76089522,
    57.78346053,
    58.47677989,
    51.53548471,
    44.22847561,
    25.71595012,
    17.25813381
]

plt.figure(figsize=(12, 8))
plt.plot(x_data_1, y_data_1, 'bo-', linewidth=3, markersize=8, label='SOSAT')
plt.plot(x_data_2, y_data_2, 'ro-', linewidth=3, markersize=8, label='Orchestra')

plt.xlabel('Application packet period (s)')
plt.ylabel('$PDR_{ave}$ (%)')
plt.grid(True, 'both')
plt.legend()
plt.xscale('log')

plt.savefig('outputs/plots/reliability.png')


##### reliability_nodes ###########
x_data = [
10,
20,
30,
40,
50,
60,
70,
80,
90,
100
]

y_data_1 = [
    100,
    100,
    100,
    100,
    99.99977625,
    99.99990708,
    99.9998146,
    99.98970582,
    99.3800245,
    99.0947317
]

y_data_2 = [
    96.10214207,
    86.26698771,
    81.71470182,
    75.65332159,
    69.75435033,
    66.58631578,
    65.23886239,
    56.92370386,
    53.87614629,
    52.09436509
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='SOSAT')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='Orchestra')

plt.xlabel('Number of nodes')
plt.ylabel('$PDR_{ave}$ (%)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/reliability_nodes.png')





######### throughput ###########
x_data = [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1,
    2,
    3,
    4,
    5
]

y_data_1 = [
    172.2165,
    122.218,
    82.79208333,
    62.59983333,
    50.32541667,
    42.07508333,
    36.14883333,
    31.687,
    28.20416667,
    25.41108333,
    12.76833333,
    8.52725,
    6.401083333,
    5.12375
]

y_data_2 = [
    1.277916667,
    2.51075,
    3.468833333,
    3.537583333,
    3.531833333,
    3.317583333,
    3.318833333,
    3.2955,
    3.230833333,
    3.21475,
    3.653833333,
    3.271083333,
    2.66525,
    2.178333333
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='SOSAT')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='Orchestra')

plt.xlabel('Application packet period (s)')
plt.ylabel('$T_{ave}$ (kB/s)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/throughput.png')


##### throughput_nodes ###########
x_data = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]

y_data_1 = [
    8.208383333,
    17.32898333,
    26.45,
    35.56948333,
    44.69103333,
    53.8091,
    62.9294,
    72.04146667,
    80.66203333,
    89.46341667
]

y_data_2 = [
    3.736116667,
    3.223283333,
    3.32895,
    3.291666667,
    3.241883333,
    3.4275,
    3.599866667,
    3.340933333,
    3.396083333,
    3.517566667
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='SOSAT')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='Orchestra')

plt.xlabel('Number of nodes')
plt.ylabel('$T_{ave}$ (kB/s)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/throughput_nodes.png')





######### latency ###########
x_data = [
    6,
    5,
    4,
    3,
    2,
    1,
    0.9,
    0.8,
    0.7,
    0.6,
    0.5,
    0.4,
    0.3,
    0.2,
    0.1
]

y_data_1 = [
    0.030992688,
    0.03105687,
    0.031144991,
    0.031349108,
    0.031648074,
    0.032654879,
    0.032916234,
    0.033240866,
    0.03367891,
    0.034226829,
    0.035104529,
    0.036567203,
    0.039330138,
    0.048348756,
    0.357655887
]

y_data_2 = [
    0.401464243,
    0.440685643,
    0.512450296,
    0.672427818,
    1.431558404,
    1.355493847,
    1.641322837,
    1.54090275,
    1.289133375,
    1.28405917,
    1.339882225,
    1.056950002,
    1.14491551,
    1.107846297,
    2.269606814
]

y_data_1_error = [
    0.079007312,
    0.07894313,
    0.088855009,
    0.078650892,
    0.088351926,
    0.107345121,
    0.107083766,
    0.136759134,
    0.11632109,
    0.135773171,
    0.134895471,
    0.163432797,
    0.160669862,
    0.211651244,
    0.262344113
]

y_data_2_error = [
    5.698535757,
    7.109314357,
    12.2675497,
    10.42757218,
    22.9884416,
    105.5045062,
    716.8286772,
    297.0290972,
    98.02086663,
    97.69594083,
    212.8001178,
    112.42305,
    92.95508449,
    93.8121537,
    298.1803932
]

lower_error_1 = [0] * len(y_data_1_error)
lower_error_2 = [0] * len(y_data_2_error)

asymmetric_error_1 = [lower_error_1, y_data_1_error]
asymmetric_error_2 = [lower_error_2, y_data_2_error]

plt.figure(figsize=(12, 8))
plt.errorbar(x_data, y_data_1, yerr=asymmetric_error_1, elinewidth=2, capsize=4, capthick=2, fmt='bo-', linewidth=3, markersize=8, label='SOSAT')
plt.errorbar(x_data, y_data_2, yerr=asymmetric_error_2, elinewidth=2, capsize=4, capthick=2, fmt='ro-', linewidth=3, markersize=8, label='Orchestra')

plt.xlabel('Application packet period (s)')
plt.ylabel('$L_{ave}$ (s)')
plt.grid(True, 'both')
plt.legend()
plt.yscale('log')

plt.savefig('outputs/plots/latency.png')


##### latency_nodes ###########
x_data = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]

y_data_1 = [
0.032578789,
0.04713497,
0.056838631,
0.069129475,
0.076033177,
0.078969597,
0.090611322,
0.113505665,
0.159660581,
0.218463331
]

y_data_2 = [
1.593472975,
1.37493273,
1.639407956,
1.676542989,
1.533917635,
1.722281338,
1.897809913,
1.663265775,
1.691360853,
1.721771308
]

y_data_1_error = [
    0.187421211,
    0.22286503,
    0.323161369,
    0.370870525,
    0.423966823,
    0.861030403,
    0.579388678,
    1.226494335,
    0.890339419,
    1.381536669
]

y_data_2_error = [
    179.006527,
    307.1050673,
    834.560592,
    675.543457,
    343.0060824,
    376.2177187,
    722.0221901,
    704.0467342,
    448.0286391,
    314.3382287
]

lower_error_1 = [0] * len(y_data_1_error)
lower_error_2 = [0] * len(y_data_2_error)

asymmetric_error_1 = [lower_error_1, y_data_1_error]
asymmetric_error_2 = [lower_error_2, y_data_2_error]

plt.figure(figsize=(12, 8))
plt.errorbar(x_data, y_data_1, yerr=asymmetric_error_1, elinewidth=2, capsize=4, capthick=2, fmt='bo-', linewidth=3, markersize=8, label='SOSAT')
plt.errorbar(x_data, y_data_2, yerr=asymmetric_error_2, elinewidth=2, capsize=4, capthick=2, fmt='ro-', linewidth=3, markersize=8, label='Orchestra')

plt.xlabel('Number of nodes')
plt.ylabel('$L_{ave}$ (s)')
plt.grid(True, 'both')
# plt.legend()
plt.yscale('log')

plt.savefig('outputs/plots/latency_nodes.png')





######### energy ###########
x_data = [
4,
3,
2,
1,
0.9,
0.8,
0.7,
0.6,
0.5,
0.4,
0.3,
0.2,
0.1
]

y_data_1 = [
7.216706667,
7.335993333,
7.573616667,
8.282003333,
8.43861,
8.633763333,
8.88385,
9.215723333,
9.678316667,
10.36587333,
11.49753667,
13.70689333,
18.38657333
]

y_data_2 = [
10.11890667,
10.63306667,
13.57213333,
24.21831333,
25.68246,
26.68415,
30.76140333,
29.12631,
32.04038,
33.79238667,
35.52941,
36.48684333,
49.53796667
]

y_data_3 = [
2.036776667,
2.07125,
2.092136667,
2.026743333,
2.029496667,
2.053826667,
1.965906667,
2.072563333,
1.999273333,
2.001163333,
2.006913333,
2.070593333,
1.54094
]

y_data_1_error = [
15.66029333,
15.82800667,
16.16238333,
17.15799667,
17.37739,
17.65123667,
18.00315,
18.47027667,
19.11968333,
20.08712667,
21.67746333,
24.78210667,
26.84242667
]

y_data_2_error = [
30.85009333,
46.85393333,
59.63686667,
49.86868667,
61.19454,
69.68585,
69.23859667,
70.87369,
67.95962,
66.20761333,
64.47059,
63.51315667,
50.46203333
]

y_data_3_error = [
0.510223333,
0.64475,
0.931863333,
1.337256667,
1.198503333,
1.305173333,
1.324093333,
1.392436667,
1.540726667,
1.674836667,
1.673086667,
2.166406667,
2.98306
]

lower_error_1 = [0] * len(y_data_1_error)
lower_error_2 = [0] * len(y_data_2_error)
lower_error_3 = [0] * len(y_data_3_error)

asymmetric_error_1 = [lower_error_1, y_data_1_error]
asymmetric_error_2 = [lower_error_2, y_data_2_error]
asymmetric_error_3 = [lower_error_3, y_data_3_error]

plt.figure(figsize=(12, 8))
plt.errorbar(x_data, y_data_1, yerr=asymmetric_error_1, elinewidth=2, capsize=4, capthick=2, fmt='bo-', linewidth=3, markersize=8, label='SOSAT')
plt.errorbar(x_data, y_data_2, yerr=asymmetric_error_2, elinewidth=2, capsize=4, capthick=2, fmt='ro-', linewidth=3, markersize=8, label='Orchestra')
plt.errorbar(x_data, y_data_3, yerr=asymmetric_error_3, elinewidth=2, capsize=4, capthick=2, fmt='go-', linewidth=3, markersize=8, label='Orchestra joined')

plt.xlabel('Application packet period (s)')
plt.ylabel('$RDC_{ave}$ (s)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/energy.png')


##### energy_nodes ###########
x_data = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]

y_data_1 = [
    5.51783,
    6.0341985,
    6.270069667,
    6.47259075,
    6.6006012,
    6.6403205,
    6.774010857,
    6.8655855,
    6.836761333,
    6.9466757
]

y_data_2 = [
    9.517256,
    17.498292,
    19.91186933,
    24.9824025,
    28.4112034,
    29.1377555,
    31.28550614,
    34.24304388,
    35.13185667,
    37.3180403
]

y_data_3 = [
    2.245457,
    1.989242,
    1.900424333,
    1.77836625,
    1.6956976,
    1.677617333,
    1.628918714,
    1.568673,
    1.552944333,
    1.5037685
]

y_data_1_error = [
    17.60317,
    18.3168015,
    19.30993033,
    20.33740925,
    21.4393988,
    22.6286795,
    23.72498914,
    25.0974145,
    27.28923867,
    27.3033243
]

y_data_2_error = [
    65.488744,
    82.501708,
    80.08813067,
    75.0175975,
    71.5887966,
    70.8622445,
    68.71449386,
    65.75695613,
    64.86814333,
    62.6819597
]

y_data_3_error = [
    1.078543,
    1.364758,
    1.234575667,
    1.75763375,
    1.7093024,
    1.727382667,
    1.877081286,
    2.232327,
    2.068055667,
    2.1052315
]

lower_error_1 = [0] * len(y_data_1_error)
lower_error_2 = [0] * len(y_data_2_error)
lower_error_3 = [0] * len(y_data_3_error)

asymmetric_error_1 = [lower_error_1, y_data_1_error]
asymmetric_error_2 = [lower_error_2, y_data_2_error]
asymmetric_error_3 = [lower_error_3, y_data_3_error]


plt.figure(figsize=(12, 8))
plt.errorbar(x_data, y_data_1, yerr=asymmetric_error_1, elinewidth=2, capsize=4, capthick=2, fmt='bo-', linewidth=3, markersize=8, label='SOSAT')
plt.errorbar(x_data, y_data_2, yerr=asymmetric_error_2, elinewidth=2, capsize=4, capthick=2, fmt='ro-', linewidth=3, markersize=8, label='Orchestra')
plt.errorbar(x_data, y_data_3, yerr=asymmetric_error_3, elinewidth=2, capsize=4, capthick=2, fmt='go-', linewidth=3, markersize=8, label='Orchestra joined')

plt.xlabel('Number of nodes')
plt.ylabel('$RDC_{ave}$ (s)')
plt.grid(True, 'both')
# plt.legend()

plt.savefig('outputs/plots/energy_nodes.png')





######### topologies_reliability ###########
x_data = [
    0.5,
    0.4,
    0.3,
    0.2,
    0.1
]

y_data_1 = [
100,
100,
100,
100,
61.1524982
]

y_data_2 = [
100,
100,
100,
100,
75.01293315
]

y_data_3 = [
100,
100,
100,
99.99840904,
86.13921198
]

y_data_4 = [
100,
100,
100,
100,
100
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='Line')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='mesh3')
plt.plot(x_data, y_data_3, 'go-', linewidth=3, markersize=8, label='mesh4')
plt.plot(x_data, y_data_4, 'mo-', linewidth=3, markersize=8, label='mesh9')

plt.xlabel('Application packet period (s)')
plt.ylabel('$PDR_{ave}$ (%)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/topologies_reliability.png')


######### topologies_throughput ###########
x_data = [
    0.5,
    0.4,
    0.3,
    0.2,
    0.1
]

y_data_1 = [
16.17583333,
20.121,
26.6115,
39.28375,
45.83216667
]

y_data_2 = [
32.35191667,
40.24283333,
53.22375,
78.56783333,
112.4968333
]

y_data_3 = [
32.3525,
40.24366667,
53.22416667,
78.56808333,
129.1636667
]

y_data_4 = [
32.35158333,
40.24291667,
53.22441667,
78.56841667,
149.9934167
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='Line')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='mesh3')
plt.plot(x_data, y_data_3, 'go-', linewidth=3, markersize=8, label='mesh4')
plt.plot(x_data, y_data_4, 'mo-', linewidth=3, markersize=8, label='mesh9')

plt.xlabel('Application packet period (s)')
plt.ylabel('$T_{ave}$ (kB/s)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/topologies_throughput.png')


######### topologies_latency ###########
x_data = [
    0.5,
    0.4,
    0.3,
    0.2,
    0.1
]

y_data_1 = [
0.049269279,
0.050814447,
0.054032154,
0.066200168,
1.102299898
]

y_data_2 = [
0.040311703,
0.042033779,
0.045672549,
0.063454678,
0.288578642
]

y_data_3 = [
0.027902095,
0.029112842,
0.031324963,
0.037477803,
0.230434591
]

y_data_4 = [
0.040379997,
0.04052088,
0.040928726,
0.04209098,
0.050378318
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='Line')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='mesh3')
plt.plot(x_data, y_data_3, 'go-', linewidth=3, markersize=8, label='mesh4')
plt.plot(x_data, y_data_4, 'mo-', linewidth=3, markersize=8, label='mesh9')

plt.xlabel('Application packet period (s)')
plt.ylabel('$L_{ave}$ (s)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/topologies_latency.png')


######### topologies_energy ###########
x_data = [
    0.5,
    0.4,
    0.3,
    0.2,
    0.1
]

y_data_1 = [
16.0541,
17.55167,
20.01539,
24.82599,
33.32173
]

y_data_2 = [
13.145215,
13.67109,
14.545295,
16.297915,
20.04341
]

y_data_3 = [
11.133365,
11.69905,
12.629995,
14.447425,
18.14532
]

y_data_4 = [
3.44187,
3.74103,
4.233985,
5.19627,
7.9075
]

plt.figure(figsize=(12, 8))
plt.plot(x_data, y_data_1, 'bo-', linewidth=3, markersize=8, label='Line')
plt.plot(x_data, y_data_2, 'ro-', linewidth=3, markersize=8, label='mesh3')
plt.plot(x_data, y_data_3, 'go-', linewidth=3, markersize=8, label='mesh4')
plt.plot(x_data, y_data_4, 'mo-', linewidth=3, markersize=8, label='mesh9')

plt.xlabel('Application packet period (s)')
plt.ylabel('$RDC_{ave}$ (%)')
plt.grid(True, 'both')
plt.legend()

plt.savefig('outputs/plots/topologies_energy.png')