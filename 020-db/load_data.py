import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model

# gdp

def load_gdp():
    gdp_data = pd.read_csv('gdp_per_capita.csv', thousands=',', 
                           delimiter = '\t', encoding='latin1',
                           na_values='n/a')

    # print(gdp_data['Country'], gdp_data['2015'])                       
    gdp_data.rename(columns={"2015": 'GDP per capita'}, inplace = True)
    gdp_data.set_index("Country", inplace = True)
    # print(gdp_data.loc[:, ['Country','GDP per capita']])
    # print(gdp_data['GDP per capita']['Austria'])
    return gdp_data
    
def load_oecd(filename = 'oecd_bli_2015.csv'):
    oecd_data = pd.read_csv(filename, thousands=',')
    oecd_data = oecd_data[oecd_data["INEQUALITY"] == "TOT"]
    oecd_data = oecd_data.pivot(index = "Country", columns ="Indicator", 
                                values = "Value")    
    return oecd_data
    
if __name__ == '__main__':
    gdp_data = load_gdp()
    oecd_data = load_oecd()
    
    country_stats = pd.merge(left=oecd_data, right=gdp_data, 
                             left_index = True, right_index = True)
    
    x = np.c_[country_stats[["GDP per capita"]]]
    y = np.c_[country_stats[["Life satisfaction"]]]
    
    print(oecd_data)
    # print(country_stats[["GDP per capita", "Life satisfaction"]])
    
    country_stats.plot(kind='scatter', x="GDP per capita", y="Life satisfaction")
    plt.show()
    
    model = sklearn.linear_model.LinearRegression()
    model.fit(x,y)
    unknown_gdp = [[25000]]
    print(model.predict(unknown_gdp))
    # print(model)
    