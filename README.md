# Penn Labs: Backend Technical Project

## Installation

The following instructions were tested with Ubuntu 16.04 LTS.

1. Run `sudo apt-get install python3 python3-pip virtualenv`.
2. Enter this repository, and run `virtualenv --python=python3 venv`.
3. Run `source venv/bin/activate` to enter the virtual environment.
4. Run `pip install -r requirements.txt`.
5. Run `./manage.py runserver`.

You should then be able to access the server at `http://localhost:8000`.

For your convenience, the server uses SQLite by default. If you want to use MySQL or PostgreSQL, edit `tasks/settings.py` and add database credentials.

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
          <li><code>description</code>: the list description</li>
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
