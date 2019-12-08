# :mahjong: Awesome Chinese Pleco Flashcards [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


## :star2: What is it 
Import the attached files to into your [Pleco Chinese Dictionary](https://www.pleco.com/) and use them as flashcards to test your vocabulary. Each set of flashcards for a common textbook. 

## :books: Books available
Please find the vocabulary of the following books: 
* [HSK Standard Course 3](./HSKStandardCourse3.txt) (complete)
* [HSK Standard Course 4 上](./HSKStandardCourse41.txt) (Level 01-04)
* [New Concept Chinese 3](./NewConceptChinese3.txt) (only Chinese, translation autofilled by Pleco)
* [Contemporary Chinese For Beginners](./ContemporaryChineseForBeginners.txt) -- from [brainscape.com/(...)/contemporary-chinese-for-beginners](https://www.brainscape.com/packs/contemporary-chinese-for-beginners-3542394) (Lesson 01-11, not 100% complete)
* [Contemporary Chinese Textbook 3](./ContemporaryChineseTextbook3.txt) -- from [quizlet.com/tokiro](https://quizlet.com/tokiro) (Unit 01-05)



## :arrow_heading_down: How to import
### :iphone: Android
(source: [Pleco manual/Flashcards](http://android.pleco.com/manual/310/flash.html))
* open the requested file on Github
* download the "Raw" file (right click on "Raw" > Download target)
* in Pleco go to Flashcards "Import/Export" > Import Cards
* Choose the file you just downloaded 
* Mandatroy settings: Encoding: UTF-8. 
* I also pick the following settings (but you can choose otherwise): 
  * Definition source: Prefer File (I don't want the definition of Pleco)
  * Fill in missing fields: yes (to add traditional characters or Pinyin if missing)
  * Ambiguous entries: Promt (ask me what to do if the import dosn't know which entry it matches)
  * Duplicate entries: Update + merge (update with new definition and don't use the old anymore)
* Then click on begin import

### :phone: iPhone
(source: [Pleco manual/Flashcards](http://iphone.pleco.com/manual/30200/flashtut.html))
* I think iPhones can not download files, so you can't do it on your phone... 
* Use another device, e.g. your computer to download the "Raw" file, then you can for example send it to your phone via email. 
* Save the email attachement, then the rest is similar to Android... good luck! 

## :arrows_clockwise: How to convert Flashcards by yourself

### From [Quizlet.com](https://quizlet.com/)
* use [quizletToPleco.py](./quizletToPleco.py)
* on [quizlet.com](https://quizlet.com/) click on export, select "separate by tab", and "new line" then copy text.
* check for the right format in the script (`exp` and `sub`), run the script
* everything is saved in the `output` variable

### From [Brainscape.com](https://www.brainscape.com/)
* use [brainscrapeToPlecoFlashcards.py](./brainscrapeToPlecoFlashcards.py)
* amend `index_url`
* run the script
* everything is saved in the `output` variable
