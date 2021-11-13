from matplotlib.pyplot import savefig
import streamlit as st

page = st.sidebar.selectbox("What do you want to see?", ("Home","Stock Analysis","Customisable Neural Network", "World Airlines", "Word Cloud Generator"))


if page == "Home":
    st.title("Welcome to Data Ed!")
    st.write(
        "#### Your go to app to brush up on data visualisation concepts!"
        )
    st.write(
        "Go ahead and find any page you like on the *sidebar*! We will go through the topic of your choice there!",
        "\n\nIf you've come here for the first time, let's get you habituated to this app first!\n\nThis is an app created by three students to help you understand the wonders of data visualisation, how it's done and how you yourself can try it out!\n\n"
        )
    st.markdown(
        "### Meet the App-Makers!\n\n|Name|GitHub Profile|\n|----|----|\n|Aishwarya Funaguskar|[Aishwarya122222e3](https://github.com/Aishwarya122222e3)|\n|Ishaan Sunita Pandita|[EmperorArthurIX](https://github.com/EmperorArthurIX)|\n|Yash Shinde|[yashshinde03](https://github.com/yashshinde03)|\n\n"
        )
    
    st.write(
        "\n\nYou may be wondering, if you're into programming, what kind of tools we have used to bring this app to you. Well, worry not, since we have made this app for education, we will let you know how we made it!",
        "\n\n### Here is the Tech Stack!\n\n"
        )
    st.markdown(
        "|Language|Usage|\n|---|---|\n|[Python](https://www.python.org/)|The base language in which this application is built!|\n|[Markdown](https://www.markdownguide.org/)|All this text that you see, it's written in MD!|"
    )
    st.write(
        "\n\nNow, you may say that's not very helpful; how can just 2 rows of a table make a website? Believe it or not, it is very much true, and let me let you in on a little secret: *Those two rows are not just 2 rows, there are millions of lines of code hidden behind them. We have just used that code to help you realise how powerful they are.*", "\n\nLet's dive a little deeper into the specifics of Python we used here.\n\n"
        )
    st.markdown(
        "##### Here are some libraries we used:\n\n|Library|Usage|\n|---|---|\n|[Streamlit](https://streamlit.io/)|It would not be an exaggeration to say that none of this would exist without Streamlit. The entire structure of the app can be attributed to Streamlit.|\n|[NumPy](https://numpy.org/)|We have many calculations in data analysis, and the library which helps us quickly do those is NumPy!|\n|[Pandas](https://pandas.pydata.org/)|This is the big brother of NumPy, the one that has OCD. We use Pandas to organise data into beautiful tables and also read and write these tables into files!|\n|[Matplotlib](https://matplotlib.org/)|This is the library that gives you quick and simple graphs!|\n|[Seaborn](https://seaborn.pydata.org/)|Big brother of Matplotlib! Gives you graphs with advanced features such as regression lines!|\n|[Folium](https://python-visualization.github.io/folium/)|Cousin of the former 2 libraries! Gives us maps of the world!|\n\n"
    )


if page == "Customisable Neural Network":
    st.title("Customisable Neural Network App")
    st.write(
        "### This is an app where you can test out a neural network!"
        )
    st.write(
        "##### You can compare how its performance is affected by various factors.",
        "Guess what, all these factors are up to you to decide! Excited?"
        )
    st.write(
        "## Let's dive in!"
        )
    st.write(
        "##### What are we checking?",
        "\n\nWe have used the [MNIST Dataset](https://en.wikipedia.org/wiki/MNIST_database) containing images of handwritten digits from 0 to 9 to train our model.",
        "\n\n##### Why Neural Networks",
        "\n\nUsing Neural Networks, we can transform image recognition into a computer-performable task. Basically, Neural Network gave your computer *eyes* **and** gave those eyes some *functionality*.",
        "On a more advanced level, this is known as [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition), that is **O**ptical **C**haracter **R**ecognition.",
        )
    st.write(
        "### Note to our beloved audience",
        "\n\nWe cannot add this function to our app right now, because it is very heavy :( and we have no money.",
        "\n\nBut fret not, you can find the github repository of this app [here](https://github.com/EmperorArthurIX/Customisable-Neural-Network-App)"
        )
    # st.markdown('<dl><dt>What are we checking?</dt><dd>We have used the <a href = "https://en.wikipedia.org/wiki/MNIST_database" target=_blank>MNIST Dataset</a> containing images of handwritten digits from 0 to 9 to train our model.</dd><dt>Why Neural Networks?</dt><dd>Using Neural Networks, we can transform image recognition into a computer-performable task. Basically, Neural Network gave your computer *eyes* **and** gave those eyes some *functionality*.On a more advanced level, this is known as <a href ="https://en.wikipedia.org/wiki/Optical_character_recognition">OCR</a>, that is <strong>O</strong>ptical <strong>C</strong>haracter <strong>R</strong>ecognition.</dd></dl>', True)

if page ==  "Stock Analysis":
    # import numpy as np
    import pandas as pd
    import mplfinance as mpf
    from PIL import Image
    # import matplotlib


    data=pd.DataFrame()
    st.title("Stock Analysis App")
    upload = st.sidebar.file_uploader("Upload a CSV file of the given format", type=['csv'])
    # st.write(upload)
    try:
        data = pd.read_csv(upload.name)
    except:
        if(upload == None):
            st.write("### Welcome to the Stock Analysis Section!\n\nYou can *upload a file* to be processed\n\n***OR***\n\nYou can view the results of the *preloaded dataset* that we have ready for you!")
        else:
            "File format is not supported"
    show_sample = st.button("Show Sample Dataset")
    hide_sample = st.button("Hide Sample Dataset")
    if show_sample and not hide_sample:
        st.image(Image.open("Sample Data.jpeg"))
    st.write(
        "### NOTE\n\nPlease adhere to the sample format while uploading a file so that we may be able to process your data properly! :)",
        "\n\nHere are some guidlines to make sure there are no unwanted errors while we process your dataset:"
        )
    st.markdown(
        "##### Data types:\n\n- Date: String or DateTime\n- Open: Integer or Float\n- High: Integer or Float\n- Low: Integer or Float\n- Close: Integer or Float\n- Volume: Integer or Float\n"
        )
    st.markdown(
        "Please maintain the order of these columns for best and accurate results.\n\n##### Heads Up:\n\nOnline, you may find these column attributes under different names, like 'Price' instead of 'Close', 'Begin' instead of 'Open'. Please try and rename these attributes to the suggested column names.\n\nAlso, in case you upload a dataset with extra columns, do not worry as long as the first six columns match with out dataset, we have taken care of that part for you! ;)"
        )
    st.write(
        "### Let's dive into the exciting part!"
        )
    
    if(upload == None):
        st.write("Currently using our dataset")
        data = pd.read_csv("MRF Stocks.csv")
    else:
        try:
            data = pd.read_csv(upload)
            st.write("Currently using your file!")
        except:
            st.write("Cannot load your dataset :(\n\nWe will show you our result till we resolve this issue")
            data = pd.read_csv("MRF Stocks.csv")
    # analyse = st.button("Analyse Dataset!")
        
    data = data[list(data.columns[0:6])]
        
    data = data.astype({data.columns[1]:'float', data.columns[2]:'float', data.columns[3]:'float', data.columns[4]:'float', data.columns[5]:'float'})
        
    data = data.rename(columns={data.columns[0]:'Date', data.columns[1]:'Open', data.columns[2]:'High', data.columns[3]:'Low', data.columns[4]:'Close', data.columns[5]:'Volume',}) 
    data.Date = pd.to_datetime(data.Date)
    max = str(data.Date.max())
    min = str(data.Date.min())
    months = pd.date_range(min,max, freq='MS').strftime("%Y-%m").tolist()
    max = max[0:-12]
    min = min[0:-12]
    month_choice = st.sidebar.selectbox("Select Month to analyse",months)  
    data = data.set_index('Date')
    data = data.sort_index()
    mpf.plot(data[month_choice],type='candle',volume=True, savefig="Output.png")
    try:
        st.image("Output.png")
    except:
        "Could not obtain plot. We are trying to resolve this issue."

if page == "Word Cloud Generator":
    import pandas as pd
    from wordcloud import WordCloud, STOPWORDS
    import numpy as np
    from PIL import Image
    st.title("Word Cloud Generator")
    st.write(
        "### Welcome to the word cloud generator application where you can upload a text file and we will generate a word cloud of the most frequent words in the file!",
        "\n\nFeel free to upload a file\n\n**OR*\n\n*Use our file as a demo!"
        )
    upload = st.sidebar.file_uploader("Upload a text file or csv file", type=['csv','txt'])
    # data = open("WordCloudText.txt", "r").read()
    data = '''Date: September 18th, 2021
Sub: Request for Registration of GDSC with Amity University Maharashtra
Hon’ble Director Sir / Hon’ble Registrar Sir,
I, the undersigned, student at Amity School of Engineering and Technology, Amity University Maharashtra, wish to bring to your kind notice that on being selected as the Google Developer Students Club (GDSC) Lead for Amity University Mumbai, I have tried to establish said club for our students.
With guidance from our faculty mentor, Dr Deepa Parasar, we have set up a core committee for the club, comprising enthusiastic and active members, abiding by guidelines provided by Google. 
We, your students, collectively seek your permission and blessings to establish our GDSC as a registered club of Amity University Mumbai.
It is a humble request that your good selves may shower your good wishes and brighten the future of our students by allowing our club GDSC AUM to be displayed as an official club on the website of Amity University Mumbai.
We not only hope, but also believe that your good selves may respond positively and as soon as conveniently possible.
Seeking your blessings,
Yours faithfully,
Tushar Sharma
For GDSC AUM'''
    if (upload == None):
        st.write(
            "If you wish to make your own word cloud, feel free to use the file uploader in the sidebar",
            "\n\nCurrently using our demo file"
        )
        # data = open("WordCloudText.txt", "r").read()
    else:
        data = open(upload.name, "r").read()


    def create_word_cloud(string):
        # maskArray = np.array(Image.open("cloud.png"))
        # cloud = WordCloud(background_color="white", max_words=200, mask=maskArray, stopwords=set(STOPWORDS))
        cloud = WordCloud(background_color="white", max_words=200, stopwords=set(STOPWORDS))
        cloud.generate(string)
        cloud.to_file("WordCloud.png")


    data = data.lower()
    create_word_cloud(data)
    try:
        st.image("WordCloud.png")
    except:
        st.write("We could not process the data. Please try again")

if page == "World Airlines":
    import folium
    from folium import plugins
    import pandas as pd
    from streamlit_folium import folium_static
    import numpy as np

    df1 = pd.read_csv("World Map air routes.csv")
    df2 = pd.read_csv("World Map airports.csv")

    df1 = df1[["Source airport", "Destination airport"]]
    df1 = df1.sort_values("Source airport")

    df2 = df2[["City","IATA","Latitude","Longitude"]]

    df2 = df2.replace('\\N',np.NaN)
    df2 = df2.dropna()
    df2 = df2.drop_duplicates()
    df2 = df2.sort_values("IATA")

    df1 = df1.replace('\\N',np.NaN)
    df1 = df1.dropna()
    df1 = df1.drop_duplicates()

    df1 = df1.set_index(df1["Source airport"])
    df2 = df2.set_index(df2["IATA"])

    city = st.sidebar.selectbox("Choose city to see routes", list(df2["City"]))
    code = df2[df2['City'] == city]
    code = code.index[0]

    dests = df1[df1["Source airport"] == code]
    dests = dests[["Destination airport"]]
    # dests.iloc[2]["Destination airport"]
    destslist = [dests.iloc[x]["Destination airport"] for x in range(len(dests))]
    lats = []
    longs = []
    for x in destslist:
        lats.append(df2.loc[x]["Latitude"])
        longs.append(df2.loc[x]["Longitude"])
    world_map = folium.Map(tiles = "Stamen Terrain", zoom_start=4)
    pops = plugins.MarkerCluster().add_to(world_map)
    for lat, long, city in zip(lats,longs,destslist):
        folium.Marker(
            location = [lat,long],
            icon = None,
            popup = city
        ).add_to(pops)
    folium_static(world_map)