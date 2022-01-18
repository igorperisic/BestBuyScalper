# BestBuyScalper
Notifies the user when a product on the Best Buy website goes from "Sold Out" to "Add to Cart" (on sale). 

The recent tech/GPU shortage fueled the idea behind this project. The purpose of it was to combat scalpers and bots when purchasing the desired out of stock product for myself and people around me. When Best Buy "drops" new batches of technology (like the PS5, XBOX, Nvidia Gpus), buyers have minutes if not seconds to add products to cart to purchase. This code gives an edge over other buyers and has sucesffuly worked for me and the people around me.  

#Functions 
notif(body) is used to send an email or a text message to user/s notifying them when their desired BestBuy product goes on sale. This notification is only sent out when there is change from "Sold Out" to "Add to Cart", this way users are not recieving notifications every second. 
openPage() opens two webpages; one is the product page and the other one adds the product to cart right away
webAccess() from the product url, using html it parses through the text and returns the output on the "Add To Cart" button. The output on the button could either be "Sold Out" or "Add to Cart"

The Main part of the code loops every second and runs the correct functions. A few try and excepts have been placed in case the Best Buy website blocks access.

If the webAccess returns "Sold Out", the code will send one email/text notifying the users of the "Sold Out" status. It will continue to loop in this section, without sending additoinal notifications, until the status of the product changes to "Add to Cart". Once the status changes, users will be notified with a different email/text and a link to the product and at the same time it will automatically open the product webpage using the openPage() function on the computer.


