# Penn Labs: Backend Technical Project

## Installation

TODO

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

API responses will return an appropriate HTTP response code with a JSON response. The status codes are listed below:

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
      <td>You submitted in invalid method to an endpoint. (ex: submitting a DELETE request to `/editlist/:listId`)</td>
    </tr>
  </tbody>
</table>

## Frontend
There is an HTML form that enables form users to add cards and add lists. You can use this form to test your API server. We are not concerned with the aesthetics of the form. We just care that it is functional.

## Submitting
1. Clone this repository
2. Checkout a branch structured as yourfirstname_yourlastname
3. Push all of your commits to your branch.
4. If you have any questions, confusions, or comments at all, feel SUPER FREE to email us at `niharp@seas.upenn.edu`, `rohanmen@seas.upenn.edu`, or `branlin@seas.upenn.edu`. We're here to help 😁. We'll help you through it - don't sweat!
