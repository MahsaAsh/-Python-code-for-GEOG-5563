import pandas as pd
import matplotlib.pyplot as plt

fields = ['sensor_index', 'name', 'location_type', 'latitude', 'longitude', 'pm2.5_60minute']

data = [
    [3088, 'Howe Neighborhood', 0, 44.935818, -93.21752, 3.6],
    [266591, 'AM-2.0', 0, 44.967037, -93.06111, 18.6],
    [5582, 'Vircroft Ashnia', 0, 44.891655, -93.34291, 11.1],
    [5644, 'APPLEGARDEN', 0, 44.967793, -93.66004, 13.2],
    [6376, 'Savage, MN', 0, 44.741486, -93.368, 12.7],
    [7314, 'Beechnut', 0, 45.138016, -93.25998, 9.4],
    [9816, 'Mounds Park', 0, 44.94585, -93.0564, 17.4],
    [272767, 'Woodbury', 0, 44.940716, -92.92438, 16.7],
    [10978, 'Mounds Park-indoor', 1, 44.94863, -93.05569, 1.1],
    [11134, 'Linden Hills', 0, 44.92776, -93.32235, 15.2],
    [21179, 'Lynn-Lake', 0, 44.944565, -93.28692, 18.0],
    [22771, 'Side Yard', 0, 44.901127, -93.594376, 7.1],
    [41561, 'Lee Circle', 0, 44.9073, -93.60277, 3.0],
    [46215, "Kevin's Home", 1, 44.90999, -93.232216, 0.2],
    [54907, 'MplsLoganAQI', 0, 45.003338, -93.25568, 15.8],
    [61239, '15XX Jefferson St NE', 0, 45.0043, -93.2546, 11.4],
    [75827, 'Ridgewood Park', 0, 44.932705, -93.14049, 11.0],
    [77405, 'Hamline Midway', 0, 44.966743, -93.17984, 24.4],
    [85113, 'Mac-Groveland', 0, 44.93642, -93.17899, 17.0],
    [97561, 'Hamline and Saint Clair', 0, 44.9354, -93.15556, 17.0],
    [97563, 'Four Seasons At Rush Creek', 0, 45.094666, -93.50745, 11.7],
    [98255, '1636 Breda Ave', 0, 44.97623, -93.16939, 1.8],
    [98297, 'MPCA_Burnsville-East', 0, 44.770008, -93.23261, 12.0],
    [98533, 'MPCA Air Monitoring Site 0890', 0, 44.966675, -93.06423, 17.0],
    [98539, 'MCPA_HighlandPark_2', 0, 44.899742, -93.17883, 10.6],
    [98581, 'MPCA-UAT-TEST1', 0, 44.899597, -93.17877, 22.0],
    [99807, 'Southwest High School', 0, 44.91834, -93.32371, 0.0],
    [101525, 'The Shire', 0, 44.893944, -93.30508, 15.4],
    [103710, 'Washington St NE, Indoor', 1, 44.997383, -93.25751, 20.4],
    [104760, 'Science Museum of Minnesota', 0, 44.942642, -93.100105, 17.2],
    [107300, 'W 84th St Bloomington', 1, 44.84951, -93.374435, 12.1],
    [107638, 'Stoneclife Drive', 0, 44.77918, -93.1688, 17.0],
    [108274, 'Northwood West Air Quality', 0, 45.03069, -93.39377, 9.6],
    [108364, 'Edina MN', 0, 44.878834, -93.35441, 12.6],
    [108366, 'Dakota Trail', 0, 44.87984, -93.38967, 17.8],
    [110979, 'Washington St NE', 0, 44.997475, -93.25726, 15.7],
    [113486, 'Bancroft', 0, 44.928123, -93.25389, 11.1],
    [119509, 'Nothern Meadows', 0, 45.16858, -93.18118, 25.5],
    [120481, 'Buffalo', 0, 45.203365, -93.833084, 8.6],
    [124799, 'Baked on Bryant', 1, 44.92788, -93.29084, 0.1],
    [126487, 'Northwoods Berry Clan', 0, 45.040394, -93.21327, 13.6],
    [128195, 'Groveland Park', 0, 44.93578, -93.18634, 11.9],
    [129377, 'The Gaul’s', 1, 45.28237, -92.9423, 0.7],
    [142724, 'City of Minneapolis Community Air Monitoring Project 21', 0, 44.937733, -93.24356, 17.4],
    [142734, 'City of Minneapolis Community Air Monitoring Project 19', 0, 44.90432, -93.280624, 13.5],
    [142736, 'City of Minneapolis Community Air Monitoring Project 17', 0, 44.972713, -93.28224, 17.4],
    [142774, 'City of Minneapolis Community Air Monitoring Project 30', 0, 44.953075, -93.31713, 13.2],
    [142932, 'City of Minneapolis Community Air Monitoring Project 77', 0, 44.953747, -93.252464, 15.8],
    [143214, 'City of Minneapolis Community Air Monitoring Project 8', 0, 44.90534, -93.232285, 15.2],
    [143216, 'City of Minneapolis Community Air Monitoring Project 14', 0, 44.97844, -93.263535, 15.1],
    [143226, 'City of Minneapolis Community Air Monitoring Project 15', 0, 44.91171, -93.227066, 12.8],
    [143242, 'City of Minneapolis Community Air Monitoring Project 33', 0, 44.96826, -93.21156, 12.7],
    [143246, 'City of Minneapolis Community Air Monitoring Project 20', 0, 44.901524, -93.276825, 10.7],
    [143262, 'City of Minneapolis Community Air Monitoring Project 80', 0, 44.928658, -93.26884, 0.0],
    [143284, 'City of Minneapolis Community Air Monitoring Project 76', 0, 44.95001, -93.24743, 14.1],
    [143648, 'City of Minneapolis Community Air Monitoring Project 34', 0, 45.029537, -93.29194, 16.0],
    [143656, 'City of Minneapolis Community Air Monitoring Project 38', 0, 44.932285, -93.28308, 13.7],
    [143666, 'City of Minneapolis Community Air Monitoring Project 56', 0, 44.998505, -93.24864, 15.2],
    [143916, 'City of Minneapolis Community Air Monitoring Project 43', 0, 44.960915, -93.26111, 18.1],
    [143942, 'City of Minneapolis Community Air Monitoring Project 41', 0, 44.98081, -93.30325, 15.1],
    [145242, 'City of Minneapolis Community Air Monitoring Project 6', 0, 45.007458, -93.26463, 20.4],
    [145252, 'The Gauls: Outdoors', 0, 45.28081, -92.9439, 13.2],
    [145454, 'City of Minneapolis Community Air Monitoring Project 2', 0, 44.94475, -93.23892, 18.4],
    [145470, 'City of Minneapolis Community Air Monitoring Project 7', 0, 44.90896, -93.23099, 16.9],
    [145498, 'City of Minneapolis Community Air Monitoring Project 1', 0, 44.935925, -93.2779, 17.0],
    [145506, 'City of Minneapolis Community Air Monitoring Project 63', 0, 44.916107, -93.25623, 15.8],
    [145604, 'City of Minneapolis Community Air Monitoring Project 26', 0, 44.962765, -93.23776, 15.0],
    [147749, '2624 Burd Place', 1, 44.95552, -93.38529, 44.7],
    [154751, 'Saint Paul West Side', 0, 44.9286, -93.09272, 5.0],
    [157861, 'City of Minneapolis Community Air Monitoring Project 61', 0, 44.930527, -93.25872, 15.9],
    [157877, 'City of Minneapolis Community Air Monitoring Project 9', 0, 44.901764, -93.2089, 15.2],
    [157935, 'City of Minneapolis Community Air Monitoring Project 62', 0, 44.930527, -93.32394, 11.6],
    [162145, 'The Avenues', 0, 44.928246, -93.41132, 13.0],
    [164991, 'Mainz Farm', 0, 44.621967, -92.834, 16.6],
    [166875, 'City of Minneapolis Community Air Monitoring Project 78', 0, 44.95375, -93.24866, 17.1],
    [168327, 'City of Minneapolis Community Air Monitoring Project 23', 0, 44.95194, -93.263916, 16.7],
    [169257, 'BeeHaven', 1, 45.09108, -92.926476, 1.6],
    [171059, 'Brooklyn Center - Inside', 1, 45.05942, -93.294106, 23.3],
    [171919, 'Sr Mas Alto', 0, 44.900303, -93.387634, 14.1],
    [173739, 'Indoor Purp - Pushing P', 1, 44.73875, -93.34813, 2.1],
    [173737, 'Outdoor Purp - Pushing P', 0, 44.750458, -93.34945, 16.5],
    [174855, 'Brooklyn Center', 0, 45.05947, -93.294075, 14.6],
    [174889, '35th St S & 26th Ave S', 0, 44.938763, -93.23495, 16.2],
    [176811, 'MPCA_CoLocation_Blaine_3', 0, 45.140778, -93.22208, 16.4],
    [176835, 'MPCA_CoLocation_Blaine_1', 0, 45.140717, -93.22207, 15.2],
    [177501, 'Dakota Ave', 0, 44.720043, -93.35996, 15.6],
    [182801, 'OpenAeros', 0, 44.961143, -93.18576, 16.9],
    [183013, 'Lake Elmo', 0, 45.022232, -92.884544, 16.8],
    [183325, 'Garfield St NE', 0, 45.02024, -93.23328, 10.4],
    [183713, 'Indoor Sensor', 1, 44.91555, -93.29696, 3.1],
    [184003, 'Southwest Eden Prairie', 0, 44.83155, -93.50169, 13.9],
    [186119, 'Tom lais', 0, 44.910538, -93.21825, 16.6],
    [189001, 'MPCA-Eagan', 0, 44.78542, -93.16039, 17.4],
    [189027, 'Roseville Indoor', 1, 45.021667, -93.130424, 0.4],
    [189353, 'Roseville C and Dale', 0, 45.021038, -93.13011, 18.2],
    [190557, 'Lake St. Croix', 0, 44.925484, -92.764496, 8.4],
    [190567, 'Deer Hill', 0, 44.96578, -93.46574, 14.1],
    [192821, 'White Bear Lake', 0, 45.085712, -93.00258, 0.1],
    [193171, 'Crystal', 0, 45.05231, -93.36097, 14.9],
    [195819, 'Hiawatha Ave', 1, 44.853672, -93.46561, 5.1],
    [195959, 'Harrison', 1, 44.979637, -93.300095, 9.8],
    [196531, '300 Block Oak Chaska', 0, 44.787113, -93.598656, 6.8],
    [196979, 'Idaho Av Northome Falcon Heights', 0, 44.989788, -93.16302, 18.6],
    [197016, 'Falcon Heights City Hall', 0, 44.99267, -93.18387, 30.4],
    [198083, 'UST-OSS', 1, 44.94014, -93.195114, 6.5],
    [198941, '36th and Hiawatha', 0, 44.93689, -93.231476, 15.4],
    [205273, 'Cleveland and St. Clair', 0, 44.93407, -93.18662, 16.4],
    [206155, 'CHS Field', 0, 44.95089, -93.084694, 18.0],
    [208767, 'WBLake Indoors', 1, 45.085655, -93.00256, 4.0],
    [212713, 'Holland', 0, 45.008553, -93.26158, 14.1],
    [224565, 'City of Minneapolis Community Air Monitoring Project 87', 0, 45.0168, -93.27133, 16.7],
    [224699, '(Las Estrellas) City of Minneapolis Community Air Monitoring Project 92', 0, 44.999817, -93.26217, 15.8],
    [224731, 'City of Minneapolis Community Air Monitoring Project 90', 0, 45.009525, -93.29559, 17.6],
    [224735, '(Andersen) City of Minneapolis Community Air Monitoring Project 91', 0, 44.952866, -93.25772, 16.2],
    [224739, 'City of Minneapolis Community Air Monitoring Project 83', 0, 44.95736, -93.24988, 15.2],
    [224751, 'City of Minneapolis Community Air Monitoring Project 84', 0, 44.92459, -93.31464, 17.6],
    [224753, 'City of Minneapolis Community Air Monitoring Project 85', 0, 44.922607, -93.32914, 15.4],
    [224773, 'City of Minneapolis Community Air Monitoring Project 89', 0, 44.99634, -93.29717, 9.8],
    [225219, 'AM-6', 0, 44.967922, -93.06293, 18.5],
    [225227, 'AM-4', 0, 44.967506, -93.06432, 19.1],
    [225229, 'AM-3', 0, 44.96753, -93.06115, 19.9],
    [225247, 'AM-5', 0, 44.967854, -93.06321, 24.0],
    [225275, 'AM-7', 0, 44.96784, -93.06263, 20.6],
    [225845, 'AM-1', 0, 44.966553, -93.061264, 16.8],
    [235931, 'Anpetu Teca', 0, 45.005337, -93.180176, 20.6],
    [235941, 'Cedar Creek Ecosystem Reserve', 0, 45.401237, -93.20064, 15.4],
    [236622, 'Las Estrellas', 1, 44.999077, -93.26186, 2.4],
    [236637, 'Andersen United Middle School', 1, 44.95334, -93.25887, 3.0],
    [238605, 'Mostardi Platt Mendota Heights', 0, 44.864822, -93.16695, 19.7],
    [239313, 'Dodge Nature Center & Preschool', 0, 44.894188, -93.09646, 18.8],
    [247979, '44th & Vincent Ave S', 0, 44.92329, -93.31632, 14.0],
    [248579, 'Berkshire', 0, 45.088303, -93.45808, 16.0],
    [251021, 'Jupiter Air', 0, 45.082245, -93.26645, 18.6],
    [253933, 'Will Heal farm', 0, 45.3646, -93.326965, 21.8],
    [253937, 'SMSC Sensor 2', 0, 44.718502, -93.493805, 118.4],
    [253941, 'SMSC Sensor 1', 0, 44.75857, -93.46464, 95.8],
    [255562, 'Lake Forest', 0, 45.06069, -93.22147, 17.8],
]

# Create DataFrame
df_all = pd.DataFrame(data, columns=fields)

# Preview the data
print(df_all.head())
print("Number of sensors:", len(df_all))
print(df_all['location_type'].value_counts())

#Plot of Sensors
plt.figure(figsize=(10, 8))

# Outdoor sensors (location_type = 0)
outdoor = df_all[df_all['location_type'] == 0]
plt.scatter(outdoor['longitude'], outdoor['latitude'], c='blue', label='Outdoor Sensor', alpha=0.9, s=10)

# Indoor sensors (location_type = 1)
indoor = df_all[df_all['location_type'] == 1]
plt.scatter(indoor['longitude'], indoor['latitude'], c='orange', label='Indoor Sensor', alpha=0.9, s=10)

# Bounding box
plt.axhline(45.414551, color='red', linestyle='--', linewidth=0.8)
plt.axhline(44.471236, color='red', linestyle='--', linewidth=0.8)
plt.axvline(-94.012557, color='red', linestyle='--', linewidth=0.8)
plt.axvline(-92.731911, color='red', linestyle='--', linewidth=0.8)
plt.plot([], [], 'r--', label='Bounding Box')  


plt.title("PurpleAir Sensors and Project Bounding Box")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



#(Bounding Box)
nwlng = -94.012557
nwlat = 45.414551
selng = -92.731911
selat = 44.471236

#Choosing suitable sensors
selected = df_all[
    (df_all['location_type'] == 0) &
    (df_all['longitude'] >= nwlng) & (df_all['longitude'] <= selng) &
    (df_all['latitude'] >= selat) & (df_all['latitude'] <= nwlat) &
    (df_all['pm2.5_60minute'] > 0)
]

print("Number of selected sensors:", len(selected))
print(selected[['sensor_index', 'name', 'latitude', 'longitude', 'pm2.5_60minute']])

selected.to_csv("selected_sensors.csv", index=False)
