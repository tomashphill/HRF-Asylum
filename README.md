# HRF-Asylum

This is a repository containing my core contributions to the **Human Rights First, Asylum** (HRF-Asylum) project, completed in under a month. The link to the main project repository is [here](https://github.com/Lambda-School-Labs/human-rights-first-asylum-ds-a), granted the project owner hasn't removed it in the process of its iteration. This is an ongoing project, and has no doubt changed a lot since the month that I worked on it.

### About the project:

HRF-Asylum wants to create an application in order better analyze outcomes of immigrants seeking asylum. Asylum-seekers must first appeal to an *Immigration Judge* (IJ), and if they are denied asylum, then they are able to appeal to the *Board of Immigration Appeals* (BIA). Our client could not give us access to IJ documents, but they were able to share thousands of BIA documents. Unfortunately, only a fraction of the BIA documents were applications that fall under the types of cases HRF-Asylum is interested in. 

#### My task was three-fold:

1. The BIA documents are hosted on scribd, and it's unlikely to automate downloading without being throttled or banned. Scraping the text on the page doesn't work either, since scribd encrypts the text on the pdf with some font-serving voodoo. I needed to find another way.

2. Once I had the documents, convert them to text and try to extract the information the client needed to conduct analysis. It was extremely difficult because I had little domain knowledge. I'm no lawyer. The more I read these documents, the more I learned their structure and how information was conveyed in them, and the better I got at scraping the correct information.

3. Find a way to convey the information to the client. We met once with the client every week for 45 minutes to and hour, and she kept reminding us that she was not tech savvy. I wanted a simple way for her to explore the data acquired, especially get a sense of *how* much data there was given that only a small subset of the documents were applicable to HRF-Asylum. I only had one day to do this, and Streamlit was absolutely perfect for this rapid prototyping (I'm serious, it didn't require many lines of code at all).

### The notebooks:

I used colab notebooks for this project, mainly because of their absolute ease of use. Given more time, I would have transferred them to `.py` files. Notebooks proved to be an excellent way to test out scraping scripts.

#### `scribd_scraper`

This is a hacky/dirty notebook put together in order to scrape the text from PDFs hosted on scribd. It uses Selenium for browser element screenshots and follows a few steps in order to get it just right... **(1)** The headless-browser viewport must be the perfect aspect-ratio in order to capture a full PDF page. **(2)** Javascript must be used in order to declutter the page for anything that might overlap/disrupt the PDF page. **(3)** Screenshots of each PDF are taken and then either saved or directly translated into text files using `pytesseract`. No doubt at the speed the front-end of web iterates, the second process would have to be updated frequently.

#### `PDF2Text`

This simple notebook takes in a PDF and turns it into a text file using `pytesseract`. It would need to be optimized for large batches of PDFs, but it did the job. The only downside is that tesseract isn't perfect. For example, the character 'l' might be mistaken for the character '!'. Therefore, fuzzy string matching was needed when scraping from the resulting text files.

#### `BIA_Scraper`

This notebook is where the scraping gets done. Again, as I said, this was hard because I lacked the domain-knowledge (I'm no lawyer!), and there was little opportunity to ask questions to the client about the typical representation of information in these documents. What was important, though, was making sure that whatever keyword I was using to match a string in the document also encapsulated the right context, especially in order to decrease any amount of false positives. `spaCy` was incredible helpful and made certain things breezey, such as finding all the 'named entities' in the document, and separating them by type (location, person, organization, etc.). 

___

This project has especially made me interested in Natural Language Processing and its capabilities. That's a huge rabbit-hole to fall into, requiring months to years of learning before becoming proficient, but I would like to give it a go sometime soon.







