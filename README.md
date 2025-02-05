# NLP-Plagiarism

#### Natural Language Processing project to detect plagiarism in documents. It runs on python3 and needs several libraries in order to work.

[Project Description](https://drive.google.com/file/d/1Fm1zaootXzEab41j6NgOaoo9NRvy3cCa/view?usp=sharing)
[DEMO](https://drive.google.com/file/d/12PJZSpCtsUyiiVqsE9_IyJZ3r-8aqsdM/view?usp=sharing)

<p align="center">
<img src="https://live.staticflickr.com/7423/11375917205_d3a610a9b3_c.jpg" width="400" height="268">
</p> 

[[1]](https://link.springer.com/chapter/10.1007/978-3-319-10671-7_4)


### Usage

At least one document/link name must be provided as a string. 
Supported languages: Spanish

<pre><code>
python plagiarism.py [DOCUMENT_NAME] [OPTIONAL_DOCUMENT_NAME]
</code></pre>


### Document extensions supported

* docx (doc not supported)
* pdf
* links


### Requirements

* Python3
* [nltk](https://www.nltk.org/)
* [docx2txt](https://pypi.org/project/docx2txt/)
* [tika (Java 7+ required)](https://github.com/chrismattmann/tika-python)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [google (google 2.0.3)](https://pypi.org/project/google/)
* [spacy](https://spacy.io/)


