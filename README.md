# Introduction 

This is a Url Shortener **RESTful** API built **Django** 

# Documentation 

There are only two **end-points** in this API, one for creating new url shorts and another to redirect user from requested short url to the original one.   

Creating a new Short Url:
      
    POST /shorten  

post request body:     
 
**original_url**: The url of the website that will be redirected to, this field is required and must be in valid url format.    

**short_url**: The unique name you want to customize the shortened link with. This field is optional, If it is not included it will be generated automatically.<br> If the unique name you select has been taken, rather than return an error, a number is attached to it. For example, if you want to use ```127.0.0.1:8000/myname``` and ```myname has been used```, it returns ```127.0.0.1:8000/myname-1```. If you try to use the same value again, it increments the number. For example if you try to use ```myname``` again it returns ```myname-2```

To Redirect from shortened url to original url we use:       
   
    GET 127.0.0.1/{short_url}
# Url-Shortener
