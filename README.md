# gpt-LineBot

<h3>The project involves step by setp tutorial for implementing an intelligent LINE chatbot that integrates the OpenAI API with LINE developer tools.</h3>
  
<h3>Additionally, the functions are deployed on Google Cloud Functions, eliminating the need for self-hosted servers.</h3>

## LINE Developer

1. **First, go to [line developer](https://developers.line.biz/en/?status=success) and register for a LINE Developer account.**
   
2. **Create a provider based on the Messaging API.**
   
3. **Now, you can have a conversation with the default bot in the LINE app using the QR code found in the 'Messaging API' option.**
   
4. **In the 'Messaging API' option, locate the 'Webhook settings' and enable the 'Use webhook' option.**
   
5. **Similarly, in the 'Messaging API' option, find the Channel access token and remember this token, as it will be used later.**

## Chat-gpt API

1. **Log in or register for an [OpenAI](https://openai.com/blog/openai-api) account.**
 
2. **After logging in, find the 'API Keys' option in the menu in the top left corner.**
   
3. **Create a new Secret Key and remember this key. This key will only be displayed once; if you miss it, you can delete it and create another one.**
   
4. **Ensure you have enough credits to use this API. If you don't have credits, you can still find the 'Settings' option in the top left corner menu, go to 'Billing', and purchase sufficient credits there.**

## Google Colud Function

1. **Log in or register for an [Google Cloud](https://cloud.google.com/apis) api account**
   
2. **Select the console in the upper right corner.**

3. **Search for Cloud Functions in the search field.**
 
4. **Click on CREATE FUNCTION.**
 
5. **Make some basic settings for the function, and remember to check the 'Allow unauthenticated invocations' option.**

6. **Under the 'Runtime, build connections and security settings', find 'Runtime environment variables'. Add two variables: in the Name1 field, enter API_KEY and in Value1, input the OpenAI Secret Key you copied earlier; in the Name2 field, enter LINE_ACCESS_TOKEN and in Value2, input the Channel access token you copied earlier.**
    
7. **After filling in all the details, click on ADD TRIGGER to create a new function.**

8. **You will see two files, main.py and requirement.txt. Copy the corresponding code from this repository. Be aware that the model and some API endpoints may change over time, so please pay attention to the official documentation.**

'''
* https://api.openai.com/v1/chat/completions

* https://api.line.me/v2/bot/message/reply
'''
9. 我
