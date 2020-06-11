from matplotlib import pyplot as plt
from mycsv import *
import numpy as np

if __name__ == "__main__":
    parser = MyCSV(delimiter=",", header=True)
    data = parser.parse("guns.csv")

#Figure 1: Gun Incidents in USA from 2012-2014
    years = sorted(set(data.year))
    months = sorted(set(data.month))
    X_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    suicides = []
    homicides = []
    for year in years:
        for month in months:
            suicide_count = 0
            homicide_count = 0
            for row in data.iterrows():
                if row.year == year and row.month == month and row.intent == "Suicide":
                    suicide_count+=1
                if row.year == year and row.month == month and row.intent == "Homicide":
                    homicide_count+=1
            suicides.append(suicide_count)
            homicides.append(homicide_count)

    plt.plot(np.arange(len(X_labels)),suicides,'g-',label="Suicides")
    plt.plot(np.arange(len(X_labels)),homicides,'r-',label="Homicides")
    plt.title("Gun Deaths\nin USA from 2012-2014")
    plt.xlabel("Months")
    plt.ylabel("Number of Gun Deaths")
    plt.xticks(np.arange(len(X_labels)),X_labels,rotation="90")
    plt.legend()
    #plt.savefig("Gun Incidents in USA from 2012-2014")
    plt.show()
    plt.close()

#Figure 2: Education Levels of Gun Suicide Victims in USA from 2012-2014
    X_labels = ["Less than\n high school","High school\n or equivalent", "Some\n college", "Graduated college\n or equivalent","Not\n available"]
    LHS_count = 0
    HS_count = 0
    C_count = 0
    GC_count = 0
    NA_count = 0
    for row in data.iterrows():
        if row.intent == "Suicide":
            if row.education == "1":
                LHS_count += 1
            if row.education == "2":
                HS_count += 1
            if row.education == "3":
                C_count += 1
            if row.education == "4":
                GC_count += 1
            if row.education == "5":
                NA_count += 1
    Y_S = [LHS_count, HS_count, C_count, GC_count, NA_count]
    LHS_count = 0
    HS_count = 0
    C_count = 0
    GC_count = 0
    NA_count = 0
    for row in data.iterrows():
        if row.intent == "Homicide":
            if row.education == "1":
                LHS_count += 1
            if row.education == "2":
                HS_count += 1
            if row.education == "3":
                C_count += 1
            if row.education == "4":
                GC_count += 1
            if row.education == "5":
                NA_count += 1
    Y_H = [LHS_count, HS_count, C_count, GC_count, NA_count]
    plt.bar(np.arange(len(X_labels)), Y_S, label="Suicides", color="cyan")
    plt.bar(np.arange(len(X_labels)), Y_H, label="Homicides", color="magenta")
    plt.xticks(np.arange(len(X_labels)), X_labels)
    plt.title("Education Levels of Gun Death Victims\nin USA from 2012-2014")
    plt.xlabel("Education Level")
    plt.ylabel("Number of Gun Deaths")
    plt.legend()
    #plt.savefig("Education Levels of Gun Suicide Victims in USA from 2012-2014")
    plt.show()
    plt.close()


#Figure 3: Race and Intent of Gun Incident Victims in USA from 2012-2014
    X_labels = ["Asian/\nPacific\nIslander","Native American/\nNative Alaskan","Black","White","Hispanic"]
    Y_S = []
    Y_H = []
    API_count = 0
    NA_count = 0
    B_count = 0
    W_count = 0
    H_count = 0
    for row in data.iterrows():
        if row.intent == "Suicide":
            if row.race == "Asian/Pacific Islander":
                API_count += 1
            if row.race == "Native American/Native Alaskan":
                NA_count += 1
            if row.race == "Black":
                B_count += 1
            if row.race == "White":
                W_count += 1
            if row.race == "Hispanic":
                H_count += 1
    Y_S = [API_count,NA_count,B_count,W_count,H_count]
    API_count = 0
    NA_count = 0
    B_count = 0
    W_count = 0
    H_count = 0
    for row in data.iterrows():
        if row.intent == "Homicide":
            if row.race == "Asian/Pacific Islander":
                API_count += 1
            if row.race == "Native American/Native Alaskan":
                NA_count += 1
            if row.race == "Black":
                B_count += 1
            if row.race == "White":
                W_count += 1
            if row.race == "Hispanic":
                H_count += 1
    Y_H = [API_count,NA_count,B_count,W_count,H_count]
    plt.bar(np.arange(len(X_labels)),Y_S, color="blue",label="Suicides")
    plt.bar(np.arange(len(X_labels)),Y_H, color="yellow", label="Homicides")
    plt.title("Race of Gun Death Victims\nin USA from 2012-2014")
    plt.xlabel("Race of Victims")
    plt.ylabel("Number of Gun Deaths")
    plt.xticks(np.arange(len(X_labels)),X_labels)
    plt.legend()
    #plt.savefig("Race and Intent of Gun Incident Victims in USA from 2012-2014")
    plt.show()
    plt.close()







