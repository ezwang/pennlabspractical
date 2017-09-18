# Penn Labs: Backend Technical Project

## Installation

The following instructions were tested with Ubuntu 16.04 LTS.

1. Clone this project.
2. Run `sudo apt-get install python3 python3-pip virtualenv`.
3. Enter the folder this repository is in and run `virtualenv --python=python3 venv`.
4. Run `source venv/bin/activate` to enter the virtual environment.
5. Run `pip install -r requirements.txt`.
6. Run `./manage.py migrate`.
7. Run `./manage.py runserver`.

You should then be able to access the server at `http://localhost:8000`.

For your convenience, the server uses SQLite by default. If you want to use MySQL or PostgreSQL, edit `tasks/settings.py` and add database credentials.

## Useful Tips for Graders

This repository is a pretty standard Django project setup. The important things you probably want to look at are:

- tasks/apps/board/models.py - Database Models
- tasks/apps/board/views/\* - API Endpoint Implementations
- tasks/static/\* - Frontend
- tasks/templates/\* - Frontend

## API Server

### Data Structures
- Card
  - title: `String`
  - description: `String`
  - listId: `Number`
  - id: `Number`
- List
  - title: `String`
  - order: `Number`
  - id: `Number`

### API Endpoints

Responses to requests to the API server are in JSON format and at minimum contain a status code.

#### Creation

- *Adding a card*: Adds a card to the database with the given title and description. The card is associated with the list with the provided listId.
<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/card</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        Post Form Parameters:
        <ul>
          <li><code>listId</code>: the ID of the list</li>
          <li><code>title</code>: the title of the list</li>
          <li><code>description</code>: the list description (optional)</li>
        </ul>
      </td>
    </tr>
  </tbody>
<table>

- *Adding a list*: Adds a list to the database with the given title. The newly added list's order is at the end of the board.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/list</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        Post Form Parameters:
        <ul>
          <li><code>title</code>: the title of the list</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

#### Modification

- *Editing a card*: Updates the card with the provided cardId. Updates only the fields provided in the querystring.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/card/:cardId</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>cardId</code>: the ID of the desired card</li>
        </ul>
        Post Form Parameters:
        <ul>
          <li><code>title</code>: the title of the list</li>
          <li><code>description</code>: the description of the list (optional)</li>
          <li><code>listId</code>: the list that this card is associated with</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

- *Changing the order of a list*: Updates the list with the provided listId. Updates only the fields provided in the querystring.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/editlist/:listId</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>listId</code>: the ID of the list to be updated</li>
        </ul>
        Post Form Parameters:
        <ul>
          <li><code>title</code>: the title of the list</li>
          <li><code>order</code>: the new place of the list (when changing order of the lists)<br>No two lists should have the same order.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

- *Merging two lists*: Puts all of the cards from the first list into the second list, and deletes the first list.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/list/merge/:fromList/:toList</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>POST</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>fromList</code>: the ID of the list to add cards from and delete</li>
          <li><code>toList</code>: the ID of the list to add cards to</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

#### Retrieval

- *Get card by ID*: Gets title, description, and listId from the card associated with the specified cardId.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/card/:cardId</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>GET</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>cardId</code>: the ID of the desired card</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

- *Get all cards*: Gets id, title, description, and listId of all of the cards.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/card/all</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>GET</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

- *Get all lists*: Gets id, title, and order of all of the lists.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/list/all</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>GET</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>None</td>
    </tr>
  </tbody>
</table>

- *Get list by ID*: Gets title and order from the list associated with the specified listId.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/list/:listId</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>GET</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>listId</code>: the ID of the desired list</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

- *Get cards by list ID*: Gets id, title, and description of all the cards from the list associated with the specified listId.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/list/:listId/cards</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>GET</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>listId</code>: the ID of the desired list</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

#### Deletion

- *Delete card by ID*: Deletes the list associated with the specified listId.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/card/:cardId</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>DELETE</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>cardId</code>: the ID of the desired card</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

- *Delete list by ID*: Deletes the list associated with the specified listId.

<table>
  <tbody>
    <tr>
      <td>URL</td>
      <td><code>/list/:listId</code></td>
    </tr>
    <tr>
      <td>HTTP Method</td>
      <td>DELETE</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>
        URL Parameters:
        <ul>
          <li><code>listId</code>: the ID of the desired list</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### API Responses

API responses will return an appropriate HTTP response code with a JSON response. A minimum of the status code is given, along with any additional requested data. The status codes are listed below:

<table>
  <tbody>
    <tr>
      <td>200</td>
      <td>The request has succeeded.</td>
    </tr>
    <tr>
      <td>400</td>
      <td>Bad request. (ex: You passed in a string to the id field, or fields are missing.)</td>
    </tr>
    <tr>
      <td>404</td>
      <td>The object you are trying to modify does not exist.</td>
    </tr>
    <tr>
      <td>405</td>
      <td>You submitted in invalid method to an endpoint. (ex: submitting a DELETE request to <code>/editlist/:listId</code>)</td>
    </tr>
  </tbody>
</table>

## Frontend
There is an HTML user interface that enables users to add cards and add lists. You can use the frontend at `http://localhost:8000`.
