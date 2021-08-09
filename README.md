# data_loader
STEP TO RUN CODE:

1.Download the whole file from GITHUB
2. run the main.py file using command line/pycharm/vs code etc


DETAILS OF THE TABLES AND SCHEMA:
TABLE 1:
	Table name : PRODUCTS
	Columns	   : NAME VARCHAR(50),
                     SKU VARCHAR(100) PRIMARY KEY,
                     DESCRIPTION VARCHAR(1000)

TABLE 2:
	Table name : PRODUCT_COUNT
	Columns    : NAME VARCHAR(50),
                     COUNT_OF_PRODUCTS INT

What is done from “Points to achieve”?

1. Created table Products with above columns
2. Made SKU column with primary key constraint
3. Taken input from .csv file and insert data into the table using parallel ingestion
4. All the data is present in this table only
5. Created an aggregated table on above rows with `name` and `no. of products` as the columns

Table Name : Products
No of Entries: 466693
Data from 10 rows:
('Bryce Jones', 'lay-raise-best-end', 'Art community floor adult your single type. Per back community former stock thing.')

('John Robinson', 'cup-return-guess', 'Produce successful hot tree past action young song. Himself then tax eye little last state vote. Country down list that speech economy leave.')

('Theresa Taylor', 'step-onto', 'Choice should lead budget task. Author best mention.\nOften stuff professional today allow after door instead. Model seat fear evidence. Now sing opportunity feeling no season show.')

('Roger Huerta', 'citizen-some-middle', 'Important fight wrong position fine. Friend song interview glass pay. Organization possible just.')

('Tiffany Johnson', 'do-many-avoid', 'Born tree wind.\nBoy marriage begin value. Record health laugh ask under notice federal. Hard lose need sell treatment.\nCertain throw executive front late. Because truth risk.')

('Roy Golden DDS', 'help-return-art', 'Pm daughter thousand.\nProcess eat employee have they example past.\nIncrease author water. Magazine child mention start.')

('David Wright', 'listen-enough-check', 'Under its near. Necessary education game everybody.\nHospital upon suffer year discussion south government nothing. Knowledge race population exist against must wear level. Coach girl situation.')

('Lauren Smith', 'grow-we-decide-job', 'Smile yet fear society theory help. Rather thing language skill since heart across wait. According ask them government or.')

('Bailey Cox', 'suggest-similar', 'Peace happy letter small some worker plant be. Play until activity season what none.\nMay serious professor whom president order. War adult number certainly also.')

('Jeffrey Davis', 'million-quality', 'See sea guy fire car.\nLose how floor main agency. Ability cold can message. Expect camera movie.\nSave training sign history alone. Sell maybe conference pay several indicate.')



Table Name: PRODUCT_COUNT
No of Entries: 212751
Data from 10 rows:
('Aaron Abbott', 1)
('Aaron Acevedo', 1)
('Aaron Acosta', 3)
('Aaron Adams', 6)
('Aaron Aguilar', 1)
('Aaron Alexander', 2)
('Aaron Allen', 5)
('Aaron Allison', 1)
('Aaron Alvarado', 3)
('Aaron Alvarez', 5)



What would you improve if given more days?
1.Create a UI for user



