import streamlit as st
import pandas as pd

# Load the Excel file into a Pandas DataFrame
#df = pd.read_excel("excelData1.xlsx")
#df["Company/Brand Name"] = df["Company/Brand Name"].astype(object)


# Load the Excel file for season 1 into a Pandas DataFrame
df_season1 = pd.read_excel("excelData1.xlsx")

# Load the Excel file for season 2 into a Pandas DataFrame
df_season2 = pd.read_excel("excelData2.xlsx")

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
        <p align="center">Details regarding the pitches of all the companies on Shark Tank India season 2.</p>
        <p align="center">This is not associated with the official Shark Tank India by Sony TV. It is an independent project with data collected from Wikipedia and Sony/Shark Tank India websites.</p>
        <br/>
        <p align="center">
        <a href="https://www.belohith.com" style="text-decoration: none">made by Lohith Bollineni</a>
        </p> 
        <br/>
        <p align="center">You can resize the table by dragging the small square on the bottom right of the window.</p>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(df_season2)


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
        <p align="center">Details regarding the pitches of all the companies on Shark Tank India season 1.</p>
        <p align="center">This is not associated with the official Shark Tank India by Sony TV. It is an independent project with data collected from Wikipedia and Sony/Shark Tank India websites.</p>
        <br/>
        <p align="center">
        <a href="https://www.belohith.com" style="text-decoration: none">made by Lohith Bollineni</a>
        </p> 
        <br/>
        <p align="center">You can resize the table by dragging the small square on the bottom right of the window.</p>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(df_season1)


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
            </div>
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

