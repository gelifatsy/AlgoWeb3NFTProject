import React from 'react'
import { Link, Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import Admin from './Admin'
import Trainee from './Trainee'

const Home = () => {
  // Assume isAdmin is a boolean indicating whether the user is an admin
  const isAdmin = true // Replace with actual logic to check if the user is an admin

  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/admin">Admin</Link>
          </li>
          <li>
            <Link to="/trainee">Trainee</Link>
          </li>
        </ul>

        <hr />

        <Switch>
          <Route exact path="/">
            {isAdmin ? <Admin /> : <Trainee />}
          </Route>
          <Route path="/admin">
            <Admin />
          </Route>
          <Route path="/trainee">
            <Trainee />
          </Route>
        </Switch>
      </div>
    </Router>
  )
}

export default Home
