import streamlit as st
import pandas as pd
import openpyxl
import plotly.express as px
from PIL import Image
import json


# Load the Excel file into a Pandas DataFrame
#df = pd.read_excel("excelData1.xlsx")
#df["Company/Brand Name"] = df["Company/Brand Name"].astype(object)

st.set_page_config(page_title='Shark Tank India Brands & Pitches')

# Load the Excel file for season 1 into a Pandas DataFrame
df_season1 = pd.read_excel("excelData1.xlsx")

# Load the Excel file for season 2 into a Pandas DataFrame
df_season2 = pd.read_excel("excelData2.xlsx")

# Specify the columns you want to keep
columns_1_s1 = ['#', 'Company/Brand Name', 'Product', 'Original Ask', 'Original Ask Amount in INR', 'Original Ask Equity in %', 'Final Deal', 'Final Deal Investment in INR', 'Final Deal Equity in %', 'Final Deal Debt in INR', 'Final Deal Debt Interest in %', 'Deal/No Deal', 'Namita', 'Anupam', 'Vineeta', 'Aman', 'Peyush', 'Ashneer', 'Ghazal', 'No. of Sharks on Board', 'No. of Entrepreneurs/Founders ', 'Founders Relation', 'Entrepreneur 1', 'Entrepreneur 2', 'Entrepreneur 3', 'Entrepreneur 4', 'Entrepreneur 5', 'Entrepreneur 6', 'Sector', 'Twitter (Company)', 'LinkedIn (Company)', 'Instagram (Company)', 'Facebook (Company)', 'Youtube (Company)', 'Website (Company)', 'Sharks on Board', 'Entrepreneurs/Founders', 'Original Ask Valuation in INR Crores', 'Final Deal Valuation in INR Crores', 'Original Ask Amount in INR Lakhs', 'Final Deal Amount in INR Lakhs']
columns_1_s2 = ['#', 'Company/Brand Name', 'Product', 'Original Ask', 'Original Ask Amount in INR', 'Original Ask Equity in %', 'Final Deal', 'Final Deal Investment in INR', 'Final Deal Equity in %', 'Final Deal Debt in INR', 'Final Deal Debt Interest in %', 'Deal/No Deal', 'Namita', 'Anupam', 'Vineeta', 'Aman', 'Peyush', 'Amit', 'No. of Sharks on Board', 'No. of Entrepreneurs/Founders ', 'Founders Relation', 'Entrepreneur 1', 'Entrepreneur 2', 'Entrepreneur 3', 'Entrepreneur 4', 'Entrepreneur 5', 'Entrepreneur 6', 'Sector', 'Twitter (Company)', 'LinkedIn (Company)', 'Instagram (Company)', 'Facebook (Company)', 'Youtube (Company)', 'Website (Company)', 'Sharks on Board', 'Entrepreneurs/Founders', 'Original Ask Valuation in INR Crores', 'Final Deal Valuation in INR Crores', 'Original Ask Amount in INR Lakhs', 'Final Deal Amount in INR Lakhs']
columns_sector = ['Sectors', 'No. of Sectors']
columns_deal = ['Deals that happened', 'No. of Deals']
columns_founders = ['Founders per Company', 'No. of Founders per Company']
columns_sharkspd = ['Sharks on Board per Deal', 'No. of Sharks on Board per Deal']
columns_sharks = ['Sharks', 'No. of deals made by a Shark']
columns_fr = ['Founders Relationship', 'Number of FR']

# Create a new DataFrame with only the specified columns
df_s1 = df_season1[columns_1_s1]
df_s2 = df_season2[columns_1_s2]
df_s1_sectors = df_season1[columns_sector]
df_s1_sectors = df_s1_sectors.iloc[:14]
df_s2_sectors = df_season2[columns_sector]
df_s2_sectors = df_s2_sectors.iloc[:14]
df_s1_deals = df_season1[columns_deal]
df_s1_deals = df_s1_deals.iloc[:2]
df_s2_deals = df_season2[columns_deal]
df_s2_deals = df_s2_deals.iloc[:2]
df_s1_founders = df_season1[columns_founders]
df_s1_founders = df_s1_founders.iloc[:6]
df_s2_founders = df_season2[columns_founders]
df_s2_founders = df_s2_founders.iloc[:6]
df_s1_sharkspd = df_season1[columns_sharkspd]
df_s1_sharkspd = df_s1_sharkspd.iloc[:8]
df_s2_sharkspd = df_season2[columns_sharkspd]
df_s2_sharkspd = df_s2_sharkspd.iloc[:7]
df_s1_sharks = df_season1[columns_sharks]
df_s1_sharks = df_s1_sharks.iloc[:7]
df_s2_sharks = df_season2[columns_sharks]
df_s2_sharks = df_s2_sharks.iloc[:6]
df_s1_fr = df_season1[columns_fr]
df_s1_fr = df_s1_fr.iloc[:5]
df_s2_fr = df_season2[columns_fr]
df_s2_fr = df_s2_fr.iloc[:5]

# convert the dataframe to a JSON object
data_s1 = df_s1.to_json(orient='records')
data_s2 = df_s2.to_json(orient='records')
data_s1_sectors = df_s1_sectors.to_json(orient='records')
data_s2_sectors = df_s2_sectors.to_json(orient='records')
data_s1_deals = df_s1_deals.to_json(orient='records')
data_s2_deals = df_s2_deals.to_json(orient='records')
data_s1_founders = df_s1_founders.to_json(orient='records')
data_s2_founders = df_s2_founders.to_json(orient='records')
data_s1_sharkspd = df_s1_sharkspd.to_json(orient='records')
data_s2_sharkspd = df_s2_sharkspd.to_json(orient='records')
data_s1_sharks = df_s1_sharks.to_json(orient='records')
data_s2_sharks = df_s2_sharks.to_json(orient='records')
data_s1_fr = df_s1_fr.to_json(orient='records')
data_s2_fr = df_s2_fr.to_json(orient='records')

#print the json object
# print(data_s1)
# print(data_s2)

with open('data_s1.json', 'w') as f:
    json.dump(data_s1, f)

with open('data_s2.json', 'w') as f:
    json.dump(data_s2, f)

with open('data_s1_sectors.json', 'w') as f:
    json.dump(data_s1_sectors, f)

with open('data_s2_sectors.json', 'w') as f:
    json.dump(data_s2_sectors, f)

with open('data_s1_deals.json', 'w') as f:
    json.dump(data_s1_deals, f)

with open('data_s2_deals.json', 'w') as f:
    json.dump(data_s2_deals, f)

with open('data_s1_founders.json', 'w') as f:
    json.dump(data_s1_founders, f)

with open('data_s2_founders.json', 'w') as f:
    json.dump(data_s2_founders, f)

with open('data_s1_sharkspd.json', 'w') as f:
    json.dump(data_s1_sharkspd, f)

with open('data_s2_sharkspd.json', 'w') as f:
    json.dump(data_s2_sharkspd, f)

with open('data_s1_sharks.json', 'w') as f:
    json.dump(data_s1_sharks, f)

with open('data_s2_sharks.json', 'w') as f:
    json.dump(data_s2_sharks, f)

with open('data_s1_fr.json', 'w') as f:
    json.dump(data_s1_fr, f)

with open('data_s2_fr.json', 'w') as f:
    json.dump(data_s2_fr, f)


#"Company/Brand Name", "Product",	"Original Ask",	"Original Ask Amount in INR",	"Original Ask Equity in %",	"Final Deal",	"Final Deal Investment in INR",	"Final Deal Debt in INR",	"Final Deal Equity in %",	"Deal/No Deal",	"Anupam",	"Ashneer",	"Namita",	"Aman",	"Peyush",	"Vineeta",	"Ghazal",	"No. of Sharks on Board",	"No. of Entrepreneurs/Founders", 	"Company/Brand Name",	"Entrepreneur 1",	"Entrepreneur 2",	"Entrepreneur 3",	"Entrepreneur 4",	"Entrepreneur 5",	"Entrepreneur 6",	"Sector",	"Twitter (Company)",	"LinkedIn (Company)",	"Instagram (Company)",	"Facebook (Company)",	"Youtube (Company)",	"Website (Company)"

# Drop the column
df_season1.drop(columns='#', inplace=True)
df_season2.drop(columns='#', inplace=True)


# Display the DataFrame
#st.dataframe(df_season1)

st.markdown(
    """
    <style>
      nav .nav-item {
        cursor: pointer;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a plot
#st.line_chart(df)


# Add a dropdown menu in the sidebar to select the season
season = st.sidebar.selectbox('Select season', ['Season 2', 'Season 1'])

# Display the DataFrame for the selected season
if season == 'Season 2':
    # Create a website header
    #st.header('Shark Tank India', align='center')
    st.markdown(
        """
        <h1 align="center">Shark Tank India: Season 2</h1>
        
        """,
        unsafe_allow_html=True,
    )

    sts2 = "stis2.jpg"
    st.image(sts2, width=720)


    # Add some text
    #st.text('This is my website!')
    st.markdown(
        """
        <br/>
        <p align="center">Details regarding the pitches of all the companies on Shark Tank India season 2.</p>
        <p align="center">This is not associated with the official Shark Tank India by Sony TV. It is an independent project with data collected from Wikipedia and Sony/Shark Tank India websites.</p>
        <br/>
        <p align="center">
        <a href="https://www.belohith.com" style="text-decoration: none">made by Lohith Bollineni</a>
        </p> 
        <br/>
        <h3 align="center">We always need a table right? Here's one</h3>
        <p>This table has details of all the pitches from the Season 2. Literally every detail. You can download the hseet on the GitHub repo.</p><br/>
        <p>Some Features: </p>
        <p>You can resize the table by dragging the small square on the bottom right of the window.</p>
        <p>View the table fullscreen by clicking the button on top right.</p>
        <p>Click on the header of any column for ascending or descending order of items.</p>
        """,
        unsafe_allow_html=True,
    )
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # plt.bar(np.arange(len(df_season2)), df_season2["Original Ask Amount in INR"], label="Company/Brand Name")
    # Create a bar chart
    # plt.title("Original Amount Asked in INR")
    # plt.xlabel("Companies/Brands")
    # plt.ylabel("Amount in INR")
    # # Show the chart
    # st.pyplot()

    st.dataframe(df_season2)

    st.markdown(
        """
        <br/>
        <h3 align="center">Let's look at some stats!! Who doesn't love charts?</h3>
        <p>Click (toggle) on one sector (legend) to dismiss it in the chart. <br/> Double-click on one one sector (legend) to isolate it.</p>
        <p>Scroll down further for complete list of the brand/company details and their social media/website.</p>
        """,
        unsafe_allow_html=True,
    )

    pie_sector = px.pie(data_frame=df_season2, title='Number of Sectors', values='No. of Sectors', names='Sectors') 
    st.write(pie_sector)
    pie_deal = px.pie(data_frame=df_season2, title='Number of Deals', values='No. of Deals', names='Deals that happened') 
    st.write(pie_deal)
    bar_nf = px.bar(data_frame=df_season2,  x='Founders per Company', y='No. of Founders per Company', text='Founders per Company', color_discrete_sequence = ['#F63366']) 
    bar_ns = px.bar(data_frame=df_season2,  x='Sharks on Board per Deal', y='No. of Sharks on Board per Deal', text='Sharks on Board per Deal', color_discrete_sequence = ['#FFEB3B'])
    bar_sd = px.bar(data_frame=df_season2,  x='Sharks', y='No. of deals made by a Shark', text='No. of deals made by a Shark', color_discrete_sequence = ['#228B22'])
    bar_fr = px.bar(data_frame=df_season2,  x='Founders Relationship', y='Number of FR', text='Founders Relationship', color_discrete_sequence = ['#32CD32'])
    bar_oav = px.bar(data_frame=df_season2,  x='Company/Brand Name', y='Original Ask Valuation in INR Crores', text='Original Ask Valuation in INR Crores', color_discrete_sequence = ['#663399'])
    bar_fdv = px.bar(data_frame=df_season2,  x='Company/Brand Name', y='Final Deal Valuation in INR Crores', text='Final Deal Valuation in INR Crores', color_discrete_sequence = ['#9932CC'])
    bar_oaa = px.bar(data_frame=df_season2,  x='Company/Brand Name', y='Original Ask Amount in INR Lakhs', text='Original Ask Amount in INR Lakhs', color_discrete_sequence = ['#FF4500'])
    bar_fda = px.bar(data_frame=df_season2,  x='Company/Brand Name', y='Final Deal Amount in INR Lakhs', text='Final Deal Amount in INR Lakhs', color_discrete_sequence = ['#FF6347'])
    bar_oae = px.bar(data_frame=df_season2,  x='Company/Brand Name', y='Original Ask Equity in %', text='Original Ask Equity in %', color_discrete_sequence = ['#87CEEB'])
    bar_fde = px.bar(data_frame=df_season2,  x='Company/Brand Name', y='Final Deal Equity in %', text='Final Deal Equity in %', color_discrete_sequence = ['#00BFFF'])
    
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of Co - Founders in each Company</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_nf)
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of Sharks on board in each Deal made</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_ns)
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of deals made by each Shark</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_sd)
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of Co - Founders who have the same relationship</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fr)
    st.markdown(
        """
        <br/>
        <h3 align="center">Valuation asked originally by each company (in INR Crores)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_oav)
    st.markdown(
        """
        <br/>
        <h3 align="center">Valuation after the final deal for each company (in INR Crores)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fdv)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Money asked originally by each company (in INR Lakhs)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_oaa)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Money offered for each company (in INR Lakhs)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fda)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Equity offered originally by each company (in %)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_oae)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Equity given after the deal by each company (in %)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fde)
     
    
  


    st.markdown(
        """
        <br/>
        <h3 align="center">List of all the Pitches and their Social Media</h3>
        <p>If a company/brand does not have a social media page, on any platform, then clicking on that platform will redirect you to thier website. (For ex., "Girgit Store" does not have a Twitter page. Clicking on "Twitter" on their card will redirect you to their website.))</p>
        """,
        unsafe_allow_html=True,
    )

    # Iterate through each row of the dataframe
    for index, row in df_season2.iterrows():
        st.markdown(
            f"""
            <div style="display: grid; grid-template-columns: repeat(3, 1fr)">
            <div class="card" style="width: 450px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); margin: 10px; border: 1px solid #e7e7e7; border-radius: 5px;">
            <div class="card-body" style=" text-align: left; padding: 5px">
                <h4 class="card-title" style=" font-size: 18px;">{row['Company/Brand Name']}</h4>
                <h5 class="card-text" style=" font-size: 14px;">{row['Sector']} / {row['Product']}</h5>
                <p class="card-text" style=" font-size: 14px;">Original Ask: {row['Original Ask']}</p>
                <p class="card-text" style=" font-size: 14px;">Entrepreneurs/ Founders: {row['Entrepreneurs/Founders']}</p>
                <p class="card-text" style=" font-size: 14px;">Final Deal: {row['Final Deal']}</p>
                <p class="card-text" style=" font-size: 14px;">Sharks on Board: {row['Sharks on Board']}</p>
                <a target="_blank" style="text-decoration: none" href="{row['Website (Company)']}">Website - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Facebook (Company)']}">Facebook - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Instagram (Company)']}">Instagram - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Twitter (Company)']}">Twitter - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Youtube (Company)']}">Youtube</a>
            </div>
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
elif season == 'Season 1':
    # Create a website header
    #st.header('Shark Tank India', align='center')
    st.markdown(
        """
        <h1 align="center">Shark Tank India: Season 1</h1>
        
        """,
        unsafe_allow_html=True,
    )

    sts1 = "stis1.jpg"
    st.image(sts1, width=720)


    # Add some text
    #st.text('This is my website!')
    st.markdown(
        """
        <br/>
        <p align="center">Details regarding the pitches of all the companies on Shark Tank India season 1.</p>
        <p align="center">This is not associated with the official Shark Tank India by Sony TV. It is an independent project with data collected from Wikipedia and Sony/Shark Tank India websites.</p>
        <br/>
        <p align="center">
        <a href="https://www.belohith.com" style="text-decoration: none">made by Lohith Bollineni</a>
        </p> 
        <br/>
        <h3 align="center">We always need a table right? Here's one</h3>
        <p>This table has details of all the pitches from the Season 1. Literally every detail. You can download the sheet on the GitHub repo.</p><br/>
        <p>Some Features: </p>
        <p>You can resize the table by dragging the small square on the bottom right of the window.</p>
        <p>View the table fullscreen by clicking the button on top right.</p>
        <p>Click on the header of any column for ascending or descending order of items.</p>
        """,
        unsafe_allow_html=True,
    )
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # plt.bar(np.arange(len(df_season2)), df_season2["Original Ask Amount in INR"], label="Company/Brand Name")
    # Create a bar chart
    # plt.title("Original Amount Asked in INR")
    # plt.xlabel("Companies/Brands")
    # plt.ylabel("Amount in INR")
    # # Show the chart
    # st.pyplot()

    st.dataframe(df_season1)

    st.markdown(
        """
        <br/>
        <h3 align="center">Let's look at some stats!! Who doesn't love charts?</h3>
        <p>Click (toggle) on one sector (legend) to dismiss it in the chart. <br/> Double-click on one one sector (legend) to isolate it.</p>
        <p>Scroll down further for complete list of the brand/company details and their social media/website.</p>
        """,
        unsafe_allow_html=True,
    )

    pie_sector = px.pie(data_frame=df_season1, title='Number of Sectors', values='No. of Sectors', names='Sectors') 
    st.write(pie_sector)
    pie_deal = px.pie(data_frame=df_season1, title='Number of Deals', values='No. of Deals', names='Deals that happened') 
    st.write(pie_deal)
    bar_nf = px.bar(data_frame=df_season1,  x='Founders per Company', y='No. of Founders per Company', text='Founders per Company', color_discrete_sequence = ['#F63366']) 
    bar_ns = px.bar(data_frame=df_season1,  x='Sharks on Board per Deal', y='No. of Sharks on Board per Deal', text='Sharks on Board per Deal', color_discrete_sequence = ['#FFEB3B'])
    bar_sd = px.bar(data_frame=df_season1,  x='Sharks', y='No. of deals made by a Shark', text='No. of deals made by a Shark', color_discrete_sequence = ['#228B22'])
    bar_fr = px.bar(data_frame=df_season1,  x='Founders Relationship', y='Number of FR', text='Founders Relationship', color_discrete_sequence = ['#32CD32'])
    bar_oav = px.bar(data_frame=df_season1,  x='Company/Brand Name', y='Original Ask Valuation in INR Crores', text='Original Ask Valuation in INR Crores', color_discrete_sequence = ['#663399'])
    bar_fdv = px.bar(data_frame=df_season1,  x='Company/Brand Name', y='Final Deal Valuation in INR Crores', text='Final Deal Valuation in INR Crores', color_discrete_sequence = ['#9932CC'])
    bar_oaa = px.bar(data_frame=df_season1,  x='Company/Brand Name', y='Original Ask Amount in INR Lakhs', text='Original Ask Amount in INR Lakhs', color_discrete_sequence = ['#FF4500'])
    bar_fda = px.bar(data_frame=df_season1,  x='Company/Brand Name', y='Final Deal Amount in INR Lakhs', text='Final Deal Amount in INR Lakhs', color_discrete_sequence = ['#FF6347'])
    bar_oae = px.bar(data_frame=df_season1,  x='Company/Brand Name', y='Original Ask Equity in %', text='Original Ask Equity in %', color_discrete_sequence = ['#87CEEB'])
    bar_fde = px.bar(data_frame=df_season1,  x='Company/Brand Name', y='Final Deal Equity in %', text='Final Deal Equity in %', color_discrete_sequence = ['#00BFFF'])
    
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of Co - Founders in each Company</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_nf)
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of Sharks on board in each Deal made</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_ns)
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of deals made by each Shark</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_sd)
    st.markdown(
        """
        <br/>
        <h3 align="center">Number of Co - Founders who have the same relationship</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fr)
    st.markdown(
        """
        <br/>
        <h3 align="center">Valuation asked originally by each company (in INR Crores)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_oav)
    st.markdown(
        """
        <br/>
        <h3 align="center">Valuation after the final deal for each company (in INR Crores)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fdv)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Money asked originally by each company (in INR Lakhs)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_oaa)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Money offered for each company (in INR Lakhs)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fda)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Equity offered originally by each company (in %)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_oae)
    st.markdown(
        """
        <br/>
        <h3 align="center">Amount of Equity given after the deal by each company (in %)</h3>
        """,
        unsafe_allow_html=True,
    )
    st.write(bar_fde)
     
    
  


    st.markdown(
        """
        <br/>
        <h3 align="center">List of all the Pitches and their Social Media</h3>
        <p>If a company/brand does not have a social media page, on any platform, then clicking on that platform will redirect you to thier website. (For ex., "Girgit Store" does not have a Twitter page. Clicking on "Twitter" on their card will redirect you to their website.))</p>
        """,
        unsafe_allow_html=True,
    )

    # Iterate through each row of the dataframe
    for index, row in df_season1.iterrows():
        st.markdown(
            f"""
            <div style="display: grid; grid-template-columns: repeat(3, 1fr)">
            <div class="card" style="width: 450px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); margin: 10px; border: 1px solid #e7e7e7; border-radius: 5px;">
            <div class="card-body" style=" text-align: left; padding: 5px">
                <h4 class="card-title" style=" font-size: 18px;">{row['Company/Brand Name']}</h4>
                <h5 class="card-text" style=" font-size: 14px;">{row['Sector']} / {row['Product']}</h5>
                <p class="card-text" style=" font-size: 14px;">Original Ask: {row['Original Ask']}</p>
                <p class="card-text" style=" font-size: 14px;">Entrepreneurs/ Founders: {row['Entrepreneurs/Founders']}</p>
                <p class="card-text" style=" font-size: 14px;">Final Deal: {row['Final Deal']}</p>
                <p class="card-text" style=" font-size: 14px;">Sharks on Board: {row['Sharks on Board']}</p>
                <a target="_blank" style="text-decoration: none" href="{row['Website (Company)']}">Website - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Facebook (Company)']}">Facebook - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Instagram (Company)']}">Instagram - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Twitter (Company)']}">Twitter - </a>
                <a target="_blank" style="text-decoration: none" href="{row['Youtube (Company)']}">Youtube</a>
            </div>
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

