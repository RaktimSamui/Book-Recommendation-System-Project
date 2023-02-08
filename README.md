# Book-Recommendation-System-Project
## In This Project the aim is to create a Book Recommender System using a data with details of lots of books.
## So getting started with it i first import the necessarry dependencies and the data from multiple sources as the data is spread across multiple files then i quickly perform some data wrangling to make sure the data is prim and proper before going further.
![Screenshot (93)](https://user-images.githubusercontent.com/116963622/217498764-aa63497e-dbf8-4036-b5a6-00845e8520f7.png)
![Screenshot (94)](https://user-images.githubusercontent.com/116963622/217499012-00a45a4a-4cd5-4322-8325-7d4cfcd2505b.png)
## After being done with the data wrangling & data munging part i moved ahead to the Exploratory Data Analysis part where i carefully analysed the data to draw some important insights.
![Screenshot (95)](https://user-images.githubusercontent.com/116963622/217500459-0f70595d-4d62-44cf-8f33-65a5d9e3b735.png)
![Screenshot (96)](https://user-images.githubusercontent.com/116963622/217500300-e3048339-702a-47a8-a7b4-2615127d9445.png)
![Screenshot (97)](https://user-images.githubusercontent.com/116963622/217500737-1f8ff1aa-d50c-459d-bf18-8dbd5d71e10a.png)
![Screenshot (98)](https://user-images.githubusercontent.com/116963622/217500963-d2d15e1c-bca9-48e0-9f59-6200ba5aa629.png)
![Screenshot (99)](https://user-images.githubusercontent.com/116963622/217501315-5261d545-3d4d-4147-bcf4-21bb0107179d.png)
![Screenshot (100)](https://user-images.githubusercontent.com/116963622/217501524-b6e33359-97d2-42cf-9f83-cc83ae440320.png)
## After the EDA i started working on the recommendation system where i decided to implement one popularity based recommendation system and one collaborative filtering based recommendation system.
## now the popularity based recommendation works on a certain parameter to display the items, such as an IMDB's top 250 movies on their official website is calculated using this formula:
![RackMultipart2019053111532z9kq-5bb2d25a-f758-49b7-82c4-94c2bcda8009-393433847](https://user-images.githubusercontent.com/116963622/217503888-86f2caa3-cd4a-4b00-9a00-d52e28f1c878.JPG)
## where the weighted rating decides the top 250 movies.
## Similarly each organization uses their own formula two calculate the popularity or trend, so here in our case i go by a simple average rating to calculate the popularity of a book however i consider only those books that has got atleast 250 ratings so as to not take into account the books that has low frequency of ratings  such as if a book has only one rating as 10 its average rating becomes 10, this is something i would like to avoid so i take only those books whose rating's frequency is considerable and somewhat significant and that is how quite effectively i display the top 50 books with the highest average rating.
![Screenshot (107)](https://user-images.githubusercontent.com/116963622/217507532-1a9aacc3-33b6-4c1c-834a-b36b20a7d43c.png)
![Screenshot (108)](https://user-images.githubusercontent.com/116963622/217507638-9686565a-23a0-4ac5-a45a-d5d9d9bbefaf.png)
![Screenshot (109)](https://user-images.githubusercontent.com/116963622/217507832-97e7f3a2-af68-4752-a747-6ab57074fcbd.png)
![Screenshot (110)](https://user-images.githubusercontent.com/116963622/217508028-fd1a0122-507b-4bda-b0bb-8ebd607804d1.png)
## After being done with the poularity based recommender system i then started working on the collaborative filtering based recommender system, now the way this works is that each of the items that we are trying to recommend is put across the rows and the users ratings are put across the columns, and this way we get a vector for each of the items in this case it is books, then we can use any distance metric such as euclidean distance, manhattan distance etc to calculate the distance between the vectors and find out the closest vectors and then recommend the books corresponding to them.
## Using this we are essentialy trying to find similar users and recommend the books read by them to another user, here in my case i used cosine similarity to find similar users as even if the two similar objects might have high distance between them, using cosine similarity they would still have a smaller angle between them and smaller the angle the higher the similarity.
## Also i am only going to consider those users ratings who have rated more than 200 books, as for the recommendations i would only want to consider users who have experience in rating and who are frequent readers as i would prefer their rating's judgement also i am going to consider only those books who have got atleast 50 ratings as that would make the recommendation system stronger as i am only taking books that are well rated.
![Screenshot (111)](https://user-images.githubusercontent.com/116963622/217515385-e4f17adb-7402-40d6-b0b4-6518ba98e6c4.png)
![Screenshot (112)](https://user-images.githubusercontent.com/116963622/217515508-4806b23b-64e3-4a83-82e2-a5c881c4a220.png)
![Screenshot (113)](https://user-images.githubusercontent.com/116963622/217515647-97429880-3451-45e9-94d8-9ea9f2db97bf.png)
![Screenshot (114)](https://user-images.githubusercontent.com/116963622/217515805-a3e9abcc-9554-4c7b-8422-a135ecf3598a.png)
## After getting the similarity scores i wrote a function that recommends 5 books based upon a given book as the recommendation of that book.
![Screenshot (115)](https://user-images.githubusercontent.com/116963622/217517534-7593fe79-ec7e-441f-b363-dc3d49f0f016.png)
![Screenshot (116)](https://user-images.githubusercontent.com/116963622/217517694-c7e09925-8387-4501-b45d-9e8697c1dd21.png)
![Screenshot (117)](https://user-images.githubusercontent.com/116963622/217517811-38df09f2-fde0-4962-b2c1-0be5025eb2cc.png)
## And finally i went ahead and created a web application that displays top 50 books and a book recommender that recommends 5 books for a given book.
![Screenshot (118)](https://user-images.githubusercontent.com/116963622/217519427-b8653077-a890-4fe5-9801-dad98aa2c2a2.png)
![Screenshot (119)](https://user-images.githubusercontent.com/116963622/217519549-840ad0f3-9cd5-4cf7-84a8-cf4b01eb965b.png)
![Screenshot (120)](https://user-images.githubusercontent.com/116963622/217519733-65e43513-37c2-4ee4-b6a1-8b78a0371ccb.png)
![Screenshot (121)](https://user-images.githubusercontent.com/116963622/217519869-e39e1281-e4f5-4d8e-98f9-1fe53bdd38d2.png)
![Screenshot (122)](https://user-images.githubusercontent.com/116963622/217520101-8822714e-5c7a-4341-87aa-895ec754e25c.png)
![Screenshot (123)](https://user-images.githubusercontent.com/116963622/217520236-bb42be5f-1b43-46fb-b98f-624ea2d47e66.png)
![Screenshot (124)](https://user-images.githubusercontent.com/116963622/217520346-167bcfe7-14c5-4066-91fc-f9a9d8636aef.png)
![Screenshot (125)](https://user-images.githubusercontent.com/116963622/217520901-7147e221-22a0-4c84-b567-b8f82ca5f154.png)
![Screenshot (126)](https://user-images.githubusercontent.com/116963622/217521027-73692cb9-32ee-4312-a740-ee17901dd9ba.png)
![Screenshot (127)](https://user-images.githubusercontent.com/116963622/217521473-7e7869c2-4b10-4d97-93b7-7f516ff98421.png)
![Screenshot (128)](https://user-images.githubusercontent.com/116963622/217521659-b81a0fa7-f31b-4cf9-abea-09666a597bd9.png)
![Screenshot (129)](https://user-images.githubusercontent.com/116963622/217521842-525baef2-e221-4817-8a8e-8bc4bf01b3a6.png)
![Screenshot (130)](https://user-images.githubusercontent.com/116963622/217522284-cabb3f8c-1d84-48be-bff3-08b1528e54d8.png)
