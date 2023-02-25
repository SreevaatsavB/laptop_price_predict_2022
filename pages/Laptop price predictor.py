import streamlit as st
import numpy as np
import pickle

st.header("Laptop price predictor")
st.write("### Choose your desired features, and get an estimated of how much would a laptop of those specific features might cost.")
st.write("**These price estimates are based on the data from June 2022**, from the flipkart's laptop catalog.")


model_type = st.selectbox("Laptop type: ",
                     ['Gaming', 'Thin and light', '2 in 1', 'Notebook', 'Normal laptop', '2 in 1 gaming', 'Business laptop', 'Chromebook', 'Creator laptop'])

type_dict = {'Gaming': 1,
 'Thin and light': 2,
 '2 in 1': 3,
 'Notebook': 4,
 'Normal laptop': 5,
 '2 in 1 gaming': 6,
 'Business laptop': 7,
 'Chromebook': 8,
 'Creator laptop': 9}
model_type = type_dict[model_type]


brand = st.selectbox("Choose a laptop brand: ",
                     ['HP', 'Lenovo', 'Dell', 'Apple','Asus','MSI', 'Realme', 'Avita', 'Acer', 'Samsung', 'Infinix', 'LG', 'Nokia', 'Redmibook', 'MI', 'Vaio'])
brand = brand.lower()
company_dict = {'asus': 1,
 'hp': 2,
 'lenovo': 3,
 'dell': 4,
 'msi': 5,
 'realme': 6,
 'avita': 7,
 'acer': 8,
 'samsung': 9,
 'infinix': 10,
 'lg': 11,
 'apple': 12,
 'nokia': 13,
 'redmibook': 14,
 'mi': 15,
 'vaio': 16}
brand = company_dict[brand]


os = st.selectbox("Choose an Operating System: ",
                  ["Windows", "MAC OS", "Ubuntu", "Chrome", "DOS"])
os = os.lower()
if os == "mac os":
    os = "mac"
os_dict = {'windows': 1, 'chrome': 2, 'dos': 3, 'mac': 4, 'ubuntu': 5}
os = os_dict[os]


cpu_brand = st.selectbox("Choose a processor brand: ",
                     ['AMD', 'Intel', 'Apple', 'Mediatek'])
cpu_brand = cpu_brand.lower()
cpu_brand_dict = {'intel': 1, 'amd': 2, 'qualcomm': 3, 'apple': 4, 'mediatek': 5}
cpu_brand = cpu_brand_dict[cpu_brand]


processor_name  = st.selectbox("Select a CPU processor : ",
                               ['core i9',
                                'ryzen 7 octa core',
                                'core i5',
                                'core i7',
                                'celeron dual core',
                                'pentium silver',
                                'athlon dual core',
                                'ryzen 7 dual core',
                                'ryzen 3 quad core',
                                'ryzen 9 octa core',
                                'core i3',
                                'ryzen 5 hexa core',
                                'ryzen 5 quad core',
                                'ryzen 7 hexa core',
                                'ryzen 7 quad core',
                                'pentium quad core',
                                'celeron quad core',
                                'snapdragon 7c gen 2',
                                'ryzen 5 dual core',
                                'ryzen 3 dual core',
                                'dual core',
                                'ryzen 5 octa core',
                                'm1 pro',
                                'ryzen 3 hexa core',
                                'apu dual core a6',
                                'mediatek kompanio 500',
                                'm1',
                                'apu dual core a9',
                                'hexa core i5',
                                'octa core i7']
                               )
processor_dict = {'core i9': 1,
 'ryzen 7 octa core': 2,
 'core i5': 3,
 'core i7': 4,
 'celeron dual core': 5,
 'pentium silver': 6,
 'athlon dual core': 7,
 'ryzen 7 dual core': 8,
 'ryzen 3 quad core': 9,
 'ryzen 9 octa core': 10,
 'core i3': 11,
 'ryzen 5 hexa core': 12,
 'ryzen 5 quad core': 13,
 'ryzen 7 hexa core': 14,
 'ryzen 7 quad core': 15,
 'pentium quad core': 16,
 'celeron quad core': 17,
 'snapdragon 7c gen 2': 18,
 'ryzen 5 dual core': 19,
 'ryzen 3 dual core': 20,
 'dual core': 21,
 'ryzen 5 octa core': 22,
 'm1 pro': 23,
 'ryzen 3 hexa core': 24,
 'apu dual core a6': 25,
 'mediatek kompanio 500': 26,
 'm1': 27,
 'apu dual core a9': 28,
 'hexa core i5': 29,
 'octa core i7': 30}
processor_name = processor_dict[processor_name]


gpu_brand = st.selectbox("Select a GPU brand :",
             ['Nvidia', 'Intel', 'AMD', 'Qualcomm'])

gpu_brand_dict = {'nvidia': 1, 'none': 2, 'amd': 3, 'qualcomm': 4}
gpu_brand = gpu_brand.lower()
if gpu_brand == "intel":
    gpu_brand = "none"
gpu_brand = gpu_brand_dict[gpu_brand]

gpu_mem = st.slider("Select the GPU memory needed (in MB)", 0, 16000, step = 2000)


# gpu_proc = st.selectbox("Select a GPU processor :",
#                         ['nvidia geforce rtx 3070 ti',
#                          'nvidia geforce rtx 3050',
#                          'intel hd',
#                          'iris xe',
#                          'amd radeon',
#                          'nvidia geforce gtx 1650',
#                          'intel uhd',
#                          'intel iris xe',
#                          'nvidia geforce rtx 3070',
#                          'nvidia geforce rtx 3050 ti',
#                          'amd radeon vega 8',
#                          'nvidia geforce rtx 3060',
#                          'nvidia geforce mx 450',
#                          'intel uhd 600',
#                          'amd radeon rx vega 10',
#                          'qualcomm adreno 618 gpu',
#                          'amd radeon vega ',
#                          'amd radeon rx 6600m',
#                          'qualcomm adreno',
#                          'nvidia geforce rtx 3050ti',
#                          'nvidia geforce rtx 3080 ti',
#                          'intel iris plus',
#                          'nvidia geforce gtx',
#                          'intel uhd 605',
#                          'nvidia geforce rtx',
#                          'intel iris',
#                          'nvidia geforce mx 350',
#                          'nvidia geforce mx 330',
#                          'amd radeon rx 6700m',
#                          'nvidia geforce',
#                          'nvidia geforce gtx 1650 ti',
#                          'm1',
#                          'amd radeon vega',
#                          'intel hd 520',
#                          'amd radeon rx6600m',
#                          'amd radeon rx 6800m',
#                          'amd radeon 5500u',
#                          'amd radeon 5500m',
#                          'nvidia geforce mx 130',
#                          'amd radeon r4',
#                          'mediatek',
#                          'intel hd 500',
#                          'amd radeon r5',
#                          'amd radeon r4 (stoney ridge)',
#                          'nvidia geforce gtx 1650 max q',
#                          'nvidia geforce mx 250',
#                          'nvidia geforce gtx 1660 ti',
#                          'nvidia geforce rtx 2060',
#                          'intel uhd 620',
#                          'intel hd 5500',
#                          'nvidia geforce rtx 2080 super max-q',
#                          'amd radeon vega 6',
#                          'intel iris xe max',
#                          'nvidia geforce gtx 1650 ti max-q',
#                          'amd radeon 520',
#                          'nvidia geforce rtx 2070 max-q',
#                          'nvidia geforce gtx mx 330',
#                          'nvidia geforce mx 230',
#                          'intel hd 620',
#                          'nvidia quadro p520',
#                          'nvidia quadro t2000',
#                          'nvidia geforce mx 110']
#                         )
# gpu_proc_dict = {'nvidia geforce rtx 3070 ti': 1,
#  'nvidia geforce rtx 3050': 2,
#  'intel hd': 3,
#  'iris xe': 4,
#  'amd radeon': 5,
#  'nvidia geforce gtx 1650': 6,
#  'intel uhd': 7,
#  'intel iris xe': 8,
#  'nvidia geforce rtx 3070': 9,
#  'nvidia geforce rtx 3050 ti': 10,
#  'amd radeon vega 8': 11,
#  'nvidia geforce rtx 3060': 12,
#  'nvidia geforce mx 450': 13,
#  'intel uhd 600': 14,
#  'amd radeon rx vega 10': 15,
#  'qualcomm adreno 618 gpu': 16,
#  'amd radeon vega ': 17,
#  'amd radeon rx 6600m': 18,
#  'qualcomm adreno': 19,
#  'nvidia geforce rtx 3050ti': 20,
#  'nvidia geforce rtx 3080 ti': 21,
#  'intel iris plus': 22,
#  'nvidia geforce gtx': 23,
#  'intel uhd 605': 24,
#  'nvidia geforce rtx': 25,
#  'intel iris': 26,
#  'nvidia geforce mx 350': 27,
#  'nvidia geforce mx 330': 28,
#  'amd radeon rx 6700m': 29,
#  'nvidia geforce': 30,
#  'nvidia geforce gtx 1650 ti': 31,
#  'm1': 32,
#  'amd radeon vega': 33,
#  'intel hd 520': 34,
#  'amd radeon rx6600m': 35,
#  'amd radeon rx 6800m': 36,
#  'amd radeon 5500u': 37,
#  'amd radeon 5500m': 38,
#  'nvidia geforce mx 130': 39,
#  'amd radeon r4': 40,
#  'mediatek': 41,
#  'intel hd 500': 42,
#  'amd radeon r5': 43,
#  'amd radeon r4 (stoney ridge)': 44,
#  'nvidia geforce gtx 1650 max q': 45,
#  'nvidia geforce mx 250': 46,
#  'nvidia geforce gtx 1660 ti': 47,
#  'nvidia geforce rtx 2060': 48,
#  'intel uhd 620': 49,
#  'intel hd 5500': 50,
#  'nvidia geforce rtx 2080 super max-q': 51,
#  'amd radeon vega 6': 52,
#  'intel iris xe max': 53,
#  'nvidia geforce gtx 1650 ti max-q': 54,
#  'amd radeon 520': 55,
#  'nvidia geforce rtx 2070 max-q': 56,
#  'nvidia geforce gtx mx 330': 57,
#  'nvidia geforce mx 230': 58,
#  'intel hd 620': 59,
#  'nvidia quadro p520': 60,
#  'nvidia quadro t2000': 61,
#  'nvidia geforce mx 110': 62}
# gpu_proc = gpu_proc_dict[gpu_proc]

ram_mem = st.slider("Select the amount of primary memory (RAM) needed (in GB)",  0, 32, step = 4)


storage = st.slider("Select the amount of storage (in GB)",  128, 2048, step = 128)


ssd = st.radio("Select thye of memory: ", ('SSD', 'HDD'))
if ssd == 'SSD':
    ssd = 1

else:
    ssd = 0

expandable = st.radio("Do you want expandable memory?: ", ('Yes', 'No'))
if expandable == 'Yes':
    expandable = 1

else:
    expandable = 0


screen_size = st.slider("Select the screen_size (in inches)",  11.6, 17.3 ,step = 0.1)


max_screen_res = st.selectbox("Select a desired screen resolution (in pixels):",
                         [720, 1080, 1440, 2160])


touchscreen = st.radio("Do you want touchscreen?: ", ('Yes', 'No'))
if touchscreen == 'Yes':
    touchscreen = 1

else:
    touchscreen = 0


# weight = st.slider("Select the weight of the laptop (in kg)", 0.78, 2.9, step = 0.1)


bat_life = st.slider("Select the battery life desired (in hrs)", 2, 8 , step = 1)


if (st.button('Get an estimate!')):
 user_inp = [model_type,gpu_mem, cpu_brand,
                     processor_name, ssd, ram_mem, expandable, os,
                     touchscreen, screen_size, max_screen_res, gpu_brand,
                     brand, storage, bat_life]


 user_inp = np.array(user_inp)
 user_inp = user_inp.reshape(1, -1)
 scaler = pickle.load(open('models/mm_scaler.sav', 'rb'))
 x_test = scaler.transform(user_inp)

 # x_test = x_test.reshape(1, -1)
 # st.write(" ## Shape of inp = ", str(x_test.shape))

 xgb_regr = pickle.load(open('models/xgb_regr_f.pkl', 'rb'))
 rf_regr = pickle.load(open('models/rf_regr_f.pkl', 'rb'))
 svr_regr = pickle.load(open('models/svr_f.pkl', 'rb'))

 op1 = xgb_regr.predict(x_test)
 op2 = svr_regr.predict(x_test)
 op3 = rf_regr.predict(x_test)

 op_f = (0.45*op1 + 0.45*op2 + 0.1*op3)
 # op_f = (op1 + op3)//2

 st.write(" ## The predicted laptop price is around Rs. {}.".format(int(op_f[0])))
 st.write("**NOTE:- This price is based on the data from May-June 2022**")
 st.write("**The price predicted may also vary depending upon your specific requirement, this model just gives an estimate**")
