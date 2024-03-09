# Auction Site

Welcome to the Auction Site project! This project is a web application designed to facilitate online auctions, allowing users to create listings, place bids, add items to their watchlist, and interact with other users through comments.

## Project Overview

The Auction Site is built using Django for the backend and HTML, CSS, and JavaScript for the frontend. The application provides various features to support auction activities, including creating listings, viewing active listings, managing watchlists, exploring categories, and more.

## Getting Started

To run the Auction Site locally on your machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/mijwad7/commerce
    ```

2. Navigate to the project directory:

    ```bash
    cd commerce
    ```
3. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

4. Open your web browser and visit http://localhost:8000 to access the Auction Site.

## Features

- **Create Listing**: Users can create new listings, specifying title, description, starting bid, image URL, and category.
  
- **Active Listings Page**: Users can view all currently active auction listings, including title, description, current price, and photo.
  
- **Listing Page**: Each listing has its own page displaying all details, including current price, option to add to watchlist, option to place a bid, option to close auction (for creators), and comments section.
  
- **Watchlist**: Users can add listings to their watchlist and view all watched listings on a dedicated page.
  
- **Categories**: Users can explore listings by category, with each category having its own page displaying active listings in that category.
  
- **Django Admin Interface**: Site administrators can manage listings, comments, and bids via the Django admin interface.

## Models

The Auction Site includes the following models:

- **User**: Represents each user of the application.
  
- **Listing**: Represents an auction listing, including title, description, starting bid, image URL, category, and status.
  
- **Bid**: Represents a bid made on a listing, including bidder, amount, and timestamp.
  
- **Comment**: Represents a comment made on a listing, including commenter, content, and timestamp.
