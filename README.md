#Dost thou even swag?

Want to generate valid swagger json from your flask project without being forced to use other flask extensions? Just generally full of #yoloswag and want to have control of your own generated json documentation? Then you've come to the right place sister/brother.

It's simple. Just run generate\_swag.py wherever you want, whenever you want, and swagger compatible json will be created for you in the directory you ran the script as 'swag.json'

Assumptions:
- You're just using good old fashioned @app.route(<stuff\_here\>) decorators. That's where I grab everything from.
