<p id="readme-top" />

<div align="center">
    <img src="/assets/logo.webp" alt="Logo" height="80">
  <h1 align="center">GenCyber Coin Scraper</h3>

  <p align="center">
    A project aimed to easily grab student's coin balances from the mumbai polygon testnet.
    </br>
  </p>
</div>

## About The Project

![Product Name Screen Shot](/assets/usage.png)

As a GenCyber Teaching Assistant, we faced the challenge of manually counting Polygon Test Coins earned by students for ranking and daily prizes. This process was time-consuming and prone to errors. To address this issue, I created a web scraper using Python that automated the data retrieval from the blockchain explorer, accurately calculating each team's total points. The web scraper streamlined the ranking process, saving time and ensuring a fair competition for all participants.

### Technologies Utilized

![Python3](https://img.shields.io/badge/Python3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-1DA1F2?style=for-the-badge&logo=python&logoColor=white)

To automate the process of fetching Polygon Test Coin data for each student, I utilized the Python library "requests" to parse the Polygon blockchain explorer's website. By crafting HTTP requests and identifying which endpoints needed to be accessed, I extracted the relevant transaction data associated with each student's wallet address. This data included the number of Polygon Test Coins earned by each student, which allowed the web scraper to accurately calculate their total points for ranking. This project provided me with valuable experience in web scraping techniques and a deeper understanding of blockchain technology's practical applications.
