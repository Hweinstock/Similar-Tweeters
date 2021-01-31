import React, { Component } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import TextBoxPage from "./Component/TextBoxPage/index.js";
import TwitterPage from "./Component/TwitterPage/index.js";


export default function App() {
  return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Text Boxes</Link>
              </li>
              <li>
                <Link to="/twitter">Twitter</Link>
              </li>

            </ul>
          </nav>

          <Switch>
            <Route path="/twitter">
                <TwitterPage/>
            </Route>
            <Route path="/">
                <TextBoxPage/>
            </Route>
          </Switch>
        </div>
      </Router>
  );
}
