pandas wine project

This is my wine guide. I take 200 wines and find top 50 with best price and quality.
I use pandas lessons 1-3 from Kaggle: read csv, filter, apply, mean.

My formula is quality = points / price * stars
95+ points = 3 stars, 85+ = 2 stars, other = 1 star
Then I sort by quality and take top 50 to best_wines.csv

My result:
Average price: 77.99 to 36.74, 2 times cheaper
Average points: 90.15 to 93.58, higher
3 star wines in top: 28 from 50
Top countries: USA 12, Chile 9, France 8

How to run:
pip install pandas
python main.py

Files:
main.py, all analysis
wines_practice.csv, raw data with 200 wines
