# WikipediaCrawler
All the modules are of python3
- install bs4 module
- install requests module

run with command:
>>python3 {filename}

# Info
The crawler will open a random page of Wikipedia using the url 
https://en.wikipedia.org/wiki/Special:Random 
then it will click the first link in each article until one of the following conditions are met.
- The number of links visited > 25
- The articles start to repeat
- Article has no links present
- It reaches it's target URL which is: https://en.wikipedia.org/wiki/Philosophy