import pandas as pd
import sqlite3
import mysql.connector as mysql
import matplotlib.pyplot as plt
import numpy as np
import os
from sqlalchemy import create_engine


economic_data=pd.read_csv('/Users/jin/python/economic_data_project.csv')
print(economic_data)
economic_data=economic_data.dropna()
print(economic_data)
economic_data=economic_data.transpose()
print(economic_data)
# economic_data.to_csv('/Users/jin/python/economic_data_project_processed.csv')
economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
print(economic_data)

engine=create_engine("mysql+pymysql://root:123456@localhost:3306/economic_data_mysql")
economic_data.to_sql("economc_data", con=engine, if_exists="append", index=False)


conn=sqlite3.connect('economic_data_final.db')
economic_data.to_sql(con=conn, name="economic_table", if_exists="replace", index=False)

#Unemployment and GDP growth rate-graph of trend and correlation


#Japan-trend graph
# plt.plot(economic_data["Year"], economic_data["Unemployment_Rate_Jap"], color="red", label="Unemployment")
# plt.plot(economic_data["Year"], economic_data["GDP_growth_Jap"], color="blue", label="GDP Growth")
# plt.xlabel("Year")
# plt.ylabel("Rate")
# plt.xticks(economic_data["Year"])
# plt.title("Japan GDP growth rate and unemployment rate trend")
# plt.legend()
# plt.show()

# Japan correlation graph and correlation value
# correlation=economic_data["GDP_growth_Jap"].corr(economic_data["Unemployment_Rate_Jap"])
# plt.scatter(economic_data["Unemployment_Rate_Jap"], economic_data["GDP_growth_Jap"])
# plt.title(f"Correlation between unemployment rate and GDP growth rate, Japan:{correlation:.5f}")
# plt.xlabel("Unemployment Rate")
# plt.ylabel("GDP growth rate")
# slope, intercept=np.polyfit(economic_data["Unemployment_Rate_Jap"], economic_data["GDP_growth_Jap"], 1)
# plt.plot(economic_data["Unemployment_Rate_Jap"], slope*economic_data["Unemployment_Rate_Jap"]+intercept, label="trend line", color="blue")
# plt.show()

#总路径
PATH=('/Users/jin/desktop/编程/数据图/')

# defining gdp unemployment trend graph
def draw_gdp_unemployment_trend(unemployment_country, gdp_growth_country, title):
    SUBPATH=PATH+'GDP和失业/'   #分路径
    folder_path = os.path.join(SUBPATH, title)  #自动创建文件夹
    os.makedirs(folder_path, exist_ok=True)     #自动创建文件夹
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    plt.figure(figsize=(12,7))
    plt.plot(economic_data["Year"], economic_data[f"Unemployment_Rate_{unemployment_country}"], color="red", label="Unemployment")
    plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{gdp_growth_country}"], color="blue", label="GDP Growth")
    plt.xlabel("Year")
    plt.ylabel("Rate")
    plt.xticks(economic_data["Year"])
    plt.title(f"{title}GDP growth rate and unemployment rate trend")
    plt.legend()
    plt.savefig(f"{SUBPATH}{title}/{title}GDP_growth_rate_and_unemployment_rate_trend.png")
    # plt.show()
    plt.close()

# defining gdp unemployment correlation graph
def correlation_graph_and_correlation_value(unemployment_country, gdp_growth_country, title):
    SUBPATH=PATH+'GDP和失业/'   #分路径
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    folder_path = os.path.join(SUBPATH, title)  #自动创建文件夹
    os.makedirs(folder_path, exist_ok=True)     #自动创建文件夹

    correlation=economic_data[f"GDP_growth_{gdp_growth_country}"].corr(economic_data[f"Unemployment_Rate_{unemployment_country}"])
    plt.figure(figsize=(12,7))
    plt.scatter(economic_data[f"Unemployment_Rate_{unemployment_country}"], economic_data[f"GDP_growth_{gdp_growth_country}"])
    plt.title(f"Correlation between unemployment rate and GDP growth rate, {title}:{correlation:.5f}")
    plt.xlabel("Unemployment Rate")
    plt.ylabel("GDP growth rate")
    slope, intercept=np.polyfit(economic_data[f"Unemployment_Rate_{unemployment_country}"], economic_data[f"GDP_growth_{gdp_growth_country}"], 1)
    plt.plot(economic_data[f"Unemployment_Rate_{unemployment_country}"], slope*economic_data[f"Unemployment_Rate_{unemployment_country}"]+intercept, label="trend line", color="blue")
    plt.savefig(f"{SUBPATH}{title}/{title} correlation between unemployment rate and GDP growth rate.png")
    # plt.show()
    plt.close()
    

#China trend graph
# draw_gdp_unemployment_trend(unemployment_country="Chi", gdp_growth_country="Chi", title="China")
# correlation_graph_and_correlation_value(unemployment_country="Chi", gdp_growth_country="Chi", title="China")


# input country thgourh input
# while True:
#     unem_nation=input("input the country for unemployment data")
#     gdp_nation=input("input the country for gdp data")
#     title_nation=input("input the country fullname for the title")
#     draw_gdp_unemployment_trend(unemployment_country=unem_nation, gdp_growth_country=gdp_nation, title=title_nation)
#     correlation_graph_and_correlation_value(unemployment_country=unem_nation, gdp_growth_country=gdp_nation, title=title_nation)
#     stop=input("have you finished?")
#     if stop=="yes":
#         break


#GDP growth and government debt
def GDP_growth_relation_with_government_debt_trend(title, gdp_growth_country, government_debt_country):
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    SUBPATH=PATH+'GDP和债务/'
    folder=os.path.join(SUBPATH, title)
    os.makedirs(folder, exist_ok=True)
    plt.figure(12,7)
    plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{gdp_growth_country}"], color="red", label="GDP growth rate")
    plt.plot(economic_data["Year"], economic_data[f"Central_government_debt_{government_debt_country}"], color="blue", label="central government debt")
    plt.xlabel("Year")
    plt.ylabel("%")
    plt.title(f"{title} GDP growth and Government debttrend")
    plt.xticks(economic_data["Year"])
    plt.legend()
    plt.savefig(f"{SUBPATH}{title}/{title} GDP growth and Government debt trend.png")
    # plt.show()
    plt.close()

def GDP_growth_correlation_with_government_debt(title, gdp_growth_country, government_debt_country):
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    SUBPATH=PATH+'GDP和债务/'
    folder=os.path.join(SUBPATH, title)
    os.makedirs(folder,exist_ok=True)
    plt.figure(12,7)
    plt.scatter(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"Central_government_debt_{government_debt_country}"])
    plt.xlabel("GDP growth")
    plt.ylabel("Government debt")
    slope, intercept=np.polyfit(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"{government_debt_country}"])
    plt.plot(economic_data[f"GDP_growth_{gdp_growth_country}"], slope*economic_data[f"GDP_growth_{gdp_growth_country}"]+intercept, label="trend line")
    correlation=economic_data[f"GDP_growth_{gdp_growth_country}"].corr(economic_data[f"{government_debt_country}"])
    plt.title(f"{title} correlation between GDP and government debt:{correlation:3f}")
    plt.savefig(f"{SUBPATH}{title}/{title} correlation between GDP and government debt.png")
    plt.close()

#GDP growth and inflation rate
def GDP_growth_relation_with_inflation(title, gdp_growth_country, inflation_country):
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    SUBPATH=PATH+'GDP和通货膨胀/'
    folder=os.path.join(SUBPATH, title)
    os.makedirs(folder, exist_ok=True)
    plt.figure(12,7)
    plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{gdp_growth_country}"], color="red", label="GDP growth rate")
    plt.plot(economic_data["Year"], economic_data[f"Inflation_according_to_CPI_{inflation_country}"], color="blue", label="inflation")
    plt.xlabel("Year")
    plt.ylabel("%")
    plt.title(f"{title} GDP growth and inflation")
    plt.xticks(economic_data["Year"])
    plt.legend()
    plt.savefig(f"{SUBPATH}{title}/{title} GDP growth and inflation trend.png")
    # plt.show()
    plt.close()


def gdp_growth_and_inflation_correlation(title, gdp_growth_country, inflation_country):
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    SUBPATH=PATH+'GDP和通货膨胀/'
    file_path=os.path.join(SUBPATH, title)
    os.makedirs(file_path, exist_ok=True)
    plt.figure(12,7)
    plt.scatter(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"Inflation_according_to_CPI_{inflation_country}"])
    plt.xlabel("GDP growth")
    plt.ylabel("Inflation")
    slope, intercept=np.polyfit(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"Inflation_according_to_CPI_{inflation_country}"])
    plt.plot(economic_data[f"GDP_growth_{gdp_growth_country}"], slope*economic_data[f"GDP_growth_{gdp_growth_country}"]+intercept, label="trend line")
    correlation=economic_data[f"GDP_growth_{gdp_growth_country}"].corr(economic_data[f"Inflation_according_to_CPI_{inflation_country}"])
    plt.title(f"{title} correlation between GDP and inflation:{correlation:3f}")
    plt.savefig(f"{SUBPATH}{title}/{title} correlation between GDP and inflation.png")
    plt.close()

#GDP和基尼系数
def GDP_growth_relation_with_gini(title, gdp_growth_country, gini_country):
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    SUBPATH=PATH+'GDP和基尼系数/'
    folder=os.path.join(SUBPATH, title)
    os.makedirs(folder, exist_ok=True)
    plt.figure(12,7)
    plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{gdp_growth_country}"], color="red", label="GDP growth rate")
    plt.plot(economic_data["Year"], economic_data[f"Gini_index_{gini_country}"], color="blue", label="gini coeffieicnt")
    plt.xlabel("Year")
    plt.ylabel("%")
    plt.title(f"{title} GDP growth and gini coefficient")
    plt.xticks(economic_data["Year"])
    plt.legend()
    plt.savefig(f"{SUBPATH}{title}/{title} GDP growth and gini coefficient trend.png")
    # plt.show()
    plt.close()



def gdp_gini_correlation(title, gdp_growth_country, gini_country):
    economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
    SUBPATH=PATH+'GDP和基尼系数/'
    file_path=os.path.join(SUBPATH, title)
    os.makedirs(file_path, exist_ok=True)
    plt.figure(12,7)
    plt.scatter(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"Gini_index_{gini_country}"])
    plt.xlabel("GDP growth")
    plt.ylabel("Gini coeffieicnt")
    slope, intercept=np.polyfit(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"Gini_index_{gini_country}"])
    plt.plot(economic_data[f"GDP_growth_{gdp_growth_country}"], slope*economic_data[f"GDP_growth_{gdp_growth_country}"]+intercept, label="trend line")
    correlation=economic_data[f"GDP_growth_{gdp_growth_country}"].corr(economic_data[f"Gini_index_{gini_country}"])
    plt.title(f"{title} correlation between GDP and gini coefficient:{correlation:3f}")
    plt.savefig(f"{SUBPATH}{title}/{title} correlation between GDP and gini coefficient.png")
    plt.close()


#gdp and relative poverty
def gdp_and_relative_poverty_trend(title, gdp_growth_country, relative_poverty_country):
    SUBPATH=PATH+'GDP和相对贫困/'
    file_path=os.path.join(SUBPATH, title)
    os.makedirs(file_path, exist_ok=True)
    plt.figure(12,7)
    plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{gdp_growth_country}"], color="red", label="GDP growth rate")
    plt.plot(economic_data["Year"], economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"], color="blue", label="gini coeffieicnt")
    plt.xlabel("Year")
    plt.ylabel("%")
    plt.title(f"{title} GDP growth and relative poverty")
    plt.xticks(economic_data["Year"])
    plt.legend()
    plt.savefig(f"{SUBPATH}/{title}/{title} GDP growth and relative poverty")



def gdp_and_relative_poverty_correlation(title, gdp_growth_country, relative_poverty_country):
    SUBPATH=PATH+'GDP和相对贫困/'
    file_path=os.path.join(SUBPATH, title)
    os.makedirs(file_path, exist_ok=True)
    plt.figure(12,7)
    plt.scatter(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"])
    slope, intercept=np.polyfit(economic_data[f"GDP_growth_{gdp_growth_country}"], economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"])
    plt.plot(economic_data[f"GDP_growth_{gdp_growth_country}"], slope*economic_data[f"GDP_growth_{gdp_growth_country}"]+intercept, color="blue", label="trend line")
    plt.xlabel("GDP growth")
    plt.ylabel("Relative poverty")
    correlation=economic_data[f"GDP_growth_{gdp_growth_country}"].corr(economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"])
    plt.title(f"{title} GDP growth and relative poverty correlation:{correlation:3f}")
    plt.legend()
    plt.savefig(f"{SUBPATH}/{title}/{title} GDP growth and relative poverty")


#write in a class
class economic:
    def __init__(self, gdp_growth_country, title):
        self.gdp=gdp_growth_country
        self.title=title


    def draw_gdp_unemployment_trend(self, unemployment_country):
        SUBPATH=PATH+'GDP和失业/'   #分路径
        folder_path = os.path.join(SUBPATH, self.title)  #自动创建文件夹
        os.makedirs(folder_path, exist_ok=True)     #自动创建文件夹
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        plt.figure(figsize=(12,7))
        plt.plot(economic_data["Year"], economic_data[f"Unemployment_Rate_{unemployment_country}"], color="red", label="Unemployment")
        plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{self.gdp}"], color="blue", label="GDP Growth")
        plt.xlabel("Year")
        plt.ylabel("Rate")
        plt.xticks(economic_data["Year"])
        plt.title(f"{self.title}GDP growth rate and unemployment rate trend")
        plt.legend()
        plt.savefig(f"{SUBPATH}{self.title}/{self.title}GDP_growth_rate_and_unemployment_rate_trend.png")
        # plt.show()
        plt.close()

    def GDP_growth_relation_with_government_debt_trend(self, government_debt_country):
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        SUBPATH=PATH+'GDP和债务/'
        folder=os.path.join(SUBPATH, self.title)
        os.makedirs(folder, exist_ok=True)
        plt.figure(12,7)
        plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{self.gdp}"], color="red", label="GDP growth rate")
        plt.plot(economic_data["Year"], economic_data[f"Central_government_debt_{government_debt_country}"], color="blue", label="central government debt")
        plt.xlabel("Year")
        plt.ylabel("%")
        plt.title(f"{self.title} GDP growth and Government debttrend")
        plt.xticks(economic_data["Year"])
        plt.legend()
        plt.savefig(f"{SUBPATH}{self.title}/{self.title} GDP growth and Government debt trend.png")
        # plt.show()
        plt.close()

    def GDP_growth_correlation_with_government_debt(self, government_debt_country):
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        SUBPATH=PATH+'GDP和债务/'
        folder=os.path.join(SUBPATH, self.title)
        os.makedirs(folder,exist_ok=True)
        plt.figure(12,7)
        plt.scatter(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"Central_government_debt_{government_debt_country}"])
        plt.xlabel("GDP growth")
        plt.ylabel("Government debt")
        slope, intercept=np.polyfit(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"{government_debt_country}"])
        plt.plot(economic_data[f"GDP_growth_{self.gdp}"], slope*economic_data[f"GDP_growth_{self.gdp}"]+intercept, label="trend line")
        correlation=economic_data[f"GDP_growth_{self.gdp}"].corr(economic_data[f"{government_debt_country}"])
        plt.title(f"{self.title} correlation between GDP and government debt:{correlation:3f}")
        plt.savefig(f"{SUBPATH}{self.title}/{self.title} correlation between GDP and government debt.png")
        plt.close()

    #GDP growth and inflation rate
    def GDP_growth_relation_with_inflation(self, inflation_country):
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        SUBPATH=PATH+'GDP和通货膨胀/'
        folder=os.path.join(SUBPATH, self.title)
        os.makedirs(folder, exist_ok=True)
        plt.figure(12,7)
        plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{self.gdp}"], color="red", label="GDP growth rate")
        plt.plot(economic_data["Year"], economic_data[f"Inflation_according_to_CPI_{inflation_country}"], color="blue", label="inflation")
        plt.xlabel("Year")
        plt.ylabel("%")
        plt.title(f"{self.title} GDP growth and inflation")
        plt.xticks(economic_data["Year"])
        plt.legend()
        plt.savefig(f"{SUBPATH}{self.title}/{self.title} GDP growth and inflation trend.png")
        # plt.show()
        plt.close()


    def gdp_growth_and_inflation_correlation(self, inflation_country):
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        SUBPATH=PATH+'GDP和通货膨胀/'
        file_path=os.path.join(SUBPATH, self.title)
        os.makedirs(file_path, exist_ok=True)
        plt.figure(12,7)
        plt.scatter(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"Inflation_according_to_CPI_{inflation_country}"])
        plt.xlabel("GDP growth")
        plt.ylabel("Inflation")
        slope, intercept=np.polyfit(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"Inflation_according_to_CPI_{inflation_country}"])
        plt.plot(economic_data[f"GDP_growth_{self.gdp}"], slope*economic_data[f"GDP_growth_{self.gdp}"]+intercept, label="trend line")
        correlation=economic_data[f"GDP_growth_{self.gdp}"].corr(economic_data[f"Inflation_according_to_CPI_{inflation_country}"])
        plt.title(f"{self.title} correlation between GDP and inflation:{correlation:3f}")
        plt.savefig(f"{SUBPATH}{self.title}/{self.title} correlation between GDP and inflation.png")
        plt.close()

    #GDP和基尼系数
    def GDP_growth_relation_with_gini(self, gini_country):
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        SUBPATH=PATH+'GDP和基尼系数/'
        folder=os.path.join(SUBPATH, self.title)
        os.makedirs(folder, exist_ok=True)
        plt.figure(12,7)
        plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{self.gdp}"], color="red", label="GDP growth rate")
        plt.plot(economic_data["Year"], economic_data[f"Gini_index_{gini_country}"], color="blue", label="gini coeffieicnt")
        plt.xlabel("Year")
        plt.ylabel("%")
        plt.title(f"{self.title} GDP growth and gini coefficient")
        plt.xticks(economic_data["Year"])
        plt.legend()
        plt.savefig(f"{SUBPATH}{self.title}/{self.title} GDP growth and gini coefficient trend.png")
        # plt.show()
        plt.close()



    def gdp_gini_correlation(self, gini_country):
        economic_data=pd.read_csv('/Users/jin/python/economic_data_project_processed_final.csv')
        SUBPATH=PATH+'GDP和基尼系数/'
        file_path=os.path.join(SUBPATH, self.title)
        os.makedirs(file_path, exist_ok=True)
        plt.figure(12,7)
        plt.scatter(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"Gini_index_{gini_country}"])
        plt.xlabel("GDP growth")
        plt.ylabel("Gini coeffieicnt")
        slope, intercept=np.polyfit(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"Gini_index_{gini_country}"])
        plt.plot(economic_data[f"GDP_growth_{self.gdp}"], slope*economic_data[f"GDP_growth_{self.gdp}"]+intercept, label="trend line")
        correlation=economic_data[f"GDP_growth_{self.gdp}"].corr(economic_data[f"Gini_index_{gini_country}"])
        plt.title(f"{self.title} correlation between GDP and gini coefficient:{correlation:3f}")
        plt.savefig(f"{SUBPATH}{self.title}/{self.title} correlation between GDP and gini coefficient.png")
        plt.close()


    #gdp and relative poverty
    def gdp_and_relative_poverty_trend(self, relative_poverty_country):
        SUBPATH=PATH+'GDP和相对贫困/'
        file_path=os.path.join(SUBPATH, self.title)
        os.makedirs(file_path, exist_ok=True)
        plt.figure(12,7)
        plt.plot(economic_data["Year"], economic_data[f"GDP_growth_{self.gdp}"], color="red", label="GDP growth rate")
        plt.plot(economic_data["Year"], economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"], color="blue", label="gini coeffieicnt")
        plt.xlabel("Year")
        plt.ylabel("%")
        plt.title(f"{self.title} GDP growth and relative poverty")
        plt.xticks(economic_data["Year"])
        plt.legend()
        plt.savefig(f"{SUBPATH}/{self.title}/{self.title} GDP growth and relative poverty")



    def gdp_and_relative_poverty_correlation(self, relative_poverty_country):
        SUBPATH=PATH+'GDP和相对贫困/'
        file_path=os.path.join(SUBPATH, self.title)
        os.makedirs(file_path, exist_ok=True)
        plt.figure(12,7)
        plt.scatter(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"])
        slope, intercept=np.polyfit(economic_data[f"GDP_growth_{self.gdp}"], economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"])
        plt.plot(economic_data[f"GDP_growth_{self.gdp}"], slope*economic_data[f"GDP_growth_{self.gdp}"]+intercept, color="blue", label="trend line")
        plt.xlabel("GDP growth")
        plt.ylabel("Relative poverty")
        correlation=economic_data[f"GDP_growth_{self.gdp}"].corr(economic_data[f"people_living_below_50%_of_median_income(relative_poverty)_{relative_poverty_country}"])
        plt.title(f"{self.title} GDP growth and relative poverty correlation:{correlation:3f}")
        plt.legend()
        plt.savefig(f"{SUBPATH}/{self.title}/{self.title} GDP growth and relative poverty")
