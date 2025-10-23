import pandas as pandu
import numpy as np
# Writing the script showing ordinal encoding
print("Rate the following cartoons, from the following words- average, good, great, excellent and love.")
a = input("rating for doraemon ").lower()
b = input("rating for ninja hathori ").lower()
c = input("rating for tom & jerry ").lower()
d = input("rating for shinchan ").lower()
e = input("rating for horrid henry ").lower()
f = input("rating for motu patlu ").lower()
g = input("rating for powerpuff girls ").lower()
Data_Set = {"Cartoons":["Doraemon","Ninja Hathori","Tom & Jerry","Shinchan","Horrid Henry","Motu Patlu","Powerpuff Girls"],
            "Ratings":[a,b,c,d,e,f,g]}
ds = pandu.DataFrame(Data_Set)
print(ds)
Rating_Order = ["average","good","great","excellent","love"]
R_O = {rating:index for index,rating in enumerate(Rating_Order)}    
print(R_O)
ds["Ordinal_Encoded_Ratings"] = ds["Ratings"].map(R_O)
print(ds)



# Writing the script showing one-hot encoding.
# Just for fun, please don't bully me after this.

print("Help me know my seniors. \n Select a adjective from the follwing options for each of the person. \n The adjectives are as follows- strict, cool, gossipy, bully, aura")
a = input("Enter a adjective for Ishan bhaiya ").lower()
b = input("Enter a adjective for Vishrut bhaiya ").lower()
c = input("Enter a adjective for Nikunj bhaiya ").lower()
d = input("Enter a adjective for Sukriti didi ").lower()
e = input("Enter a adjective for Ujjwal bhaiya ").lower()
f = input("Enter a adjective for Pihu didi ").lower()
AIMS_Seniors = {"Names":["Ishan Bhaiya","Vishrut Bhaiya","Nikunj Bhaiya","Sukriti Didi","Ujjwal Bhaiya","Pihu Didi"],
                "Qualities":[a, b, c, d, e, f]}
A_S = pandu.DataFrame(AIMS_Seniors)
print(A_S)
Seniors_Qualities = ["strict","cool","aura","gossipy","bully"]
for quality in Seniors_Qualities:
    A_S[quality] = np.where(A_S["Qualities"] == quality, 1, 0)
print(A_S)



# Writing the script showing imputation technique.
# Now, let's level it up.

print("Now, can I please know your CGPA? \n Dekhte h AIMS ke sare maharathi kitne smart h")
print("Enter the CGPAs carefully kyuki president sahab ki CG aap logo ki CG pe depend krti h 😅")
a = float(input("enter the CGPA of Sparsh Bhaiya "))
b = float(input("enter the CGPA of Abhinav Bhaiya "))
c = float(input("enter the CGPA of Sukriti Didi "))
d = float(input("enter the CGPA of Pihu didi "))
e = float(input("enter the CGPA of Nikunj Bhaiya "))
Seniors_CG = {"Names":["Vishrut Bhaiya","Sparsh Bhaiya","Abhinav Bhaiya","Sukriti Didi","Pihu Didi","Nikunj Bhaiya"],
              "CGPA":[np.nan, a, b, c, d, e]}
S_C = pandu.DataFrame(Seniors_CG)
print(S_C)
Imp_Tech = input("Enter the imputation technique by which you would like to calculate the missing value, from the following options-\n mean, median or mode ").lower()
if Imp_Tech == "mean":
   mean_CG = S_C["CGPA"].mean(skipna=True)
   S_C["CGPA"] = S_C["CGPA"].fillna(mean_CG)
   print(S_C)
elif Imp_Tech == "median":
     median_CG = S_C["CGPA"].median(skipna=True)
     S_C["CGPA"] = S_C["CGPA"].fillna(median_CG)
     print(S_C)
elif Imp_Tech == "mode":
     Mode_CG = S_C["CGPA"].mode().iloc[0]
     S_C["CGPA"] = S_C["CGPA"].fillna(Mode_CG)
     print(S_C)
else:
     print("You have entered some other imputation techniques or anything else. Kindly enter the imputation technique as specified above.")
print("That's all for this assignment. \n Hope you liked it.")