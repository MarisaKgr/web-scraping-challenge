
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)



    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)


    #Scrape the Mars News Site https://redplanetscience.com/ and 
    #collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


    #assign HTML 
    html = browser.html

    #assign BS object to parse
    news = BeautifulSoup(html, 'html.parser')

    #Find title <div class = "content_title
    news_title = news.find('div', class_='content_title').text

    #print title found
    print(news_title)


    #pull paragraph <div class ="article_teaser_body"
    #Find title <div class = "content_title
    news_p = news.find('div', class_='article_teaser_body').text

    #print title found 
    print(news_p)



    #Visit the url for the Featured Space Image site here https://spaceimages-mars.com/.
    #Use splinter to navigate the site and find the image url for the current Featured Mars Image
    #and assign the url string to a variable called featured_image_url.

    #Make sure to find the image url to the full size .jpg image.

    #Make sure to save a complete url string for this image.


    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)


    #assign HTML 
    html = browser.html

    #assign BS object to parse
    image = BeautifulSoup(html, 'html.parser')

    #Find image <img class = "headerimage fade-in'
    images = image.find('img', class_='headerimage fade-in')['src']
    featured_image_url = f'http://spaceimages-mars.com/{images}'


    #print stock image url
    print(images)
    print(featured_image_url)



    #Visit the Mars Facts webpage https://galaxyfacts-mars.com/ 

    url3 = 'https://galaxyfacts-mars.com/'
    browser.visit(url3)


    #use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

    tables = pd.read_html(url3)
    tables


    #Use Pandas to convert the data to a dataframe
    df = tables[0]
    df.columns=['Description','Mars','Earth']
    df.set_index('Description', inplace=True)
    df.head()


    #Use Pandas to convert the data to a HTML table string.
    html_table = df.to_html()
    html_table


    #strip unwanted new lines
    mars_table = html_table.replace('\n', '')


    #save table to a file
    #df.to_html('table.html')


    #open in browser
    #!open table.html


    #Visit the astrogeology site https://marshemispheres.com/ to obtain high resolution images for each of Mar's hemispheres.
    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)


    #You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    #image under "downloads" tag and h3 for title

    #assign HTML 
    html = browser.html

    #assign BS object to parse
    hemispheres = BeautifulSoup(html, 'html.parser')


    #Save both the image url string for the full resolution hemisphere image, 
    #and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store 
    #the data using the keys img_url and title.

    #create dictionary
    hemisphere_images_urls=[]

    #scrape for image information div class="collapsible results", individual hemisphere div class="item", title h3
    hemispheres_data=hemispheres.find('div', class_='collapsible results')
    hemisphere_item = hemispheres_data.find_all('div',class_='item')

    #loop through hemispheres
    for hemisphere in hemisphere_item:
    
        #grab title
        title_tag=hemisphere.find('div',class_='description')
        title = title_tag.find('h3').text
        #find image link tag
        image_link=hemisphere.find('a')['href']
    
        #travel to site for wide image
        browser.visit(url4 + image_link)
        html=browser.html
        image_soup= BeautifulSoup(html, 'html.parser')
        image_download=image_soup.find('div',class_='downloads')
        img_url = image_download.find('li').a['href']
    
        #Append the dictionary with the image url string and the hemisphere title to a list. 
        #This list will contain one dictionary for each hemisphere.
        # Example:
        #hemisphere_image_urls = [
        #{"title": "Valles Marineris Hemisphere", "img_url": "..."},
        hemisphere_images_urls.append({'title':title,'img_url':f'https://marshemispheres.com/{img_url}'})
    
    
    #print dictionary
    print(hemisphere_images_urls)


    #use function scrape to executing scraping in one python dictionary
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "Mars_Facts": mars_table,
        "hemisphere_images_urls": hemisphere_images_urls
    }

    #close browser
    browser.quit()

    #return python dictionary of mars
    return mars_dict

