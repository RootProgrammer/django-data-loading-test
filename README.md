# django-data-loading-test

## Rules:  

- You have to work in an existing project here [Project](https://drive.google.com/drive/folders/1kguo61I9oviPthmJ1a5DlSS2XcFQiIBW?usp=sharing)
- There is Two (2) Front-End variant Reactjs and Vuejs. Pick your favorit one.
**NB: If you are not good in Vujs or Reactjs, We suggest your to download the vuejs version and change the url to your own created post url from here [post url](https://prnt.sc/26jheo6), by this you will have the frontend data in your backend**
- Make a GitHub repository in your GitHub account  (Make sure you push the code in correct folder stracture as ours).
- First install your project and push your initial commit before start coding to your  master branch.
- Then create a new branch dev.1.0.0 and checkout in it and you will write your code  in this new branch and push your final work in this branch  
- Solve all the tasks given below. Then submit the GitHub repository URL in the bottom page form.
- You will have the demo data in `src/django_coding_test.json`. to load the demo data execute this command `python manage.py loaddata django_coding_test.json` after migrate the database


## Project Structure:

- The project has been created using pipenv . To install it run this command in your terminal/cmd "pip install pipenv"
**You need to execute npm run watch commend from the root directory to generate js, and css files which you will see in static folder under src folder
- You will have the JS source code in the src/template/assets/js directory 
- The main django project held in the src directory 
- All the config files are helds in root directory (i.e: Pipenv, package.json, webpack.mix.js)

## Tasks:  

### Migrate the database

- Create a superadmin from command line interface
- Check the [data flow diagrams](https://prnt.sc/u93yw2). You need to apply this data flow for listing products on the table and insert new products into the database.  

#### Data List: 4

- Make a list of view page of Products table data the [same as](https://prntscr.com/u944u8)                              (2)
- Make a data summary of the products [same as](https://prntscr.com/u945c2)                                              (1)  
- Make data pagination of products [same as](https://prntscr.com/u945nv)                                                 (1)

#### Data Filter: 7

- Make a product filter with product title, product variant, price range and date. [Check](https://prntscr.com/u946mf)                            (5)
- Make sure the product variant data show dynamically and group by product variant table’s variant column [same as](https://prntscr.com/u947ex)    (2)
 
#### Create Product:  5

- (Click on Product and then Create Product from Left sidebar) this page has been designed  with vuejs and reactjs you will find the code in the directory: `src/template/assets/js/components/CreateProduct.vue?js` (based on which version you downloaded).  
- As we use variant permutation thats why we use js framework, if you don't have enough knowladge in vuejs / reactjs we suggest you to download the vue project because vue have all the code to send the data to backend (django). All you need is to change the post url to your newly created url and that's all.
- Insert data into products, product_variants, product_product_prices and  product_images while create a product ,check the [screenshot](https://prntscr.com/u94u5i)
  
#### Edit Product: 10  

- Data should be loaded as same as given data in the edit product page. And it can be updated 
