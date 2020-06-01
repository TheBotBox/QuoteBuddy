<h1 align=center>QuoteBuddy</h1> 
<h4 align=center>API for one of the largest open source collection of Quotes for free </h4>   

<img src= "https://user-images.githubusercontent.com/41512314/83441571-5e0fcc80-a464-11ea-883d-39f00985ee16.png"/>  

#  Contents    
**[Features](#features)**  
**[Usage](#usage)**   
**[To-dos](#to-dos)**   
**[Contributing](#contributing)**    
**[License](#license)** 


# Features 
<ul>
  <li>Get random quote along with author</li>
  <li>Get quote by Id </li>
  <li>Update new quote </li>
</ul>     


# Usage    
### API Base URL: `thebotbox.pythonanywhere.com/` 

result :
`Status: 200`

```json
{
	"developer": "TheBotbox",
	"developer_profile": "http://thebotbox.online/",
	"base_url": "thebotbox.pythonanywhere.com",
	"project_name": "QuoteBuddy",
	"project_url": "https://github.com/TheBotBox/QuoteBuddy"
}
```  

### ENDPOINT : `/get-random-quote`
##### GET: `http://thebotbox.online/get-random-quote`    

result: 
`Status: 200`
```json
{
	"quote": "Stand amongst the ashes of a trillion dead souls, and ask the ghosts if honor matters.
                  The silence is your answer.",
	"author": "Javik (Mass Effect 3)",
	"quote_id": 1
}
```    

### ENDPOINT : `/get-quote/<quote_id>`
##### GET: `http://thebotbox.online/get-quote/3`     

result: 
`Status: 200`
```json
{
	"quote": "Everyone admires Robert Frost but not everyone takes the road less traveled",
	"author": "anonymous",
	"quote_id": 3
}
```  

Error when Id is not found in database:    
`Status: 404`  
```json
{
  "error": "Quote not found"
}
```   


### ENDPOINT : `/create-quote`
##### POST: `http://thebotbox.online/create-quote`     

#### Request: 
```json
{
	"quote": "If you want to go quickly, go alone. If you want to go far, go together",
	"author": "African Proverb"
}
```  

result: 
```json 
{
    "message": "Quote updated successfully",
    "quote_id": 4
}
```    

# To-dos   
<ul>
  <li>Get all quotes</li>  
</ul>


## Humble Appeal    
As I have made the `create-quote` api public, kindly do not post gibbrish quotes just for fun. You are allowed to post as many quotes you want but please don't post gibberish. Thanks 😀 



# Contributing   
<a href="http://thebotbox.pythonanywhere.com/post-quote" target="_blank">Post your favorite quote</a>



# License   
![alt tag](https://img.shields.io/github/license/mashape/apistatus.svg)  
```
Copyright (c) 2020 TheBotBox

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without
limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to 
whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE,ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE. 
```   

[ ![](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg) ](https://saythanks.io/to/boxforbot%40gmail.com)
