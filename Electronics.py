import pandas as pd
from pdf_code import create_receipt

class Articles :
    def __init__(self, article_id):
        self.article_id = article_id


    def get_name (self, user_id) :
        art_name = df.loc[df["id"] == self.article_id, ["name"]]
        return art_name
class get_receipt :
    pass

df = pd.read_csv("articles.csv")
print (df)
user_id = int(input ("Please enter the code of the article you want to purchase"))
order_article = Articles(user_id)
art_names = order_article.get_name (user_id)
instock = df.loc[df["id"] == user_id, ["in stock"]]
final_stock = instock["in stock"] - 1
df.loc[df["id"] == user_id, "in stock"] = final_stock
df.to_csv ("articles.csv", index=False)
print (final_stock.squeeze())
print (art_names.squeeze())
print ("art name : ", art_names)
price = df.loc[df["id"] == user_id, "price"].squeeze()
create_receipt (art_names.squeeze(), price)